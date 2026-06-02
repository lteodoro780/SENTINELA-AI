#!/usr/bin/env bash
set -Eeuo pipefail

OPEN_WEBUI_URL="${OPEN_WEBUI_URL:-http://localhost:3000}"
OLLAMA_URL="${OLLAMA_URL:-http://localhost:11434}"

echo "Verificando Open WebUI..."
curl -fsS "$OPEN_WEBUI_URL" >/dev/null && echo "Open WebUI OK" || echo "Open WebUI indisponível"

echo "Verificando Ollama..."
curl -fsS "$OLLAMA_URL/api/tags" >/dev/null && echo "Ollama OK" || echo "Ollama indisponível"
