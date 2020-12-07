[![Python application](https://github.com/gfpaiva/wishlist-api/workflows/Python%20application/badge.svg)](https://github.com/gfpaiva/wishlist-api/actions?query=workflow%3A%22Python+application%22)
[![CodeFactor](https://www.codefactor.io/repository/github/gfpaiva/wishlist-api/badge)](https://www.codefactor.io/repository/github/gfpaiva/wishlist-api)
[![codecov](https://codecov.io/gh/gfpaiva/wishlist-api/branch/main/graph/badge.svg?token=MRSD5MVV9H)](https://codecov.io/gh/gfpaiva/wishlist-api)
[![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/gfpaiva/wishlist-api)

# WISHLIST API

[Wishlist Api](https://gfpaiva-wishlist-api.herokuapp.com/docs) É uma API Pública (com autenticação de aplicação) para criar e gerenciar listas de desejos.

Criado como side project para estudo e diversão 🤓.  
Desenvolvido a partir das especificações técnicas do desafio técnico do [LuizaLabs](http://luizalabs.com/), consumindo [API externa](https://gist.github.com/Bgouveia/9e043a3eba439489a35e70d1b5ea08ec) para detalhe dos produtos.

## ⚙️ Requisitos

Recomendado (principalmente para desenvolvimento local):

- [Docker\*](https://www.docker.com/)

Ou instalação a parte dos serviços:

- [Python 3.8](https://www.python.org/)
- [Postgres 13.0](http://postgresql.org/)
- [Redis](https://redis.io/)

\* Dica para linux: [Post-installation](https://docs.docker.com/engine/install/linux-postinstall/) recomendado para não precisar rodar comandos docker com `sudo` 😉

## 🏃🏽‍♂️ Rodando local

Primeiro de tudo você precisa criar um arquivo `.env` na raiz do projeto.  
Você pode usar o arquivo `.env.example`, apenas duplicá-lo e renomeá-lo para `.env` já te deixa preparado para o desenvolvimento local.

Scripts:

| comando       | descrição                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------- |
| make dev      | Encerra processo anterior, e cria novo através do _docker-compose_ (python, postgres e redis) |
| make dev-logs | Exibe logs dos serviços do _docker-compose_ caso estejam rodando                              |

Caso seu sistema não tenha suporte para rodar comandos do [make](https://pt.wikipedia.org/wiki/Makefile) você pode copiar e rodar manualmente as receitas que estão no arquivo `./Makefile`.  
Após os serviços e aplicação rodando, você pode acessar [http://localhost:3000](http://localhost:3000) para desenvolvimento e teste da API. Todos os endpoints estão documentados via [SwaggerUI](https://swagger.io/tools/swagger-ui/), que pode ser acessado no endereço [http://localhost:3000/docs](http://localhost:3000/docs).

Uma autenticação inicial é criada para realizar os testes local:

- usuário `wishlist`
- senha `wishlist`

(receitas podem ser conferidas em `db/init.sql`)

## ✔️ Qualidade

Alguns checks feitos no código assegurando mais qualidade:

- [Github Actions](https://github.com/gfpaiva/wishlist-api/actions?query=workflow%3A%22Python+application%22) (Lint e testes)
- [CodeCov](https://codecov.io/gh/gfpaiva/wishlist-api) (Cobertura de testes)
- [CodeFactor](https://www.codefactor.io/repository/github/gfpaiva/wishlist-api) (CodeScanner verificando vulnerabilidades e code smells)

## 🔍 Testes

Scripts:

| comando               | descrição                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------- |
| make test             | Roda testes de unidade dos services da aplicação                                                   |
| make test-cov         | Roda testes de unidade dos services da aplicação e gera relatórios de coverage                     |
| make test-integration | Inicia serviços através do _docker-compose_ e roda testes de integração dos endpoints da aplicação |

## 🚀 Deploy

Hospedado no [Heroku](https://www.heroku.com/). E pode ser acessado no endereço [https://gfpaiva-wishlist-api.herokuapp.com/docs](https://gfpaiva-wishlist-api.herokuapp.com/docs) (Documentação)  
Processo de deploy e build são feitos automaticamente após sucesso dos checks do Github Actions na branch `main`.
