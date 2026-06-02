# Como contribuir

Obrigado pelo interesse em contribuir com o SENTINELA-AI.

## Fluxo recomendado

1. Abra uma issue descrevendo o problema ou melhoria.
2. Crie uma branch a partir da `main`.
3. Faça alterações pequenas e bem descritas.
4. Teste localmente.
5. Abra um pull request usando o template.

## Padrão de branches

```text
feat/nome-da-feature
fix/nome-do-ajuste
docs/nome-da-doc
chore/nome-da-tarefa
```

## Commits

Use mensagens claras:

```text
feat: adiciona documentação de integração com zabbix
fix: corrige compose do open-webui
docs: melhora guia de instalação
chore: adiciona workflow de ci
```

## Checklist antes do PR

- [ ] Não contém senha, token ou IP real.
- [ ] `docker compose -f deploy/compose.yaml config` executa sem erro.
- [ ] Scripts shell passam em `bash -n`.
- [ ] Documentação foi atualizada.
- [ ] CHANGELOG foi atualizado quando necessário.
