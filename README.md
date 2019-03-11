# Análise de Logs

Este projeto é uma ferramenta de análise de logs para um site de notícias que extraí informações de um banco de dados PostgreSQL para gerar um relatório que responde a três perguntas:

- Quais são os três artigos mais populares de todos os tempos?
- Quem são os autores de artigos mais populares de todos os tempos?
- Em quais dias mais de 1% das requisições resultaram em erros?

## Pré-requisitos

- Docker
- Docker Compose
- Python 3.7.2
- Psycopg2
- PostgreSQL

## Executando a aplicação com Docker Compose

- Clone o projeto `https://github.com/gabrielmq/analise-logs.git`
- Acesse o diretório do projeto através do prompt de comando e execute o comando `docker-compose up` para que seja inicializado o container do banco de dados postgreSQL e o banco seja populado com os dados do arquivo `newsdata.sql.gz`
- Com o container inicializado, dentro do diretorio do projeto execute o comando `python3 app.py` pelo prompt de comandos para inicializar a ferramenta de análise logs

_Obs: para finalizar a execução do container execute o comando `docker-compose down` pelo prompt de comando_

## Executando a aplicação sem Docker Compose

Caso possua um banco de dados PostgreSQL instalado em sua máquina, siga os passo abaixo:

- Crie um novo usuário chamado vagrant e uma nova base de dados chamada news.
- Baixe o arquivo newsdata.zip clicando [aqui](https://bit.ly/2y4PPQy).
- Após descompactar o arquivo newsdata.zip, execute o comando `psql -d news -f newsdata.sql` no prompt de comando para que a base de dados news seja populada
- Clone o projeto `https://github.com/gabrielmq/analise-logs.git`
- Acesse o diretório do projeto pelo prompt de comando e execute o comando `python3 app.py` para inicializar a ferramenta de análise de log


## Licensa

Este projeto foi criado durante o Nanodegree Desenvolvedor Web Full-Stack oferecido pela Udacity.
