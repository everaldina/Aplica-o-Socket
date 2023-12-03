import socket
import json

def createConection(host, port):
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 4: Conectar
    cliente_socket.connect((host, port))
    return cliente_socket

def searchFile(search, type):
    s = createConection("127.0.0.1", 12345)

    list = []
    
    # Envia o tipo de operacao que ira ser realizada
    s.send("search".encode())
    
    # Envia os dados da busca
    s.send(search.encode())
    s.send(type.encode())
    
    # Recebe o tamanho dos dados
    data_size = int(s.recv(1024).decode())

    # Envia confirmação a servidor indicando que está pronto para receber os dados
    s.send(b'OK')

    # Recebe os dados em partes e os concatena
    json_data = ''
    while len(json_data) < data_size:
        part = s.recv(1024).decode()
        json_data += part

    # Desserializa os dados JSON para obter a lista original
    list = json.loads(json_data)

    # Envia os dados do arquivo
    #with open(nome_arquivo, 'rb') as arquivo:
    #    dados = arquivo.read(1024)
    #    while dados:
    #        s.send(dados)
    #        dados = arquivo.read(1024)

    s.close()
    return list