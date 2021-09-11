#!/usr/bin/env python3

import socket, time, sys, threading

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
print('%s(localhost) IP:%s' % (socket.gethostname(), get_ip()))

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

def udpServer():
    DeviceList = set([])
    oldDeviceList = set([])
    
    while True:
        data, addr = socket_client.recvfrom(1024) #接收
        #print(data.decode('utf-8'), addr)
    
        if addr[0]: #判断新设备地址并打印
            msg = data.decode('utf-8')
            ip = addr[0]
            port = addr[1]

            hostIp = msg + ':' + ip
            DeviceList.add(hostIp)
            #print(DeviceList, oldDeviceList)
            #print('There is a new device: %s' % addr[0])
        
            if not DeviceList == oldDeviceList:
                print('\ndevice list changed:')
                #print(DeviceList)
                for device in DeviceList:
                    print(device)
                oldDeviceList.add(hostIp)
t = threading.Thread(target=udpServer)
t.start()
#t.join() #这个是等着运行完的。就ctrl+c结束吧

while True:
    #w = input('Please say:')
    w = socket.gethostname()
    socket_client.sendto(w.encode('utf-8'), Address) #发送

    time.sleep(1) #扫描频率


socket_client.close()

