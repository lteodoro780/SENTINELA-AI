from __future__ import annotations

from typing import Any

import httpx

from .config import settings


class ZabbixError(RuntimeError):
    pass


class ZabbixClient:
    def __init__(self) -> None:
        self.url = settings.zabbix_url
        self.headers = {
            "Content-Type": "application/json-rpc",
            "Authorization": f"Bearer {settings.zabbix_api_token}",
        }
        self._request_id = 1

    async def call(self, method: str, params: dict[str, Any] | list[Any] | None = None) -> Any:
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or {},
            "id": self._request_id,
        }
        self._request_id += 1

        async with httpx.AsyncClient(
            timeout=settings.timeout_seconds,
            verify=settings.verify_ssl,
        ) as client:
            response = await client.post(self.url, headers=self.headers, json=payload)

        if response.status_code >= 400:
            raise ZabbixError(f"Zabbix HTTP {response.status_code}: {response.text[:500]}")

        data = response.json()
        if "error" in data:
            raise ZabbixError(str(data["error"]))

        return data.get("result")

    async def api_version(self) -> str:
        return await self.call("apiinfo.version")

    async def list_hosts(self, *, search: str | None = None, limit: int = 20) -> Any:
        params: dict[str, Any] = {
            "output": ["hostid", "host", "name", "status"],
            "selectInterfaces": ["ip", "dns", "port", "type", "main"],
            "sortfield": "name",
            "limit": limit,
        }
        if search:
            params["search"] = {"name": search, "host": search}
            params["searchByAny"] = True
        return await self.call("host.get", params)

    async def get_host(self, host_id: str) -> Any:
        return await self.call(
            "host.get",
            {
                "output": "extend",
                "hostids": [host_id],
                "selectInterfaces": "extend",
                "selectGroups": ["groupid", "name"],
                "selectTags": "extend",
            },
        )

    async def list_host_groups(self, *, search: str | None = None, limit: int = 20) -> Any:
        params: dict[str, Any] = {
            "output": ["groupid", "name"],
            "sortfield": "name",
            "limit": limit,
        }
        if search:
            params["search"] = {"name": search}
        return await self.call("hostgroup.get", params)

    async def get_problems(self, *, limit: int = 20, severity: int | None = None) -> Any:
        params: dict[str, Any] = {
            "output": "extend",
            "selectAcknowledges": "extend",
            "selectTags": "extend",
            "sortfield": ["eventid"],
            "sortorder": "DESC",
            "recent": True,
            "limit": limit,
        }
        if severity is not None:
            params["severities"] = [severity]
        return await self.call("problem.get", params)

    async def get_triggers(self, *, host_id: str | None = None, limit: int = 20) -> Any:
        params: dict[str, Any] = {
            "output": ["triggerid", "description", "priority", "value", "status"],
            "sortfield": "priority",
            "sortorder": "DESC",
            "limit": limit,
        }
        if host_id:
            params["hostids"] = [host_id]
        return await self.call("trigger.get", params)

    async def get_items(self, *, host_id: str, search: str | None = None, limit: int = 20) -> Any:
        params: dict[str, Any] = {
            "output": ["itemid", "name", "key_", "lastvalue", "lastclock", "value_type", "units"],
            "hostids": [host_id],
            "sortfield": "name",
            "limit": limit,
        }
        if search:
            params["search"] = {"name": search, "key_": search}
            params["searchByAny"] = True
        return await self.call("item.get", params)

    async def get_history(self, *, item_id: str, value_type: int = 0, limit: int = 10) -> Any:
        return await self.call(
            "history.get",
            {
                "output": "extend",
                "history": value_type,
                "itemids": [item_id],
                "sortfield": "clock",
                "sortorder": "DESC",
                "limit": limit,
            },
        )
