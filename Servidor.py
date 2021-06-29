import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.6"
port = 8000
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            mensagem = self.sock.recv(1024).decode()
            self.sock.send(b'ACK')
            print('Client sent:', mensagem)
            arquivo = open('arq.txt','a')
            arquivo.write(mensagem)
            arquivo.close()

serversocket.listen(5)
print ('Servidor conectado e rodando')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
    


        