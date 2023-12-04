import os
from client import searchFile, streamFile, closeServer

def main():
    '''
        Função principal da interface do usuario, é responsavel por 
        chamar as funções de busca e stream.
    '''
    
    while(1):
        logo_grande()
        # menu principal
        print("\t\t1. Busca por titulo")
        print("\t\t2. Busca por genero")
        print("\t\t3. Busca por ano")
        print("\t\t4. Busca por diretor")
        print("\t\t5. Busca por tipo")
        print("\t\t0. Sair")
        opc = input("Busca por: ")
        
        # busca vai receber o termo de busca que o usuario digitou
        busca = menu(opc)
        
        # --- é usado para separar os dados enviados ao servidor e nao pode ser usado como busca
        if busca is not None and "---" in busca:
            print("Cadeia de caracterer '---' invalido")
            input()
            limpar_terminal()
            continue
        
        # caso o usuario tenha digitado algo invalido busca vai ser None
        if busca is None:
            continue
        
        # manda o tipo de busca para o servidor de acordo com a opção escolhida
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
                
        # sevidor deve mandar uma lista com os resultados da busca
        # caso haja um erro na conexão com o servidor um erro é levantado
        try:
            list = searchFile(busca, procura_por)
        except Exception as e:
            print(str(e))
        
        # imprime os resultados da busca
        limpar_terminal()
        logo_pequena()
        print(f"-------Resultados-------")
        
        
        if len(list) == 0: # se a lista estiver vazia
            print("Nenhum resultado encontrado")
            input()
            limpar_terminal()
            continue
        else: 
            # print_media imprime os resultados da busca e retorna uma lista com os ids
            ids = print_media(list)
            
            # o usuario pode escolher um id para assistir ou voltar ao menu principal
            id_selected = input("Selecione o id para assistir ou 0 para voltar: ")
            
            if id_selected == "0": # se o usuario escolher voltar
                continue
            if id_selected not in ids: # caso o usuario digite um id invalido
                print("Opcao invalida")
                input()
                limpar_terminal()
                continue
            else: # se o usuario escolher um id valido
                limpar_terminal()
                
                # procura o id selecionado na lista de resultados
                for i in list:
                    if str(i["id"]) == id_selected:
                        selected = i
                        break
                
                print(f"Assistindo {selected['title_ptBR']}")
                
                # tenta fazer o stream do arquivo, caso haja um erro uma mensagem é impressa
                try:
                    streamFile(id_selected) # faz o stream do arquivo
                    print("Fim.......")
                    input("Pressione enter para voltar ao menu principal......")
                except Exception as e:
                    print(str(e))
                    input()
                limpar_terminal()
                    
        

        
    
def menu(opc):
    ''' Um menu que recebe uma opcao e retorna um termo de busca'''
    
    # string com opçoes de busca
    tipo = ["titulo", "genero", "ano", "diretor", "tipo"]
    textos = ["BUSCA POR TITULO", "BUSCA POR GENERO", "BUSCA POR ANO", "BUSCA POR DIRETOR", "BUSCA POR TIPO"]
    
    # verifica se a opcao digitada é um numero
    try:
        opc = int(opc)
    except:
        print("Opcao invalida")
        input()
        limpar_terminal()
        return
    
    if(opc == 0): # se o usuario escolher sair o servidor é fechado
        print("Saindo...")
        closeServer()
        exit()
    elif(opc < 1 or opc > 5): # se o usuario escolher uma opcao invalida
        print("Opcao invalida")
        input()
        limpar_terminal()
        return
    else: # se o usuario escolher uma opcao valida
        # impressao de cabeçalho de acordo com a opcao escolhida
        limpar_terminal()
        logo_pequena()
        print(textos[opc-1])
        
        # caso a opcao seja buscar por tipo o usuario deve escolher entre filme e serie
        if(opc == 5):
            print("1. Filme")
            print("2. Serie")
            
            # verifica se a opcao digitada é um numero
            try:
                opc = int(input("Digite o tipo: "))
            except:
                print("Opcao invalida")
                input()
                #limpar_terminal()
                return
            # Atribui o tipo de busca de acordo com a opcao escolhida
            if opc == 1:
                busca = "filme"
            elif opc == 2:
                busca = "serie"
            else:
                print("Opcao invalida")
                input()
                limpar_terminal()
                return
        else: # se a opcao nao for buscar por tipo o usuario deve digitar o termo de busca
            busca = input(f"Digite o {tipo[opc-1]}: ")
        return busca

def limpar_terminal():
    ''' Limpa o terminal de acordo com o sistema operacional '''
    sistema_operacional = os.name

    if sistema_operacional == 'posix':  # Linux ou macOS
        os.system('clear')
    elif sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:
        print()


def print_media(list):
    ''' Imprime os items da lista recebida e retorna uma lista com os seus ids'''
    
    ids = []
    for i in list:
        print(f'{i["id"]} - \t{i["title_ptBR"]} ({i["original_title"]})')
        if i["type"] == "filme": # se for um filme
            print("\t   - Filme")
            print(f'\t   - Ano: {i["year"]}\n\t   - Duracao{i["duration"]} min')
        else: # se for uma serie
            print("\t   - Serie")
            print(f'\t   - Lancamento: {i["premiered"].split("-")[0]}\n\t   - {i["seasons"]} temporadas')
        ids.append(str(i["id"]))
    return ids

def logo_grande():
    ''' Imprime o logo do CiCflix grande'''
    print("\n")
    print('  ,ad8888ba,   88    ,ad8888ba,      ad88  88  88')
    print(' d8\'     `"8b  88   d8"\'    `"8b    d8"    88  "" ')
    print('d8\'            88  d8\'              88            8b,     ,d8')
    print('88             88  88             MM88MMM  88  88  `Y8, ,8P\'')
    print('88             88  88               88     88  88    )888(')
    print('Y8,            88  Y8,              88     88  88   ,d8 8b,')
    print(' Y8a.    .a8P  88   Y8a.    .a8P    88     88  88   ,d8" "8b,')
    print('  `"Y8888Y\'    88    `"Y8888Y"\'     88     88  88  8P\'     `Y8')
    print()

def logo_pequena():
    ''' Imprime o logo do CiCflix pequena '''
    print("\n")
    print("\t\t   ___ ___  ___    __ _ _ ")
    print("\t\t  / __|_ _|/ __|  / _| (_)_ __")
    print("\t\t | (__ | |  (__  |  _| | \\ \\ /")
    print("\t\t  \\___|___|\\___| |_| |_|_/_\_\\")
    print()
    
if __name__ == "__main__":
    main()