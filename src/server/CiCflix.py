import json
import os

def searchYear(index, search):
    ''' 
        Recebe uma lista de index's de medias e um ano de busca, retorna uma lista 
        com as medias que foram lançadas no ano de busca
    '''
    
    # percorre lista de index e compara o ano de lançamento com o ano de busca, se for igual adiciona a lista
    list = []
    for i in index:
        if "premiered" in i:  
            # se for uma serie o released de formato yyyy-mm-dd representa a data de lançamento
            year = i["premiered"].split("-")[0]
            if search == year:
                list.append(i)
        else: # se for um filme o ano de lançamento é representado por um inteiro year
            if search == str(i["year"]):
                list.append(i)
                

# Funções de busca por titulo, genero e diretor 
searchDirector = lambda x, search: [i for i in x if search in i["director"] or search in i["creator"]]
searchTitle = lambda x, search: [i for i in x if search in i["original_title"] or search in i["title_ptBR"]]
searchGenre = lambda x, search: [i for i in x if search in i["genres"]]
searchType = lambda x, search: [i for i in x if search == i["type"]]


def searchFiles(search, type):
    ''' Recebe um termo de busca e um tipo de busca, retorna uma lista com os resultados da busca'''
    
    # abre o arquivo index.json que contem os index de midias
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data/index.json")
    
    # transforma o arquivo em uma lista
    list = []
    with open(file_path) as json_file:
        list = json.load(json_file)
    
    # de acordo com o tipo de busca chama a função de busca correspondente e retorna os resultados
    if type == "titulo":
        results = searchTitle(list, search)
    elif type == "genero":
        results = searchGenre(list, search)
    elif type == "ano":
        results = searchYear(list, search)
    elif type == "diretor":
        results = searchDirector(list, search)
    elif type == "tipo": 
        results = searchType(list, search)
    return results

def searchFile(id):
    ''' Recebe um id de midia e retorna o conteudo do arquivo de midia correspondente'''
    
    # abre o arquivo file.txt que contem o conteudo da midia
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, f"data/{id}/file.txt")
    
    # transforma o arquivo em uma string e retorna
    with open(file_path) as file:
        data = file.read()
        return data
    
    