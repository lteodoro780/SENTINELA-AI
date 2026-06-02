# Variáveis de ambiente e segredos

## Regra principal

Nunca publique arquivos `.env` reais.

Use apenas:

```text
.env.example
```

## Exemplos de dados proibidos

- Senhas reais.
- Tokens GLPI.
- Tokens Zabbix.
- API keys.
- IPs internos.
- Nome real de servidores.
- Usuários LDAP reais.
- Inventário institucional.

## Gerando chave para WEBUI_SECRET_KEY

```bash
openssl rand -hex 32
```

## Antes de commitar

```bash
git status
git diff
```

Confira se nenhum segredo entrou no commit.
