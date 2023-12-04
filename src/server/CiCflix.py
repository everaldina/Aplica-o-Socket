import json
import os

def searchYear(index, search):
    ''' 
        Recebe uma lista de index's de midias e um ano de busca, retorna uma lista 
        com as midias que foram lançadas no ano de busca
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
    return list
                

# Funções de busca por titulo, genero e diretor 
def searchDirector(index, search):
    ''' 
        Recebe uma lista de index's de midias e um diretor de busca, retorna uma lista 
        com as midias que foram dirigidas pelo diretor de busca
    '''
    
    list = []
    for i in index:
        # a busca é feita com a lista de diretores e criadores em lower case
        if "director" in i:
            lower_director = [j.lower() for j in i["director"]]
            for j in lower_director:
                if search in j:
                    list.append(i)
                    break
        elif "creator" in i:
            lower_creator = [j.lower() for j in i["creator"]]
            for j in lower_creator:
                if search in j:
                    list.append(j)
    return list

def searchGenre(index, search):
    ''' 
        Recebe uma lista de index's de midias e um genero de busca, retorna uma lista 
        com as midias que tem o genero de busca
    '''
    
    list = []
    for i in index:
        # a busca é feita com a lista de generos em lower case
        lower_genres = [j.lower() for j in i["genres"]]
        if search in lower_genres:
            list.append(i)
    return list


# Funções de busca por titulo e tipo
searchTitle = lambda x, search: [i for i in x if search in i["original_title"].lower() or search in i["title_ptBR"].lower()]
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
    search = search.lower()
    results = []
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
    
    