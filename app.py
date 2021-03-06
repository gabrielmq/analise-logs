#!/usr/bin/env python3

""" Ferramenta de Análise de Logs
    Script principal que inicializa a ferramenta de analise de logs
    printando algumas informações no console.
"""

import appdb


print("\n1. Quais são os três artigos mais populares de todos os tempos?")
for artigo in appdb.get_artigos_populares():
    print("- {0} - {1} views".format(artigo[0], artigo[1]))

print("\n2. Quem são os autores de artigos mais populares de todos os tempos?")
for autor in appdb.get_autores_populares():
    print("- {0} - {1} views".format(autor[0], autor[1]))

print("\n3. Em quais dias mais de 1% das requisições resultaram em erros?")
for erros in appdb.get_erros_requisicao():
    print("- {0} - {1} erros".format(erros[0], erros[1]))
