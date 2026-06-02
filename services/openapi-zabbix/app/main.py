from typing import Any

from fastapi import FastAPI, HTTPException, Query

from .config import settings
from .zabbix_client import ZabbixClient, ZabbixError

app = FastAPI(
    title="Sentinela AI - Zabbix Tools",
    description="API interna para o Sentinela consultar hosts, grupos, problemas, triggers e itens no Zabbix.",
    version="0.1.0",
)


@app.get("/health")
async def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "service": "openapi-zabbix",
        "zabbix_url_configured": bool(settings.zabbix_url),
        "api_token_configured": bool(settings.zabbix_api_token),
    }


@app.get("/zabbix/version")
async def api_version() -> dict[str, str]:
    try:
        version = await ZabbixClient().api_version()
        return {"version": version}
    except ZabbixError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/zabbix/hosts")
async def list_hosts(
    search: str | None = Query(None, description="Busca por nome visível ou hostname"),
    limit: int = Query(20, ge=1, le=100),
) -> Any:
    try:
        return await ZabbixClient().list_hosts(search=search, limit=limit)
    except ZabbixError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/zabbix/hosts/{host_id}")
async def get_host(host_id: str) -> Any:
    try:
        return await ZabbixClient().get_host(host_id)
    except ZabbixError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/zabbix/groups")
async def list_groups(
    search: str | None = Query(None, description="Busca por nome do grupo"),
    limit: int = Query(20, ge=1, le=100),
) -> Any:
    try:
        return await ZabbixClient().list_host_groups(search=search, limit=limit)
    except ZabbixError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/zabbix/problems")
async def get_problems(
    limit: int = Query(20, ge=1, le=100),
    severity: int | None = Query(None, ge=0, le=5, description="0-5 conforme severidade do Zabbix"),
) -> Any:
    try:
        return await ZabbixClient().get_problems(limit=limit, severity=severity)
    except ZabbixError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/zabbix/triggers")
async def get_triggers(
    host_id: str | None = Query(None),
    limit: int = Query(20, ge=1, le=100),
) -> Any:
    try:
        return await ZabbixClient().get_triggers(host_id=host_id, limit=limit)
    except ZabbixError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/zabbix/items")
async def get_items(
    host_id: str = Query(...),
    search: str | None = Query(None),
    limit: int = Query(20, ge=1, le=100),
) -> Any:
    try:
        return await ZabbixClient().get_items(host_id=host_id, search=search, limit=limit)
    except ZabbixError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.get("/zabbix/history")
async def get_history(
    item_id: str = Query(...),
    value_type: int = Query(0, ge=0, le=5, description="Tipo de histórico do Zabbix. Float costuma ser 0."),
    limit: int = Query(10, ge=1, le=100),
) -> Any:
    try:
        return await ZabbixClient().get_history(item_id=item_id, value_type=value_type, limit=limit)
    except ZabbixError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
