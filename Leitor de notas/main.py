''' Autor: Rodrigo L P Morosky
Projeto final para conclusão do Curso na Lets Code
Leitor de XML de nota fiscal eletrônica
Divulgação autorizada do autor para a Lets Code'''


import bs4
from lxml import etree
import pandas as pd
import os
from funcoes import Ler_Xml2

pasta = 'XML'
arquivos = os.listdir('XML/')
df = pd.DataFrame()

for f in arquivos:
    if f[-4:] == '.xml':
        arq= pasta + '/'+ f
        p = Ler_Xml2(arq)
        df = df.append(p,ignore_index=True)
    else:
        pass

lista = list(df['Emissao'])
for t in range(len(lista)):
    x = lista[t][8:10] + '/' + lista[t][5:7] + '/' + lista[t][:4]
    lista[t] = x

indice = 0
for i in df['Emissao']:
    df['Emissao'].loc[indice] = lista[indice]
    indice +=1

df_semgtin = df[df['EAN'] == 'SEM GTIN' | df['EAN'] == '']
df_comgtin = df[df['EAN'] != 'SEM GTIN' | df['EAN'] != '']
print(df)
df.to_excel('notas.xlsx')
df_semgtin.to_excel('sem gtin.xlsx')
df_comgtin.to_excel('com gtin.xlsx')