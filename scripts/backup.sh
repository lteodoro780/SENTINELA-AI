#!/usr/bin/env bash
set -Eeuo pipefail

BACKUP_DIR="${BACKUP_DIR:-backups}"
DATE="$(date +%Y%m%d-%H%M%S)"

mkdir -p "$BACKUP_DIR"

echo "Gerando backup dos volumes Docker..."
docker run --rm \
  -v sentinela-ai_openwebui_data:/openwebui_data:ro \
  -v sentinela-ai_ollama_data:/ollama_data:ro \
  -v "$(pwd)/$BACKUP_DIR":/backup \
  alpine sh -c "tar czf /backup/sentinela-ai-$DATE.tar.gz /openwebui_data /ollama_data"

echo "Backup criado em: $BACKUP_DIR/sentinela-ai-$DATE.tar.gz"
