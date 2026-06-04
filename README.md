# SENTINELA-AI

> Assistente local de IA para apoio à infraestrutura de TI, suporte técnico, documentação interna e automação operacional.

![Linux](https://img.shields.io/badge/Linux-333?style=for-the-badge&logo=linux)
![Docker](https://img.shields.io/badge/Docker-333?style=for-the-badge&logo=docker)
![Python](https://img.shields.io/badge/Python-333?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-333?style=for-the-badge&logo=fastapi)
![Ollama](https://img.shields.io/badge/Ollama-333?style=for-the-badge)
![GLPI](https://img.shields.io/badge/GLPI-333?style=for-the-badge)
![Zabbix](https://img.shields.io/badge/Zabbix-333?style=for-the-badge)
![Local AI](https://img.shields.io/badge/Local%20AI-333?style=for-the-badge)

---

## Visão geral

O **SENTINELA-AI** é um projeto de assistente local de inteligência artificial voltado para ambientes de infraestrutura de TI. A proposta é centralizar consultas técnicas, documentação interna, apoio a chamados, monitoramento e automações em uma solução privada, executada em ambiente controlado.

O projeto nasceu como laboratório prático para integrar IA local com rotinas reais de suporte técnico, especialmente em cenários onde privacidade, rede restrita e operação offline são importantes.

---

## Objetivo

Criar um assistente técnico capaz de auxiliar profissionais de TI em tarefas como:

- Consultar documentação interna.
- Apoiar análise de chamados.
- Consultar informações de ativos e serviços.
- Integrar dados de ferramentas como **GLPI**, **Zabbix** e **Grafana**.
- Automatizar respostas e ações operacionais.
- Disponibilizar atendimento interno via interfaces como Web, API ou Telegram.

---

## Principais recursos

- Execução local/self-hosted.
- Integração com modelos locais via **Ollama**.
- Base documental com suporte a RAG.
- API para consultas e automações.
- Possibilidade de integração com GLPI.
- Possibilidade de integração com Zabbix.
- Fluxo de uso interno via Telegram para técnicos.
- Foco em privacidade e redes restritas.
- Documentação voltada para ambientes reais de infraestrutura.

---

## Arquitetura proposta

```text
Usuário / Técnico
      |
      | Web UI / Telegram / API
      v
SENTINELA-AI
      |
      |-- Modelo local via Ollama
      |-- Base documental / RAG
      |-- API interna em Python/FastAPI
      |-- Integração GLPI
      |-- Integração Zabbix
      |-- Dashboards e informações operacionais
```

---

## Tecnologias utilizadas

| Área | Tecnologias |
|---|---|
| IA local | Ollama, modelos locais, RAG |
| Backend | Python, FastAPI |
| Infraestrutura | Linux, Docker |
| Monitoramento | Zabbix, Grafana |
| ITSM / Chamados | GLPI |
| Interface | Open WebUI, Telegram Bot, API HTTP |
| Automação | Scripts, endpoints internos, integrações |

---

## Casos de uso

### Suporte técnico interno

O assistente pode ser usado para orientar técnicos em procedimentos, comandos, soluções conhecidas e documentação de ambiente.

### Apoio a chamados

Com integração ao GLPI, o projeto pode ajudar na consulta, análise e registro de soluções de chamados.

### Monitoramento operacional

Com integração ao Zabbix e Grafana, o assistente pode consultar alertas, hosts, disponibilidade e informações relevantes da infraestrutura.

### Base de conhecimento privada

Documentos internos podem ser utilizados como fonte de consulta sem depender de serviços externos.

---

## Status do projeto

Projeto em desenvolvimento e evolução contínua.

### Já desenvolvido / em teste

- Ambiente local com IA.
- Estrutura inicial de assistente técnico.
- Testes com bases documentais.
- Testes de integração com ferramentas de infraestrutura.
- Uso interno voltado a técnicos.

### Próximos passos

- Padronizar estrutura de API.
- Melhorar documentação de instalação.
- Criar exemplos de integração com GLPI.
- Criar exemplos de integração com Zabbix.
- Adicionar prints e diagramas sem dados sensíveis.
- Criar fluxo de Telegram para uso técnico interno.
- Separar documentação em arquivos dentro de `docs/`.

---

## Estrutura sugerida do projeto

```text
SENTINELA-AI/
├── README.md
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── integrations/
├── docs/
│   ├── architecture.md
│   ├── installation.md
│   ├── glpi-integration.md
│   ├── zabbix-integration.md
│   ├── telegram-bot.md
│   └── security-notes.md
├── scripts/
├── examples/
└── docker-compose.yml
```

---

## Segurança e privacidade

Este projeto é pensado para uso interno e controlado. Ao publicar prints, exemplos ou documentações, é importante remover ou mascarar:

- IPs internos.
- Hostnames reais.
- Domínios corporativos.
- Usuários e senhas.
- Tokens de API.
- Dados de chamados.
- Nomes de servidores e ativos sensíveis.

---

## Observação

Este repositório faz parte de um laboratório pessoal/profissional de infraestrutura, automação e IA local. O objetivo é documentar o processo de aprendizado e desenvolvimento, incluindo testes, erros, correções e melhorias.

---

## Autor

**Luiz Teodoro**  
Infraestrutura de TI • Linux • Automação • Monitoramento • IA Local

- GitHub: [@lteodoro780](https://github.com/lteodoro780)
