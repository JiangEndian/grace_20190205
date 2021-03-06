#!/usr/bin/env python3

import socket
import time

#打印本机地址
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
print('本机IP:%s' % get_ip())

#一些设定。。。已经看不懂。。。但还好，在正常工作
Network = '<broadcast>'
Port = 9876
Address = (Network, Port)

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
socket_client.setblocking(1)
socket_client.settimeout(2)
socket_client.setblocking(1)
socket_client.bind(('', Port)) #绑定用以接收

#收集设备列表，不重复print
DeviceList = []

while True:
    #w = input('Please say:')
    w = 'Broadcast my IP address. '
    socket_client.sendto(w.encode('utf-8'), Address) #发送
    #if w == 'exit':
        #break
    data, addr = socket_client.recvfrom(65535) #接收
    #print('\nReceived reply: %s \n\tfrom %s:%s.' % (data.decode('utf-8'), addr[0], addr[1]))
    if not addr[0] in DeviceList: #判断新设备地址并打印
        DeviceList.append(addr[0])
        print('There is a new device: %s' % addr[0])

    time.sleep(3) #扫描频率

socket_client.close()

