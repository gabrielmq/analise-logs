#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# tutorial de referência:
# http: // www.postgresqltutorial.com/postgresql-python/connect/

""" Script de configuração de conexão a base de dados.
    Este script realizar a conexão com a base de dados
    a partir dos parametros de acesso a base informados no arquivo
    database.ini
"""

from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    """
        Função responsável por ler o arquivo database.ini e
        retornar o dados de conexão com o banco
    """
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)

        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('{0} not found in the {1}'.format(section, filename))
    return db
