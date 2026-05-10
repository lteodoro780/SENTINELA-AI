# Installation

## Environment Preparation

Update the system before starting:

```bash
sudo apt update && sudo apt upgrade -y
```

## Docker Installation

Install Docker and Docker Compose:

```bash
sudo apt install docker.io docker-compose -y
```

Enable Docker service:

```bash
sudo systemctl enable docker
sudo systemctl start docker
```

## Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/sentinela-ai.git
cd sentinela-ai
```

## Start Environment

```bash
docker-compose up -d
```

## Verify Containers

```bash
docker ps
```

## Access Web Interface

Open the browser:

```txt
http://SERVER-IP:3000
```

## Notes

The environment was designed for:

* Offline environments
* Enterprise networks
* Self-hosted infrastructure
* Internal AI services
