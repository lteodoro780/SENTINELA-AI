# Architecture

## Overview

SENTINELA AI is a self-hosted AI environment designed for enterprise and laboratory deployments.

The project architecture focuses on:

* Offline operation
* Modular containerized services
* Lightweight deployment
* Internal document processing
* LAN-based access

---

## Core Components

### Open WebUI

Responsible for:

* Web interface
* User interaction
* Chat management
* Model selection

Runs as a Docker container.

---

### Ollama

Responsible for:

* Local model inference
* LLM execution
* Model management

Models are stored locally on the server.

---

## Container Architecture

```text id="g5gnq0"
Client Browser
       │
       ▼
Open WebUI Container
       │
       ▼
Ollama API Container
       │
       ▼
Local AI Models
```

---

## Deployment Model

The environment was designed to support:

* Standalone servers
* Laboratory environments
* Enterprise internal networks
* Low-cost infrastructure
* Offline operation

---

## Storage

Persistent Docker volumes are used for:

* Model storage
* User data
* Chat history
* Configuration files

---

## Security Design

Recommended practices:

* Internal-only deployment
* Dedicated VLANs
* Firewall isolation
* Restricted SSH access
* No direct internet exposure

---

## Scalability

The project can be expanded using:

* Reverse proxy
* External databases
* Additional AI models
* Distributed inference servers

---

## Future Goals

* Document-based RAG support
* Centralized authentication
* Multi-user environments
* Enterprise deployment automation
* ARM-based deployments
