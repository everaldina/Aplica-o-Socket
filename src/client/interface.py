import os
from client import searchFile, streamFile
import json

def main():
    # menu principal
    while(1):
        logo_grande()
        print("\t\t1. Busca por titulo")
        print("\t\t2. Busca por genero")
        print("\t\t3. Busca por ano")
        print("\t\t4. Busca por diretor")
        print("\t\t5. Busca por tipo")
        print("\t\t0. Sair")
        opc = input("Busca por: ")
            
        busca = menu(opc)
        
        if busca is None:
            continue
            
        match opc:
            case "1":
                procura_por = "titulo"
            case "2":
                procura_por = "genero"
            case "3":
                procura_por = "ano"
            case "4":
                procura_por = "diretor"
            case "5":
                procura_por = "tipo"
        list = searchFile(busca, procura_por)
        
        limpar_terminal()
        logo_pequena()
        print(f"-------Resultados-------")
        ids = print_media(list)
        if len(ids) == 0:
            print("Nenhum resultado encontrado")
            input()
            limpar_terminal()
            continue
        else:
            id_selected = input("Selecione o id para assistir ou 0 para voltar: ")
            if id_selected == "0":
                continue
            if id_selected not in ids:
                print("Opcao invalida")
                input()
                limpar_terminal()
                continue
            else:
                limpar_terminal()
                for i in list:
                    if str(i["id"]) == id_selected:
                        selected = i
                        break
                print(f"Assistindo {selected['title_ptBR']}")
                streamFile(id_selected)
                print("Fim.......")
                input("Pressione enter para voltar ao menu principal......")
                limpar_terminal()
                    
        
        
    
        
    
def menu(opc):
    tipo = ["titulo", "genero", "ano", "diretor", "tipo"]
    textos = ["BUSCA POR TITULO", "BUSCA POR GENERO", "BUSCA POR ANO", "BUSCA POR DIRETOR", "BUSCA POR TIPO"]
    
    try:
        opc = int(opc)
    except:
        print("Opcao invalida")
        input()
        limpar_terminal()
        return
    if(opc == 0):
        print("Saindo...")
        exit()
    elif(opc < 1 or opc > 5):
        print("Opcao invalida")
        input()
        limpar_terminal()
        return
    else:
        limpar_terminal()
        logo_pequena()
        print(textos[opc-1])
        if(opc == 5):
            print("1. Filme")
            print("2. Serie")
            try:
                opc = int(input("Digite o tipo: "))
            except:
                print("Opcao invalida")
                input()
                limpar_terminal()
                return
            if opc == 1:
                busca = "filme"
            elif opc == 2:
                busca = "serie"
            else:
                print("Opcao invalida")
                input()
                limpar_terminal()
                return
        else:
            busca = input(f"Digite o {tipo[opc-1]}: ")
        return busca

def limpar_terminal():
    sistema_operacional = os.name

    if sistema_operacional == 'posix':  # Linux ou macOS
        os.system('clear')
    elif sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:
        print()


def print_media(list):
    ids = []
    for i in list:
        print(f'{i["id"]} - \t{i["title_ptBR"]} ({i["original_title"]})')
        if i["type"] == "movie":
            print("\t   - Filme")
            print(f'\t   - Ano: {i["year"]}\n\t   - Duracao{i["duration"]} min')
        else:
            print("\t   - Serie")
            print(f'\t   - Lancamento: {i["premiered"].split("-")[0]}\n\t   - {i["seasons"]} temporadas')
        ids.append(str(i["id"]))
    return ids

def logo_grande():
    print("\n")
    print("  ,ad8888ba,   88    ,ad8888ba,      ad88  88  88")
    print(" d8'      `8b  88   d8'      `8b    d8     88  88  8b,     ,d8")
    print("d8'            88  d8'              88                   88")
    print("88             88  88             MM88MMM  88  88  `Y8, ,8P'")
    print("88             88  88               88     88  88    )888(")
    print("Y8,            88  Y8,              88     88  88   ,d8 8b,")
    print(" `Y8888Y'      88    `Y8888Y'       88     88  88  8P'     `Y8")
    print()

def logo_pequena():
    print("\n")
    print("\t\t   ___ ___  ___    __ _ _ ")
    print("\t\t  / __|_ _|/ __|  / _| (_)_ __")
    print("\t\t | (__ | |  (__  |  _| |  \\ \\")
    print("\t\t  \\___|___|\\___| |_| |_|_/__/")
    print()
    
if __name__ == "__main__":
    main()