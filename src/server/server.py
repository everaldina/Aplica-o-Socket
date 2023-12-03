import socket
from CiCflix import searchFiles, searchFile
import json

# 1: Criar o socket
host = '127.0.0.1'
porta = 12345
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((host, porta))


# 2: Escutar
servidor_socket.listen()

while(1):
    conexao, endereco_cliente = servidor_socket.accept()
    print("Conectado com: ", endereco_cliente)


    # Recebe o nome do arquivo
    stream = conexao.recv(1024).decode().split("---")
    if(stream[0] == "search"):
        list = []
        search = stream[1]
        type = stream[2]
        list = searchFiles(search, type)
        json_data = json.dumps(list)
        
        # Envia o tamanho dos dados
        data_size = len(json_data)
        conexao.send(str(data_size).encode())

        # Aguarda retorno do cliente para envio dos dados
        conexao.recv(1024)  # Pode ser uma confirmação simples
        # Envia os dados em partes
        for i in range(0, data_size, 1024):
            part = json_data[i:i+1024]
            conexao.send(part.encode())
        conexao.close()
        
    elif(stream[0] == "stream"):
        id = stream[1]
        data = searchFile(id)
        conexao.send(str(len(data)).encode())
        conexao.recv(1024)
        
        for i in range(0, len(data), 1024):
            part = data[i:i+1024]
            conexao.send(part.encode())
            
        conexao.close()
        servidor_socket.close()
    else:
        conexao.send("ERRO".encode())
        conexao.close()
        servidor_socket.close()

    # Abre o arquivo para escrita binária
    #with open(nome_arquivo, 'wb') as arquivo:
    #    while True:
    #        dados = conexao.recv(1024)
    #        if not dados:
    #            break
    #        arquivo.write(dados)