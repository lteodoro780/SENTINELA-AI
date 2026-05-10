# Networking

## Overview

SENTINELA AI was designed to operate in:

* Offline environments
* LAN-only deployments
* Restricted enterprise networks

The environment can operate without internet access after initial deployment.

---

## Default Ports

| Service    | Port  |
| ---------- | ----- |
| Open WebUI | 3000  |
| Ollama API | 11434 |

---

## LAN Access

The web interface can be accessed through:

```txt id="awhax0"
http://SERVER-IP:3000
```

Example:

```txt id="r8hxfx"
http://192.168.100.10:3000
```

---

## Recommended Network Topology

* Dedicated management VLAN
* Internal-only access
* Firewall isolation
* No external exposure

---

## Firewall Recommendations

Allow only required ports internally.

Example using UFW:

```bash id="z31efj"
sudo ufw allow 3000/tcp
sudo ufw allow 11434/tcp
```

Block external access whenever possible.

---

## Docker Networking

Containers communicate using the default Docker bridge network.

To verify:

```bash id="abndjw"
docker network ls
```

---

## Security Notes

Recommended practices:

* Avoid direct internet exposure
* Use reverse proxy if external access is required
* Restrict SSH access
* Keep Docker updated
* Use internal DNS when possible
