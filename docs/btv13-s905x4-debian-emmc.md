# BTV13 Amlogic S905X4 com Debian na eMMC

## Visão geral

Este documento registra um teste de reaproveitamento de TV Box BTV13 com SoC Amlogic S905X4, utilizando Debian instalado diretamente na eMMC.

O objetivo é documentar o processo como parte do projeto Vanguardeira, demonstrando a possibilidade de reutilizar hardware de TV Box como mini computador Linux ou terminal leve para laboratório, estudo, automação e uso educacional.

## Hardware utilizado

- Dispositivo: BTV13
- SoC: Amlogic S905X4
- Arquitetura: ARM64
- Armazenamento: eMMC interna
- Mídia auxiliar: cartão microSD com adaptador USB
- Sistema instalado: Debian ARM64

## Contexto do teste

Durante os testes iniciais com imagens Armbian/Ophub, foi identificado que algumas imagens não traziam DTBs específicos para a família SC2/S905X4.

A pasta de DTBs continha arquivos para famílias anteriores, como:

- meson-g12
- meson-sm1
- meson-gxl
- meson-gxm

O DTB mais próximo encontrado era voltado ao S905X3, como:

```text
meson-sm1-x88-pro-x3.dtb
```

Porém, para o S905X4, o ideal seria utilizar arquivos da família SC2, como:

```text
sc2_s905x4_*.dtb
```

## Destravamento e instalação

Foi utilizado o DevMFC em conjunto com uma ROM da X99 para destravar o boot do equipamento e permitir a instalação do Debian na eMMC.

Após o procedimento, a BTV13 passou a inicializar o Debian diretamente pela memória interna, sem depender do cartão SD para boot.

## Resultado

Status atual:

- Debian rodando na eMMC
- Boot funcional
- Dispositivo reaproveitado como ambiente Linux ARM64
- Base pronta para testes de desktop leve, automação ou mini servidor

## Comandos de validação

Após o boot no Debian, recomenda-se executar:

```bash
uname -a
cat /proc/device-tree/model
lsblk
free -h
df -h
```

Esses comandos ajudam a validar:

- versão do kernel
- modelo/DTB carregado
- partições da eMMC
- memória RAM disponível
- uso do armazenamento

## Backup recomendado

Antes de novas alterações, recomenda-se gerar uma imagem da eMMC:

```bash
sudo dd if=/dev/mmcblk0 of=/root/backup-btv13-emmc.img bs=4M status=progress
```

Depois, copie esse backup para outro computador ou armazenamento externo.

> Não mantenha o único backup dentro da própria eMMC.

## Possíveis usos no projeto Vanguardeira

A BTV13 com Debian pode ser usada como:

- terminal Linux educacional;
- mini computador para navegação e pacote office leve;
- thin client;
- nó de laboratório para redes;
- host para serviços leves;
- cliente de monitoramento;
- equipamento de estudo em Linux embarcado.

## Próximos passos

- Validar rede cabeada e Wi-Fi;
- Testar ambiente gráfico leve, como XFCE ou LXQt;
- Instalar ferramentas educacionais;
- Criar imagem padrão;
- Documentar processo de clonagem;
- Avaliar estabilidade em uso contínuo.
