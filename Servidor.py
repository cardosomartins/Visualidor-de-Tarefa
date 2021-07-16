import socket

from threading import *
import time
import fileinput


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.0.15"

port = 8000

print('IP do host:')
print (host)
print('Porta do host:')
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

            mensagem = self.sock.recv(1024).decode().split('\n')   #AQUI SE DIVIDE A MENSAGEM RECEBIDA EM DOIS
        
            self.sock.send(b'MENSAGEM RECEBIDA PELO SERVIDOR')

            print('Client sent:')
            print(mensagem[0])
            print(mensagem[1])
            print(mensagem[2])

    ###########################################
            arquivo = "VISUALIZADOR DE TAREFAS"

            contador_linha = -1
            booleano = 3
            numero_linha = -5
            cond_nova_escrita = -3
            time_lapsed = 0
            
        ## FALTA CONVERTER A MENSAGEM EM UM BOOLEANO E DEIXAR SÓ A MENSAGEM 
            arquivo = open('VISUALIZADOR_DE_TAREFAS.txt', 'rt')
            data = arquivo.readlines()
            
            for line in data:
                    booleano = int(mensagem[1])
                    contador_linha = contador_linha + 1
                    if (((mensagem[0]+'\n') == line) and booleano == 1): ##ATENTAR AO BOOLEANO SER INT
                        start_time = time.time()
                        print("TESTE AMENDOIM 1")
                        cond_nova_escrita = 0
                    if (((mensagem[0]+'\n') == line) and booleano == 0):
                        end_time = time.time()
                        time_lapsed = end_time - start_time
                        numero_linha = contador_linha
                        print('TESTE AMENDOIM 2')
                        cond_nova_escrita = 0
                    if (contador_linha == (numero_linha+1)):
                            tempo_anterior = line
                            tempo_novo = int(int(tempo_anterior) + int(time_lapsed))
                            print(line.replace(tempo_anterior, str(tempo_novo)), end='')
                            cond_nova_escrita = 0
                            arquivo.close()
                            arquivo = open('VISUALIZADOR_DE_TAREFAS.txt', 'wt')
                            arquivo.write(str(data))
                            arquivo.close()
                            print('HOUVE OVERWRITE NO ARQUIVO TXT')
                            
            arquivo.close()                
                 ################
            if cond_nova_escrita != 0:
                arquivo = open('VISUALIZADOR_DE_TAREFAS.txt','a+')
                arquivo.write(mensagem[0] + '\n') 
                arquivo.write(mensagem[1] + '\n')
                arquivo.write(mensagem[2] + '\n')              
                arquivo.close()
                start_time = 0
                print("ESCREVERAM-SE NOVOS DADOS NO ARQUIVO TXT")


            cond_nova_escrita = -3            
            contador_linha = -1
            booleano = 3
            numero_linha = -1
            


            ###############################

            if mensagem == 'Nicolas,Labview,1':
                start_time_nicolas = time.time()
                print('Temporizador de Nicolas começou')            

            if mensagem == 'Nicolas,Labview,0':
                end_time_nicolas = time.time()
                arquivo = open('VISUALIZADOR_DE_TAREFAS.txt','w')
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
print ('Conexão do Servidor estabelecida e disponível para receber mensagens!')

while 1:

    clientsocket, address = serversocket.accept()

    client(clientsocket, address)  


    
            