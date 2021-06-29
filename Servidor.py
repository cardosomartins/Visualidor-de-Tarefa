import socket

from threading import *
import time


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

            self.sock.send(b'MENSAGEM RECEBIDA')

            print('Client sent:', mensagem)

            if mensagem == 'Nicolas,Labview,1':
                start_time_nicolas = time.time()
                print('Temporizador de Nicolas começou')            

            if mensagem == 'Nicolas,Labview,0':
                end_time_nicolas = time.time()
                arquivo = open('arq.txt','w')
                arquivo.write(mensagem)
                arquivo.write('\t')
                time_lapsed_nicolas = end_time_nicolas - start_time_nicolas
                tempo_convertido_nicolas = time_convert(time_lapsed_nicolas)
                arquivo.write(tempo_convertido_nicolas)
                print('Temporizador de Nicolas terminou')
                arquivo.close()
    
    
def time_convert(sec):

     mins = sec // 60     
     sec = sec % 60  
     hours = mins // 60 
     mins = mins % 60
     mins = int(mins)
     sec = int(sec)
     hours = int(hours)
     mins = str(mins)
     sec = str(sec)
     hours = str(hours)        
     tempo_convertido = hours+"horas:  "+mins+"minutos:  "+sec+"segundos"

     return tempo_convertido
            
serversocket.listen(5)
print ('Servidor conectado e rodando')

while 1:

    clientsocket, address = serversocket.accept()

    client(clientsocket, address)
    


        