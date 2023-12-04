import os

def create_folders_and_files(ini, fim, x, max_bytes):
    ''' 
        Cria (fim - ini + 1) arquvios com nomes de ini a fim. 
        Cada arquivo se chama file.txt, e esta dentro de uma pasta com nome de ini a fim.
        Cada arquivo tem max_bytes.
    '''
    
    path = 'src/server/data'  # especifica o caminho onde as pastas e arquivos serão criados
    
    # cria as pastas e arquivos
    for i in range(ini, fim+1):
        folder_name = str(i) # nome da pasta
        os.makedirs(os.path.join(path, folder_name), exist_ok=True) # cria a pasta
        file_path = os.path.join(path, folder_name, 'file.txt') # caminho do arquivo

        # cria o arquivo com o tamanho especificado
        with open(file_path, 'wb') as file:
            data = (str(i) * x).encode()
            while file.tell() < max_bytes:
                file.write(data)

# cria 15 arquivos dentro de pastas com nomes de 1 a 15, cada arquivo tem 5000 bytes
create_folders_and_files(1, 15, 10, 5000)
# cria 6 arquivos dentro de pastas com nomes de 16 a 22, cada arquivo tem 10000 bytes
create_folders_and_files(16, 22, 10, 10000)
