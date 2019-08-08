#!/usr/local/bin/python3
import socket
from time import ctime
def tcpCreate():
    #HOSTIPV6='::1'
    HOST=''
    PORT=12345
    BUFSIZ=1024
    ADDR=(HOST,PORT)
    #创建tcp套接字
    tcpSerSock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    print('listening....')
    tcpSerSock.listen(5)
    
    while True:
        print('waiting for connection...')
        tcpCliSock,addr=tcpSerSock.accept()
        print('...connected from:', addr)

        while True:
            data=tcpCliSock.recv(BUFSIZ)
            data.decode()
            if not data:
                break
            tcpCliSock.send('[%s] %s'.encode('utf-8') %(bytes(ctime(), 'utf-8'), data))
        tcpCliSock.close
    tcpSerSock.close

def udpCreate():
    HOST=''
    PORT=12345
    BUFSIZ=1024
    ADDR=(HOST,PORT)
    #创建udp套接字
    udpSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSock.bind(ADDR)

    while True:
        print('waiting for message...')
        data,addr=udpSock.recvfrom(BUFSIZ)
        udpSock.sendto('[%s] %s'.encode('utf-8') % (bytes(ctime(), 'utf-8'),data), addr)
        print('...received form and retuned to:', addr)
    udpSock.close()



if __name__ == '__main__':
    #tcpCreate()
    udpCreate()
