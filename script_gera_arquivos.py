import os

def create_folders_and_files(ini, fim, x, max_bytes):
    path = 'src/server/data'  # Specify the path to the folder where files will be created
    for i in range(ini, fim+1):
        folder_name = str(i)
        os.makedirs(os.path.join(path, folder_name), exist_ok=True)
        file_path = os.path.join(path, folder_name, 'file.txt')
        with open(file_path, 'wb') as file:
            data = (str(i) * x).encode()
            while file.tell() < max_bytes:
                file.write(data)

# Example usage
create_folders_and_files(1, 15, 10, 5000)
create_folders_and_files(16, 22, 10, 100000)
