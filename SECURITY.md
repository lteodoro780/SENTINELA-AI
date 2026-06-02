# Política de segurança

## Como reportar vulnerabilidades

Caso encontre uma falha de segurança, não abra uma issue pública com dados sensíveis.

Entre em contato com o mantenedor do projeto informando:

- descrição do problema;
- impacto possível;
- passos mínimos para reprodução;
- versão/commit afetado;
- evidências sem segredos reais.

## O que não deve ser publicado

Não publique neste repositório:

- tokens de API;
- senhas;
- IPs internos reais;
- nomes reais de servidores;
- inventários institucionais;
- dumps de banco;
- arquivos `.env`;
- backups;
- logs com dados sensíveis.

## Escopo

Este projeto é mantido como laboratório e portfólio técnico. Exemplos de integração com GLPI, Zabbix e outros sistemas devem usar dados fictícios ou sanitizados.

## Boas práticas recomendadas

- rotacione tokens expostos acidentalmente;
- use `.env.example` para documentação;
- mantenha `.env` fora do Git;
- revise commits antes do push;
- use secret scanning do GitHub quando disponível.
