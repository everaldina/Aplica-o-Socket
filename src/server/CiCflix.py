import json
import os

def searchYear(index, search):
    list = []
    for i in index:
        if "premiered" in i:
            year = i["premiered"].split("-")[0]
            if search == year:
                list.append(i)
        else:
            if search == str(i["year"]):
                list.append(i)
                
def searchType(index, search):
    if search == "filme":
        search = "movie"
    elif search == "serie":
        search = "tv show"
        
    list = []
    for i in index:
        if i["type"] == search:
            list.append(i)
    return list
            
searchDirector = lambda x, search: [i for i in x if search in i["director"] or search in i["creator"]]
searchTitle = lambda x, search: [i for i in x if search in i["original_title"] or search in i["title_ptBR"]]
searchGenre = lambda x, search: [i for i in x if search in i["genres"]]

def searchFile(search, type):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data/index.json")
    list = []
    
    with open(file_path) as json_file:
        list = json.load(json_file)
        
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
    
    