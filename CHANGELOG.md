# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato segue a ideia do Keep a Changelog e o versionamento segue SemVer enquanto o projeto estiver em desenvolvimento inicial.

## [0.2.0] - 2026-06-02

### Adicionado

- README principal reorganizado.
- Estrutura de deploy em `deploy/`.
- Arquivo `deploy/.env.example`.
- Política de segurança em `SECURITY.md`.
- Guia de contribuição em `CONTRIBUTING.md`.
- Código de conduta em `CODE_OF_CONDUCT.md`.
- Templates de issue e pull request.
- Workflow inicial de CI para validação de scripts e Docker Compose.
- Documentação base para arquitetura, RAG, segredos, GLPI e Zabbix.

### Alterado

- Organização do repositório para separar documentação, deploy, scripts e serviços futuros.
- Exemplos passaram a usar dados fictícios e sanitizados.

### Segurança

- Removidas referências a dados institucionais sensíveis dos exemplos públicos.
- Reforçado uso de `.env.example` em vez de `.env`.
