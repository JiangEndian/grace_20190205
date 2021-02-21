import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    w = input('Please say:')
    socket_client.sendto(w.encode('utf-8'), ('127.0.0.1', 9999))
    if w == 'exit':
        break
    print(socket_client.recv(1024).decode('utf-8'))

socket_client.close()

