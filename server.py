import socket
import sys
import json


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('Iniciando em {} porta {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)

while True:
    
    print('Aguardando uma conexão...')
    connection, client_address = sock.accept()
    try:
        print('conexão de', client_address)

        
        while True:
            data = connection.recv(1024).decode()
            
            if data:
                print('JSON recebido com sucesso')
                json_data = json.loads(data)
                
               
                print(type(json_data))
                print(json.dumps(json_data, indent=4, sort_keys=False))
                
            else:
                print('Nenhum arquivo chegou de', client_address)
                break

    finally:
        connection.close()