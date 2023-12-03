import socket
from CiCflix import searchFile
import json

# 1: Criar o socket
host = '127.0.0.1'
porta = 12345
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((host, porta))


# 2: Escutar
servidor_socket.listen()

conexao, endereco_cliente = servidor_socket.accept()


# Recebe o nome do arquivo
operation = conexao.recv(1024).decode()

if(operation == "search"):
    list = []
    search = conexao.recv(1024).decode()
    type = conexao.recv(1024).decode()
    list = searchFile(search, type)
    json_data = json.dumps(list)
    
    # Envia o tamanho dos dados
    data_size = len(json_data)
    conexao.send(str(data_size).encode())

    # Aguarda retorno do cliente para envio dos dados
    conexao.recv(1024)  # Pode ser uma confirmação simples
    # Envia os dados em partes
    for i in range(0, json_data, 1024):
        part = json_data[i:i+1024]
        conexao.send(part.encode())
    
elif(operation == "stream"):
    print("stream")
    nome_arquivo = conexao.recv(1024).decode()
    print(nome_arquivo)
    

conexao.close()

# Abre o arquivo para escrita binária
#with open(nome_arquivo, 'wb') as arquivo:
#    while True:
#        dados = conexao.recv(1024)
#        if not dados:
#            break
#        arquivo.write(dados)
