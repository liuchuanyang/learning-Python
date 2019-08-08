#!/usr/local/bin/python3

import socket 

def tcpCreate():
    HOST=''
    PORT=12346
    SERV_PORT=12345
    ADDR=(HOST, PORT)
    BUFSIZE=1024
    tcpSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #tcpSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #tcpSock.bind(ADDR)
    tcpSock.connect((HOST, SERV_PORT))

    while True:
        '''
        mystr=input('请输入字符串，\\n代表退出循环')
        if mystr == '\n'
            break
         '''
        data = input('> ')
        #print(type(data))
        if not data:
            break
       
        #tcpSock.send(data.encode('utf-8'))
        tcpSock.send(data.encode('utf-8'))
        data=tcpSock.recv(BUFSIZE)
        #print(type(data))
        if not data:
            break
        print(data.decode('utf-8'))
    tcpSock.close()
def updCreate():
    BUFFIZE=1024
    udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data = input('> ')
        if not data:
            break
        udpSock.sendto(data.encode(), ('', 12345))
        data, addr = udpSock.recvfrom(BUFFIZE)
        print(data.decode('utf-8'))
if __name__ == '__main__':
    #tcpCreate()
    updCreate()

