import socket

from threading import *
import time
import fileinput


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

            self.sock.send(b'MENSAGEM RECEBIDA PELO SERVIDOR')

            print('Client sent:\n', mensagem)

            arquivo = "arq.txt"

            contador = -1
            contador_auxiliar = -1
        ## FALTA CONVERTER A MENSAGEM EM UM BOOLEANO E DEIXAR SÓ A MENSAGEM 
            with fileinput.FileInput(arquivo, inplace = True, backup ='.bak') as f:
                for line in arquivo:
                    contador += 1
                    if mensagem == line:
                        start_time = time.time()
                    if mensagem == line:
                        end_time = time.time()
                        time_lapsed = end_time - start_time
                        numero_linha = i
                        if i == numero_linha+2 in arquivo:
                            tempo_anterior = int(line)
                            tempo_novo = int(tempo_anterior + time_lapsed)
                            print(line.replace(tempo_anterior, tempo_novo), end='')
                        if i == numero_linha+1 in arquivo:
                            tempo_convertido_anterior = line    
                            tempo_convertido_novo = time_convert(tempo_novo)
                            print(line.replace(tempo_convertido_anterior, tempo_convertido_novo))
                contador = -1
                contador_auxiliar = -1
        


                                   

            if mensagem == 'Nicolas,Labview,1':
                start_time_nicolas = time.time()
                print('Temporizador de Nicolas começou')            

            if mensagem == 'Nicolas,Labview,0':
                end_time_nicolas = time.time()
                arquivo = open('arq.txt','a')
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
     tempo_convertido = hours+"h:"+mins+"m:"+sec+"s"

     return tempo_convertido
            
serversocket.listen(5)
print ('Servidor conectado e rodando')

while 1:

    clientsocket, address = serversocket.accept()

    client(clientsocket, address)  