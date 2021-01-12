'''''''''''''''''''''''''''''''''
Web-scraping da página de óleos essenciais da Lazlo
Authors: Diego Cortinhas, Marcio Kriiger, Rafael Santos e Ricardo de Castro
'''''''''''''''''''''''''''''''''
from builtins import print
import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from mysql.connector import Error

# Variáveis para preparar a inserção no banco
connection = mysql.connector.connect(host='localhost', database='fithotera', user='root',password='admin')
cursor = connection.cursor()
add_produto = ("INSERT INTO produto "
               "(nomeBotanico, origem, descricao) "
               "VALUES (%s, %s, %s)")

lista_paginas = []
lista_Numero_Paginas = []
pagina_base = 'https://www.emporiolaszlo.com.br/aromatologia/oleosessenciais.html?p='
lista_itens = []
nomeBotanico = ""
nomeBotanico_aux = []
descricao = []
origem = ""
contador = 0
descricao_aux = []

def removeTagPProduto(produto_c_tag):
    produto_s_tag = produto_c_tag.replace("<strong>", "")
    produto_s_tag = produto_s_tag.replace("</strong>", "")
    produto_s_tag = produto_s_tag.replace("<em>", "")
    produto_s_tag = produto_s_tag.replace("<br/>", "&")
    produto_s_tag = produto_s_tag.replace("</span>", "")
    produto_s_tag = produto_s_tag.replace("<span>", "")
    produto_s_tag = produto_s_tag.replace("<em>", "")
    produto_s_tag = produto_s_tag.replace("</em>", "")
    produto_s_tag = produto_s_tag.replace("<br>", "")
    produto_s_tag = produto_s_tag.replace("</br>", "")
    produto_s_tag = produto_s_tag.replace("<p>", "")
    produto_s_tag = produto_s_tag.replace("</p>", "")
    produto_s_tag = produto_s_tag.replace("<address>", "")
    produto_s_tag = produto_s_tag.replace("</address>", "")
    produto_s_tag = produto_s_tag.replace("Sinônimos:", ",")
    return produto_s_tag

# Percorre as páginas de oleos essenciais
for i in range (1):
    lista_Numero_Paginas = i + 1
    pagina_base = pagina_base + str(lista_Numero_Paginas)
    page = requests.get(pagina_base)
    soup = BeautifulSoup(page.content, 'html.parser')
    products2 = soup.select('h2.product-name')
    links = soup.select('h2.product-name > a')
    # Percorre as páginas de cada produto
    for ahref in links:
        text = ahref.text
        text = text.strip() if text is not None else ''
        print(text)
        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        href = href.lower()
        #Remove os casos que nao são oleos essenciais
        if (not href.__contains__("kit")):
            lista_paginas.append(href)

            page2 = requests.get(href)
            soup = BeautifulSoup(page2.content, 'html.parser')
            produto_c_tag = str(soup.select('div.short-description > div.std > p'))
            produto_c_tag2 = str(soup.select('div.short-description > div.std > address'))
           
            if (produto_c_tag != "[]"):
                produto_s_tag = removeTagPProduto(produto_c_tag)
                print("processando tag p")
                
            else:
                if (produto_c_tag2 != "[]"):
                    print("processando tag address")
                    produto_s_tag = removeTagPProduto(produto_c_tag2)
                else:
                    print("Produto não inserido no banco: " + text + " - Sem descricao")
        
            if(produto_s_tag.__contains__("Origem:")):
                regex_base = "(:\s)([A-zÀ-ÿ0-9 \/]+)(|&)"
                if (re.findall(regex_base, produto_s_tag) != []):
                    descricao.append(re.findall(regex_base, produto_s_tag))
                    nomeBotanico = str(descricao[contador][0][1])
                    origem = str(descricao[contador][1][1])
                    produto_tratada = produto_s_tag.replace("&", " ")
                    dados_produto = (nomeBotanico, origem, produto_tratada)
                    cursor.execute(add_produto, dados_produto)
                    connection.commit()
                    print("Inserindo nome botânico: ",nomeBotanico)
                    print("Inserindo origem: ",origem)
                    contador = contador+1

    pagina_base = 'https://www.emporiolaszlo.com.br/aromatologia.html?cat=12&p='

cursor.close()
connection.close()