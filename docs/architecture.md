# Arquitetura do SENTINELA-AI

## Objetivo

O SENTINELA-AI foi pensado como um stack local de IA para apoiar infraestrutura de TI, suporte técnico e operação em redes restritas.

## Componentes

| Componente | Função |
|---|---|
| Open WebUI | Interface web e orquestração de conversas |
| Ollama | Execução local de modelos de linguagem |
| RAG local | Consulta a documentos técnicos sanitizados |
| Tool Server GLPI | Integração futura com chamados |
| Tool Server Zabbix | Integração futura com monitoramento |

## Fluxo básico

```text
Usuário -> Open WebUI -> Ollama
                 |
                 +-> Base RAG local
                 +-> API GLPI
                 +-> API Zabbix
```

## Portas padrão

| Serviço | Porta |
|---|---|
| Open WebUI | 3000 |
| Ollama | 11434 |

## Observações de segurança

- Em produção, restrinja o acesso por firewall.
- Não exponha Ollama ou Open WebUI diretamente na internet sem autenticação e proxy reverso seguro.
- Use dados fictícios na documentação pública.
