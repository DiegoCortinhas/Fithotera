class Produto:
    def __init__(self,nomeBotanico,origem,volume, sintomas):
        self.__sintomas = []
        self.__nomeBotanico = nomeBotanico
        self.__origem = origem
        self.__volume = volume
        self.__sintomas = sintomas

def removeTagProduto(produto_c_tag):
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
    produto_tratada = produto_s_tag.replace("&", " ")#tirar essa linha
    produto_s_tag = produto_s_tag.replace("Sinônimos:", ",")
    return produto_s_tag


def retornaTagTratada(produto_c_tag):
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
    produto_tratada = produto_s_tag.replace("&", " ")#tirar essa linha
    return produto_tratada