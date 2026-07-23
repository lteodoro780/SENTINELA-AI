<div align="center">

# 🛡️ SENTINELA AI

### Inteligência artificial local para ambientes de infraestrutura e redes restritas

[![Linux](https://img.shields.io/badge/Linux-supported-333?style=for-the-badge&logo=linux)](https://www.linux.org/)
[![Docker](https://img.shields.io/badge/Docker-required-333?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![Ollama](https://img.shields.io/badge/Ollama-local_AI-333?style=for-the-badge)](https://ollama.com/)
[![Open WebUI](https://img.shields.io/badge/Open_WebUI-interface-333?style=for-the-badge)](https://github.com/open-webui/open-webui)
[![License](https://img.shields.io/badge/License-MIT-333?style=for-the-badge)](LICENSE)

</div>

---

## Sobre o projeto

O **Sentinela AI** é um ambiente de inteligência artificial auto-hospedado, criado para funcionar localmente em laboratórios, redes internas e ambientes com acesso limitado ou sem acesso à internet.

A solução utiliza **Ollama** para executar modelos de linguagem na própria infraestrutura e **Open WebUI** como interface de conversa. O projeto prioriza privacidade, baixo custo, controle dos dados e facilidade de implantação com Docker.

## Principais recursos

- Execução de modelos de IA localmente.
- Interface web acessível pela rede interna.
- Implantação com Docker Compose.
- Operação em ambientes offline ou restritos.
- Persistência dos modelos e das configurações.
- Compatibilidade com servidores e computadores Linux.
- Base preparada para integrações futuras com ferramentas de infraestrutura.
- Documentação e scripts voltados à automação do ambiente.

## Tecnologias

- **Linux** — sistema recomendado para hospedagem.
- **Docker e Docker Compose** — criação e gerenciamento dos serviços.
- **Ollama** — execução local dos modelos de IA.
- **Open WebUI** — interface web para interação com os modelos.
- **Shell Script** — instalação, configuração e automação.

## Arquitetura

```text
Usuário na rede local
        │
        ▼
Open WebUI — porta 3000
        │
        ▼
Ollama — porta 11434
        │
        ▼
Modelo de IA armazenado localmente
```

Os serviços utilizam volumes persistentes para manter modelos, usuários e configurações mesmo após a reinicialização dos contêineres.

## Estrutura do repositório

```text
SENTINELA-AI/
├── docs/                 # Documentação técnica e guias
├── images/               # Imagens, diagramas e capturas de tela
├── scripts/              # Scripts de instalação e automação
├── docker-compose.yml    # Definição dos serviços principais
├── CHANGELOG.md          # Histórico de alterações
├── LICENSE               # Licença do projeto
└── README.md             # Apresentação e instruções principais
```

## Requisitos

Antes de iniciar, tenha instalado:

- Linux com suporte ao Docker.
- Docker Engine.
- Docker Compose.
- Pelo menos 8 GB de RAM para modelos pequenos; modelos maiores exigem mais memória.
- Espaço em disco suficiente para armazenar os modelos escolhidos.

O desempenho depende do modelo, da quantidade de memória RAM e da disponibilidade de aceleração por GPU.

## Instalação rápida

Clone o repositório:

```bash
git clone https://github.com/lteodoro780/SENTINELA-AI.git
cd SENTINELA-AI
```

Inicie os serviços:

```bash
docker compose up -d
```

Verifique os contêineres:

```bash
docker compose ps
```

Acesse a interface pelo navegador:

```text
http://IP-DO-SERVIDOR:3000
```

## Baixando um modelo

Exemplo com um modelo leve:

```bash
docker exec -it ollama ollama pull qwen2.5:1.5b
```

Para listar os modelos instalados:

```bash
docker exec -it ollama ollama list
```

Depois, selecione o modelo diretamente na interface do Open WebUI.

## Comandos úteis

Parar os serviços:

```bash
docker compose down
```

Reiniciar os serviços:

```bash
docker compose restart
```

Acompanhar os logs:

```bash
docker compose logs -f
```

Atualizar as imagens dos contêineres:

```bash
docker compose pull
docker compose up -d
```

## Segurança

Para uso em ambiente corporativo ou institucional:

- Restrinja as portas ao segmento de rede necessário.
- Não exponha o Ollama diretamente à internet.
- Utilize firewall e controle de acesso.
- Não publique arquivos `.env`, senhas, tokens ou endereços internos.
- Revise os modelos e documentos antes de disponibilizá-los aos usuários.
- Mantenha backups dos volumes persistentes.

O projeto foi pensado para execução interna. A configuração de segurança deve ser adaptada às políticas de cada ambiente.

## Objetivos futuros

- Integração com ferramentas como Zabbix e GLPI.
- Base de conhecimento local com RAG.
- Perfis de acesso para administradores e usuários.
- Scripts adicionais de instalação, backup e isolamento de rede.
- Monitoramento dos serviços do ambiente.
- Suporte a novos modelos e configurações de hardware.

## Status

O Sentinela AI está em desenvolvimento ativo. Consulte o arquivo [CHANGELOG.md](CHANGELOG.md) para acompanhar as versões e alterações.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

## Autor

Desenvolvido por [Luis Teodoro](https://github.com/lteodoro780).
