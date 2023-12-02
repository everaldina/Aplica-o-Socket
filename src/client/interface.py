import os

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
        
        if busca is not None:
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
                    
        
        
    
        
    
def menu(opc):
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
        busca = input("Digite o titulo: ")
        return busca

def limpar_terminal():
    sistema_operacional = os.name

    if sistema_operacional == 'posix':  # Linux ou macOS
        os.system('clear')
    elif sistema_operacional == 'nt':  # Windows
        os.system('cls')
    else:
        print()


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