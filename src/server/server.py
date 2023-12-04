import socket
from CiCflix import searchFiles, searchFile
import json

#Criar o socket TCP/IP
host = '127.0.0.1'
port = 12345
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((host, port))


# Colocar o socket para escutar conexões
servidor_socket.listen()

# loop enquanto o servidor estiver rodando
while(1):
    # Aceitar conexão
    client_connection, client_address = servidor_socket.accept()
    print("Conectado com: ", client_address)


    # Recebe stream de solicitação do cliente
    stream = client_connection.recv(1024).decode().split("---")
    
    if(stream[0] == "search"): # Se for uma solicitação de busca
        search = stream[1]
        type = stream[2]
        
        # list com os dados buscados por uma categoria 'type' com o termo 'search'
        list = []
        list = searchFiles(search, type)
        json_data = json.dumps(list) # transforma a lista em um json
        
        # Envia o tamanho dos dados
        print("Enviando tamanho dos dados")
        data_size = len(json_data)
        client_connection.send(str(data_size).encode())

        # Aguarda retorno do cliente para envio dos dados
        print("Aguardando retorno do cliente para envio dos dados")
        client_connection.recv(1024)
        
        # Envia os dados em partes
        for i in range(0, data_size, 1024):
            part = json_data[i:i+1024]
            client_connection.send(part.encode())
        
        # Aguarda confirmação de que os dados foram recebidos
        if(client_connection.recv(1024).decode() == "DONE"):
            print("Dados enviados")
        else:
            print("Erro ao enviar dados")

        print("Fechando conexao com ", client_address)
        client_connection.close() # fecha a conexão
        
    elif(stream[0] == "stream"): # se for uma solicitaçao de stream
        # procura o arquivo com o id passado
        id = stream[1]
        data = searchFile(id)
        
        # envia o tamanho do arquivo
        data_size = len(data)
        client_connection.send(str(data_size).encode())
        print("Enviando tamanho dos dados")
        
        # Aguarda retorno do cliente para envio dos dados
        print("Aguardando retorno do cliente para envio dos dados")
        client_connection.recv(1024)
        
        # Envia os dados em partes
        for i in range(0, len(data), 1024):
            part = data[i:i+1024]
            client_connection.send(part.encode())
        
        if(client_connection.recv(1024).decode() == "DONE"):
            print("Dados enviados")
        else:
            print("Erro ao enviar dados")
        
        # fecha a conexão com o cliente
        print("Fechando conexao com ", client_address)
        client_connection.close()
        
    elif(stream[0] == "end"): # se for uma solicitação de encerramento
        print(f"Fechando conexao com {client_address}")
        client_connection.close()
        print("Fechando socket do servidor")
        servidor_socket.close()
        break
    else: # se for um stream desconhecido
        print("Erro: Comando desconhecido")
        print("Fechando conexao com ", client_address)
        client_connection.close()