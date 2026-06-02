from typing import Any

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field

from .config import settings
from .glpi_client import GLPIClient, GLPIError

app = FastAPI(
    title="Sentinela AI - GLPI Tools",
    description="API interna para o Sentinela consultar e atualizar chamados no GLPI.",
    version="0.1.0",
)


class FollowupRequest(BaseModel):
    content: str = Field(..., min_length=3, description="Texto do acompanhamento")
    is_private: bool = Field(False, description="Define se o acompanhamento será privado")


class SolveTicketRequest(BaseModel):
    solution: str = Field(..., min_length=3, description="Texto da solução do chamado")


@app.get("/health")
async def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "service": "openapi-glpi",
        "glpi_url_configured": bool(settings.glpi_url),
        "app_token_configured": bool(settings.glpi_app_token),
        "user_token_configured": bool(settings.glpi_user_token),
    }


@app.get("/glpi/profiles")
async def get_profiles() -> Any:
    try:
        return await GLPIClient().get_my_profiles()
    except GLPIError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/glpi/tickets")
async def list_tickets(
    limit: int = Query(10, ge=1, le=100),
    status: int | None = Query(None, description="Status numérico do GLPI. Ex: 1 novo, 2 em andamento, 5 solucionado, 6 fechado"),
) -> Any:
    try:
        return await GLPIClient().list_tickets(limit=limit, status=status)
    except GLPIError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/glpi/tickets/{ticket_id}")
async def get_ticket(ticket_id: int) -> Any:
    try:
        return await GLPIClient().get_ticket(ticket_id)
    except GLPIError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/glpi/tickets/search")
async def search_ticket(
    q: str = Query(..., min_length=2),
    limit: int = Query(10, ge=1, le=100),
) -> Any:
    try:
        return await GLPIClient().search_ticket(q, limit=limit)
    except GLPIError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/glpi/tickets/{ticket_id}/followups")
async def add_followup(ticket_id: int, body: FollowupRequest) -> Any:
    try:
        return await GLPIClient().add_ticket_followup(
            ticket_id=ticket_id,
            content=body.content,
            is_private=body.is_private,
        )
    except GLPIError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/glpi/tickets/{ticket_id}/solve")
async def solve_ticket(ticket_id: int, body: SolveTicketRequest) -> Any:
    try:
        return await GLPIClient().solve_ticket(ticket_id=ticket_id, solution=body.solution)
    except GLPIError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
