# Ferramenta de Análise de Logs

Este projeto é uma ferramenta de relatórios que realiza consultas no banco de dados para gerar um relatório com base nos dados retornados pelas consultas.

## Pré-requisitos

- [Docker](https://docs.docker.com/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.7.2](https://www.python.org/downloads/)
- [Pyscopg2](http://initd.org/psycopg/download/)

## Executando a aplicação

- Clone o projeto `https://github.com/gabrielmq/analise-logs.git`
- Acesse o diretório do projeto através do prompt de comando e execute o comando `docker-compose up` para que seja inicializado o container do banco de dados postgreSQL
- Com o container inicializado, dentro do diretorio do projeto execute o comando `python3 app.py` pelo prompt de comandos para inicializar a ferramenta de logs

_Obs: para finalizar a execução do container execute o comando `docker-compose down` pelo prompt de comando_

## Licensa

Este projeto foi criado durante o Nanodegree Desenvolvedor Web Full-Stack oferecido pela Udacity.