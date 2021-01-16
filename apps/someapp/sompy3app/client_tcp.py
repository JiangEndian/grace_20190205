import socket

socket4client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket4client.connect(('127.0.0.1', 9999))

socket4client.send(b'Hello.')
print(socket4client.recv(1024).decode('utf-8'))

while True:
    w = input('Please say:')
    socket4client.send(w.encode('utf-8'))
    if w == 'exit':
        break
    print(socket4client.recv(1024).decode('utf-8'))

socket4client.close()
