#!/usr/bin/env python3
import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_server.bind(('127.0.0.1', 9876))

print('Bind UDP on 9876...')

while True:
    data, addr = socket_server.recvfrom(1024)
    print(data.decode('utf-8'))
    #print('Received %s from %s:%s.' % (data.decode('utf-8'), addr[0], addr[1]))
    #socket_server.sendto(b'recved:' +data, addr)

