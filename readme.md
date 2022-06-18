# DEVOPS - VAGRANT/PYTHON

## Pré-requisitos

Para executar essa aplicação em ambiente local, é necessário que você já tenha instalado os seguintes softwares:

- Vagrant
- Virtual box

## Executando a máquina virtual

Para que os próximos comandos sejam executados sem problemas, certifique que esteja no diretório raiz do projeto.

Subindo máquina virtual com Vagrant:

```
vagrant up
```

Durante a instalação será necessário informar a interface de rede para que o vagrant possa utilizar como ponte.

```
==> default: Available bridged network interfaces:
1) enp1s0
2) wlp2s0
...
```

O Vagrant irá baixar a imagem do CentOs 7 e irá provisionar com a instalação do Apache Zeppelin

Para acessar a máquina via SSH:

```
ssh vagrant@192.168.1.111
```
