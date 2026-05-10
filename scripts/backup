#!/bin/bash

BACKUP_DIR="./backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")

mkdir -p "$BACKUP_DIR"

echo "Creating backup directory: $BACKUP_DIR"

echo "Backing up Open WebUI data..."
docker run --rm \
  -v sentinela-ai_openwebui_data:/volume \
  -v "$(pwd)/$BACKUP_DIR":/backup \
  ubuntu \
  tar czf "/backup/openwebui-data-$DATE.tar.gz" -C /volume .

echo "Backing up Ollama data..."
docker run --rm \
  -v sentinela-ai_ollama_data:/volume \
  -v "$(pwd)/$BACKUP_DIR":/backup \
  ubuntu \
  tar czf "/backup/ollama-data-$DATE.tar.gz" -C /volume .

echo "Backup completed."
echo "Files saved in: $BACKUP_DIR"
