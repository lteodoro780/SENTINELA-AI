# Changelog

All notable changes to this project will be documented in this file.





# 🚀 SENTINELA 2.7 / RONDANTE 1.0 — Recent Updates

## 📌 GLPI Integration
- Functional integration with the GLPI REST API
- Automatic ticket creation through AI
- Real-time ticket queries
- Computer and printer inventory queries
- HTML cleanup and processing from GLPI API responses
- Support for categories and urgency levels in tickets
- Structure prepared for automatic ticket resolution workflows

## 🖨️ Knowledge Base
- Creation of an institutional printer catalog
- Organization by department, IP address, and serial number
- Markdown (.md) standardization
- Troubleshooting knowledge base for:
  - Printers
  - Computers
  - Networking
  - DHCP
  - VLANs
  - Switches

## 📡 Zabbix Integration
- Host querying through AI
- Switch and equipment status verification
- REST API integration with Zabbix
- Fixes for `/host-status` endpoints
- Hostname resolution improvements

## 🤖 AI Architecture
- Conceptual separation between:
  - SENTINELA → support and automation assistant
  - RONDANTE → operational consultant
- Infrastructure based on:
  - OpenWebUI
  - Ollama
  - Qwen
  - DeepSeek
- Planning for multiple specialized AI models
- Foundation for a public portal without login requirements

## 🔐 Infrastructure
- Complete LDAP authentication troubleshooting for GLPI
- Root cause identification on LDAP bind account (`esa\glpi`)
- Active Directory authentication recovery
- Apache, MySQL, and LDAP validation procedures
- Snapshot-based rollback and recovery strategy

## 🌐 Intelligent Support Portal
Planning and development of a smart pre-support portal:
- Users consult AI before opening tickets
- AI attempts automatic issue resolution
- If unresolved:
  - automatic GLPI ticket creation
  - automatic categorization
  - automatic urgency definition

## 🧠 Project Goal
Transform ESA infrastructure into a platform for:
- Intelligent Service Desk
- AI-assisted Operations
- AI-powered NOC
- Institutional Knowledge Base
- Technical support automation
- Self-hosted AI infrastructure

---

## 🛠️ Technologies Used
- OpenWebUI
- Ollama
- Qwen2.5
- DeepSeek
- FastAPI
- Python
- GLPI
- Zabbix
- Linux
- Apache
- MySQL
- LDAP / Active Directory

---

## 📅 Current Status
✅ Functional GLPI integration  
✅ Functional Zabbix integration  
✅ Automatic ticket creation  
✅ AI-based operational queries  
✅ Active institutional knowledge base  
🚧 Public SENTINELA portal in development  
🚧 AI → GLPI automated workflow under expansion
---

## [0.1.0] - Initial Release

### Added

- Initial Docker Compose environment
- Open WebUI integration
- Ollama integration
- Deployment documentation
- Networking documentation
- Architecture documentation
- Backup scripts
- Update scripts
- Docker status scripts
- Network lockdown scripts
- Initial repository structure
