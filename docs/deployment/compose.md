# Deploy com Docker Compose

## Fonte única do deploy

O arquivo canônico do stack é:

```text
deploy/compose.yaml
```

Scripts, documentação e CI devem usar esse arquivo. O antigo `docker-compose.yml` da raiz foi removido para evitar duas fontes de verdade.

O projeto Compose possui o nome fixo `sentinela-ai`, mantendo nomes previsíveis para volumes e recursos associados.

## Requisitos

- Linux com Docker instalado.
- Docker Compose v2 (`docker compose`).
- Pelo menos 8 GB de RAM para testes básicos.
- Acesso ao Docker Hub/GHCR para baixar imagens, salvo em ambiente preparado offline.

## Configuração

```bash
cp deploy/.env.example deploy/.env
nano deploy/.env
```

Troque `WEBUI_SECRET_KEY` por uma chave forte antes de utilizar o ambiente.

## Subindo o ambiente

```bash
docker compose --env-file deploy/.env -f deploy/compose.yaml up -d
```

Ou utilize o script:

```bash
./scripts/compose-up.sh
```

## Verificando contêineres

```bash
docker compose --env-file deploy/.env -f deploy/compose.yaml ps
```

Ou:

```bash
./scripts/status.sh
```

## Logs

```bash
docker compose --env-file deploy/.env -f deploy/compose.yaml logs -f
```

## Parando

```bash
docker compose --env-file deploy/.env -f deploy/compose.yaml down
```

Ou:

```bash
./scripts/compose-down.sh
```

## Atualizando

```bash
./scripts/update.sh
```

## Validando o Compose

Para validar com valores seguros de exemplo:

```bash
docker compose --env-file deploy/.env.example -f deploy/compose.yaml config
```

## Backup

O script de backup utiliza os volumes do projeto Compose `sentinela-ai`:

```bash
./scripts/backup.sh
```

Por padrão, os arquivos são gravados em `backups/`.
