# APIs internas de ferramentas do Sentinela

Este pacote adiciona duas APIs internas em FastAPI:

- `openapi-glpi`: consulta e atualiza chamados no GLPI.
- `openapi-zabbix`: consulta hosts, grupos, problemas, triggers, itens e histórico no Zabbix.

Essas APIs foram pensadas para serem usadas pelo Sentinela/Open WebUI como ferramentas externas, sem expor tokens diretamente para o usuário final.

## Portas padrão

| Serviço | Porta local | Documentação Swagger |
|---|---:|---|
| GLPI Tools | `5051` | `http://localhost:5051/docs` |
| Zabbix Tools | `5052` | `http://localhost:5052/docs` |

## Como subir

Copie o exemplo de ambiente:

```bash
cp deploy/.env.integrations.example deploy/.env.integrations
nano deploy/.env.integrations
```

Suba os serviços:

```bash
docker compose --env-file deploy/.env.integrations -f deploy/compose.integrations.yaml up -d --build
```

Teste:

```bash
curl http://localhost:5051/health
curl http://localhost:5052/health
```

## Endpoints GLPI

- `GET /health`
- `GET /glpi/profiles`
- `GET /glpi/tickets?limit=10`
- `GET /glpi/tickets/{ticket_id}`
- `GET /glpi/tickets/search?q=texto`
- `POST /glpi/tickets/{ticket_id}/followups`
- `POST /glpi/tickets/{ticket_id}/solve`

Exemplo para adicionar acompanhamento:

```bash
curl -X POST http://localhost:5051/glpi/tickets/123/followups \
  -H "Content-Type: application/json" \
  -d '{"content":"Teste de acompanhamento via Sentinela.","is_private":false}'
```

Exemplo para solucionar chamado:

```bash
curl -X POST http://localhost:5051/glpi/tickets/123/solve \
  -H "Content-Type: application/json" \
  -d '{"solution":"Chamado solucionado via Sentinela."}'
```

## Endpoints Zabbix

- `GET /health`
- `GET /zabbix/version`
- `GET /zabbix/hosts?search=switch&limit=20`
- `GET /zabbix/hosts/{host_id}`
- `GET /zabbix/groups?search=switch`
- `GET /zabbix/problems?limit=20`
- `GET /zabbix/triggers?host_id=12345`
- `GET /zabbix/items?host_id=12345&search=icmpping`
- `GET /zabbix/history?item_id=12345&value_type=0`

Exemplo para listar hosts com nome contendo `switch`:

```bash
curl "http://localhost:5052/zabbix/hosts?search=switch&limit=20"
```

Exemplo para listar problemas recentes:

```bash
curl "http://localhost:5052/zabbix/problems?limit=10"
```

## Segurança

Não versione `deploy/.env.integrations`.
Use somente `deploy/.env.integrations.example` no GitHub.

Nunca coloque tokens reais no README, issues, prints ou commits.
