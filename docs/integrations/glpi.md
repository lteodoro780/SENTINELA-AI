# Integração com GLPI

## Objetivo

Criar um tool server para permitir consultas seguras ao GLPI, como busca de chamados, status e detalhes básicos.

## Fluxo planejado

```text
Open WebUI -> Tool Server GLPI -> GLPI REST API
```

## Variáveis planejadas

```text
GLPI_URL=https://glpi.example.local/apirest.php
GLPI_APP_TOKEN=troque_este_valor
GLPI_USER_TOKEN=troque_este_valor
```

## Cuidados

- Não publicar tokens reais.
- Não publicar IDs de chamados reais.
- Não publicar nomes de usuários reais.
- Não publicar domínio institucional.

## Endpoints futuros

- `GET /health`
- `GET /tickets`
- `GET /tickets/{id}`
- `POST /tickets/{id}/solution`
