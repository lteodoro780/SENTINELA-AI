# Deployment

## Starting the Environment

Start all containers:

```bash id="cjlwm7"
docker-compose up -d
```

Verify running containers:

```bash id="hjjlwm"
docker ps
```

---

## Stopping the Environment

Stop containers:

```bash id="hl9s0f"
docker-compose down
```

---

## Restarting Services

Restart all services:

```bash id="g97qg0"
docker-compose restart
```

Restart individual containers:

```bash id="r7o56l"
docker restart ollama
docker restart open-webui
```

---

## Updating Containers

Pull latest images:

```bash id="bh8wwm"
docker-compose pull
```

Recreate containers:

```bash id="fjfnhk"
docker-compose up -d
```

---

## Backup

Backup Docker volumes:

```bash id="yq1u5z"
docker run --rm \
  -v ollama_data:/volume \
  -v $(pwd):/backup \
  ubuntu \
  tar cvf /backup/ollama-backup.tar /volume
```

---

## Restore

Restore backup archive:

```bash id="v6yk2w"
docker run --rm \
  -v ollama_data:/volume \
  -v $(pwd):/backup \
  ubuntu \
  bash -c "cd /volume && tar xvf /backup/ollama-backup.tar --strip 1"
```

---

## Recommended Deployment Environment

* Debian 12
* Docker Engine
* Docker Compose
* SSD storage
* Internal network deployment

---

## Notes

This environment was designed for:

* Offline infrastructure
* Internal enterprise networks
* Laboratory environments
* Self-hosted AI deployments
