#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Script responsável por encapsular o acesso a base de dados
    para realizar consultas
"""

import psycopg2
from config_acesso_db import config


# 1. Quais são os três artigos mais populares de todos os tempos?
ARTIGOS_PUPULARES_QUERY = """
    select
        a.title,
        count(l.*) articles_views
    from
        articles a,
        log l
    where
        a.slug = substring(l.path, 10) and
        l.status = '200 OK'
    group by
        a.title, l.path
    order by
        articles_views desc
    limit 3;
"""

# 2. Quem são os autores de artigos mais populares de todos os tempos?
AUTORES_POPULARES_QUERY = """
    select
        at.name,
        count(l.*) author_views
    from
        authors at,
        articles a,
        log l
    where
        at.id = a.author and
        a.slug = substring(l.path, 10) and
        l.status = '200 OK'
    group by
        at.name
    order by
        author_views desc;
"""

# 3. Em quais dias mais de 1% das requisições resultaram em erros?
ERROS_REQUISICAO_QUERY = """
    select
        to_char(request.dia,'Month DD, YYYY'),
        concat(request.porcentagem_erro,'%')
    from (
        select
            date(time) dia,
            round(
                cast(
                    sum(case when status != '200 OK' then 1 else 0 end)
                as numeric) / count(*) * 100
            , 2) porcentagem_erro
        from log
        group by dia
    ) as request
    where
        request.porcentagem_erro >= 1.00;
"""


def connect():
    """Função que faz a conexão com a base de dados"""
    conn = None

    try:
        params = config()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        conn.close()
        print(error)


def get_artigos_populares():
    """Busca os 3 artigos mais populares de todos os tempos"""
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute(ARTIGOS_PUPULARES_QUERY)
        return cursor.fetchall()
    finally:
        if db is not None:
            db.close()


def get_autores_populares():
    """
        Busca os autores de artigos mais populares de todos os tempos
    """
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute(AUTORES_POPULARES_QUERY)
        return cursor.fetchall()
    finally:
        if db is not None:
            db.close()


def get_erros_requisicao():
    """
        Retorna quais os dias que as requisições
        resultaram em mais de 1% de errors
    """
    try:
        db = connect()
        cursor = db.cursor()
        cursor.execute(ERROS_REQUISICAO_QUERY)
        return cursor.fetchall()
    finally:
        if db is not None:
            db.close()
