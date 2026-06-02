from __future__ import annotations

from typing import Any

import httpx

from .config import settings


class GLPIError(RuntimeError):
    pass


class GLPIClient:
    def __init__(self) -> None:
        self.base_url = settings.glpi_url.rstrip("/")
        self.headers = {
            "App-Token": settings.glpi_app_token,
            "Authorization": f"user_token {settings.glpi_user_token}",
            "Content-Type": "application/json",
        }

    async def _request(
        self,
        method: str,
        path: str,
        *,
        session_token: str | None = None,
        **kwargs: Any,
    ) -> Any:
        headers = dict(self.headers)
        if session_token:
            headers["Session-Token"] = session_token
            headers.pop("Authorization", None)

        async with httpx.AsyncClient(
            timeout=settings.timeout_seconds,
            verify=settings.verify_ssl,
        ) as client:
            response = await client.request(
                method,
                f"{self.base_url}/{path.lstrip('/')}",
                headers=headers,
                **kwargs,
            )

        if response.status_code >= 400:
            raise GLPIError(f"GLPI HTTP {response.status_code}: {response.text[:500]}")

        if not response.content:
            return None
        return response.json()

    async def init_session(self) -> str:
        data = await self._request("GET", "initSession")
        token = data.get("session_token") if isinstance(data, dict) else None
        if not token:
            raise GLPIError("GLPI não retornou session_token em initSession")
        return token

    async def kill_session(self, session_token: str) -> None:
        await self._request("GET", "killSession", session_token=session_token)

    async def get_my_profiles(self) -> Any:
        session = await self.init_session()
        try:
            return await self._request("GET", "getMyProfiles", session_token=session)
        finally:
            await self.kill_session(session)

    async def list_tickets(self, *, limit: int = 10, status: int | None = None) -> Any:
        session = await self.init_session()
        try:
            params: dict[str, Any] = {
                "range": f"0-{max(limit - 1, 0)}",
                "sort": "date_mod",
                "order": "DESC",
            }
            if status is not None:
                params["criteria[0][field]"] = "12"
                params["criteria[0][searchtype]"] = "equals"
                params["criteria[0][value]"] = status
            return await self._request("GET", "Ticket", session_token=session, params=params)
        finally:
            await self.kill_session(session)

    async def get_ticket(self, ticket_id: int) -> Any:
        session = await self.init_session()
        try:
            return await self._request("GET", f"Ticket/{ticket_id}", session_token=session)
        finally:
            await self.kill_session(session)

    async def search_ticket(self, query: str, *, limit: int = 10) -> Any:
        session = await self.init_session()
        try:
            params = {
                "criteria[0][field]": "1",
                "criteria[0][searchtype]": "contains",
                "criteria[0][value]": query,
                "range": f"0-{max(limit - 1, 0)}",
            }
            return await self._request("GET", "search/Ticket", session_token=session, params=params)
        finally:
            await self.kill_session(session)

    async def add_ticket_followup(self, ticket_id: int, content: str, *, is_private: bool = False) -> Any:
        session = await self.init_session()
        try:
            payload = {
                "input": {
                    "items_id": ticket_id,
                    "itemtype": "Ticket",
                    "content": content,
                    "is_private": 1 if is_private else 0,
                }
            }
            return await self._request("POST", "ITILFollowup", session_token=session, json=payload)
        finally:
            await self.kill_session(session)

    async def solve_ticket(self, ticket_id: int, solution: str) -> Any:
        session = await self.init_session()
        try:
            payload = {
                "input": {
                    "items_id": ticket_id,
                    "itemtype": "Ticket",
                    "solutiontypes_id": 0,
                    "content": solution,
                }
            }
            return await self._request("POST", "ITILSolution", session_token=session, json=payload)
        finally:
            await self.kill_session(session)
