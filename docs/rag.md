# RAG e base documental

## Objetivo

Permitir que o assistente consulte documentos técnicos locais, como runbooks, procedimentos e anotações de laboratório.

## Tipos de documentos recomendados

- Procedimentos técnicos sanitizados.
- Guias internos sem dados sensíveis.
- Checklists.
- Documentação de laboratório.
- Exemplos fictícios.

## O que não deve entrar na base pública

- IPs reais.
- Senhas.
- Tokens.
- Inventário institucional.
- Dados pessoais.
- Documentos internos sem autorização.

## Boas práticas

- Criar versões públicas e sanitizadas dos documentos.
- Remover nomes de servidores.
- Substituir IPs por exemplos como `192.0.2.10`, `10.0.0.10` ou `example.local`.
- Separar base real privada da documentação pública.
