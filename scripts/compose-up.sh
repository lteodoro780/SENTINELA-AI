#!/usr/bin/env bash
set -Eeuo pipefail

COMPOSE_FILE="${COMPOSE_FILE:-deploy/compose.yaml}"

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker não encontrado."
  exit 1
fi

docker compose -f "$COMPOSE_FILE" up -d
docker compose -f "$COMPOSE_FILE" ps
