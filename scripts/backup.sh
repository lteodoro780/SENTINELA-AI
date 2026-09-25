#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"
BACKUP_DIR="${BACKUP_DIR:-$REPO_ROOT/backups}"
DATE="$(date +%Y%m%d-%H%M%S)"

OPENWEBUI_VOLUME="sentinela-ai_openwebui_data"
OLLAMA_VOLUME="sentinela-ai_ollama_data"

mkdir -p "$BACKUP_DIR"
BACKUP_DIR="$(cd -- "$BACKUP_DIR" && pwd)"

for volume in "$OPENWEBUI_VOLUME" "$OLLAMA_VOLUME"; do
  if ! docker volume inspect "$volume" >/dev/null 2>&1; then
    echo "Volume Docker não encontrado: $volume"
    echo "Inicie o stack do Sentinela antes de executar o backup."
    exit 1
  fi
done

echo "Gerando backup dos volumes Docker..."
docker run --rm \
  -v "$OPENWEBUI_VOLUME":/openwebui_data:ro \
  -v "$OLLAMA_VOLUME":/ollama_data:ro \
  -v "$BACKUP_DIR":/backup \
  alpine sh -c "tar czf /backup/sentinela-ai-$DATE.tar.gz /openwebui_data /ollama_data"

echo "Backup criado em: $BACKUP_DIR/sentinela-ai-$DATE.tar.gz"
