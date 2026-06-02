# Deploy com Docker Compose

## Requisitos

- Linux com Docker instalado.
- Docker Compose v2.
- Pelo menos 8 GB de RAM para testes básicos.
- Acesso ao Docker Hub/GHCR para baixar imagens, salvo em ambiente preparado offline.

## Subindo o ambiente

```bash
cp deploy/.env.example deploy/.env
nano deploy/.env
docker compose -f deploy/compose.yaml up -d
```

## Verificando containers

```bash
docker compose -f deploy/compose.yaml ps
```

## Logs

```bash
docker compose -f deploy/compose.yaml logs -f
```

## Parando

```bash
docker compose -f deploy/compose.yaml down
```

## Validando o Compose

```bash
docker compose -f deploy/compose.yaml config
```
