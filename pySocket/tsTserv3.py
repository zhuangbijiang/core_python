#!/usr/bin/env python3
# encoding: utf-8

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock= socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZE).decode()
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode())
    tcpCliSock.close()
tcpSerSock.close()
