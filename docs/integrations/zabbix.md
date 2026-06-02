# Integração com Zabbix

## Objetivo

Criar um tool server para consultar dados do Zabbix, como hosts, grupos, interfaces e status.

## Fluxo planejado

```text
Open WebUI -> Tool Server Zabbix -> Zabbix API
```

## Variáveis planejadas

```text
ZABBIX_URL=https://zabbix.example.local/api_jsonrpc.php
ZABBIX_API_TOKEN=troque_este_valor
```

## Exemplo conceitual de consulta

```json
{
  "jsonrpc": "2.0",
  "method": "host.get",
  "params": {
    "output": ["hostid", "host", "name"],
    "selectInterfaces": ["ip"]
  },
  "id": 1
}
```

## Cuidados

- Não publicar token real.
- Não publicar IPs reais.
- Não publicar nomes reais de hosts.
- Usar exemplos fictícios.
