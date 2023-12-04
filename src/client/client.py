import socket
import json

def createConection():
    ''' Cria uma conexão com o servidor com host e porta especificados e retorna o socket criado'''
    
    # variaveis de conexao
    host = "127.0.0.1"
    port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 4: Conectar
    client_socket.connect((host, port))
    return client_socket

def searchFile(search, type):
    connection = createConection() # Cria conexão com o servidor

    
    # Envia o tipo de operacao que ira ser realizada
    connection.send("search---".encode())
    
    # Envia os dados da busca
    connection.send(search.encode())
    connection.send("---".encode())
    connection.send(type.encode())
    
    
    list = []
    # Recebe o tamanho dos dados
    try:
        data_size = int(connection.recv(1024).decode())
    except:
        print("Erro ao receber tamanho dos dados")
        return list

    # Envia confirmação a servidor indicando que está pronto para receber os dados
    connection.send(b'OK')

    # Recebe os dados em partes e os concatena
    json_data = ''
    while len(json_data) < data_size:
        part = connection.recv(1024).decode()
        json_data += part
        
    # Envia confirmação a servidor indicando que os dados foram recebidos
    connection.send(b'DONE')
    
    # transforma os dados recebidos em uma lista
    list = json.loads(json_data)
    
    # Fecha a conexão com o servidor e retorna a lista de resultados
    return list

def streamFile(id):
    connection = createConection() # Cria conexão com o servidor
    
    # Envia o tipo de operacao que ira ser realizada
    connection.send("stream---".encode())
    
    # Envia id da midia
    connection.send(id.encode())
    
    # Recebe o tamanho dos dados e manda confirmação de que está pronto para receber
    size = int(connection.recv(1024).decode())
    connection.send(b'OK')
    
    # Recebe os dados em partes e assiste (imprime) eles
    stream_size = 0
    while stream_size < size:
        data = connection.recv(1024).decode()
        stream_size += len(data)
        print(data, end='')
        input()
        
def closeSocket():
    ''' Envia uma mensagem ao servidor para que ele feche o socket'''
    connection = createConection()
    connection.send("end---".encode())