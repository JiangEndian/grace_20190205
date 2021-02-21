#!/usr/bin/env python3
import socket
import threading

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_server.bind(('127.0.0.1', 9876))

print('Bind UDP on 127.0.0.1:9876...')

def udp_receive(socket_server):
    while True:
        data, addr = socket_server.recvfrom(1024)
        key_pressed = data.decode('utf-8')
        #You can input your command in hear...
        #Or you can copy it to your source file.
        print(data.decode('utf-8'))

threading.Thread(target=udp_receive, args=(socket_server,)).start()

