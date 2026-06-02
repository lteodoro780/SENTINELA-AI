#!/usr/bin/env bash
set -Eeuo pipefail

COMPOSE_FILE="${COMPOSE_FILE:-deploy/compose.yaml}"

docker compose -f "$COMPOSE_FILE" down
