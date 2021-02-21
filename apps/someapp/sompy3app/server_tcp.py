import socket
import threading

socket4server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket4server.bind(('127.0.0.1', 9999))

socket4server.listen(3)

print('Server is start...\n')

def tcplink(sock, addr):    #写定义后用
    print('Accept new connection from %s:%s.' % addr)
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8')=='exit':
            break
        print(data.decode('utf-8'))
        sock.send(('server_recved:%s' % data.decode('utf-8')).encode('utf-8'))
    print('Connection end... %s:%s.' % addr)
    sock.close()

while True:
    sock, addr = socket4server.accept()
    doit = threading.Thread(target=tcplink, args=(sock, addr))
    doit.start()
