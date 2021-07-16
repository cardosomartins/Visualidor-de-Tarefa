import socket
import tkinter as tk
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
                        cond_nova_escrita = 0
                    if (((mensagem[0]+'\n') == line) and booleano == 0):
                        end_time = time.time()
                        time_lapsed = end_time - start_time
                        numero_linha = contador_linha
                        cond_nova_escrita = 0                        
                    if (contador_linha == (numero_linha+2)):
                            string_repor = line
                            tempo_anterior = line.split(':')                                                        
                            tempo_novo = int(3600*int(tempo_anterior[0]) + 60*int(tempo_anterior[1])+ int(tempo_anterior[2])+int(time_lapsed))
                            tempo_novo_convertido = time_convert(tempo_novo)                            
                            data[contador_linha]= time_convert(tempo_novo)
                            print(tempo_novo_convertido)                                                    
                            arquivo.close()
                            arquivo = open('VISUALIZADOR_DE_TAREFAS.txt', 'wt')
                            for line in data:
                                arquivo.write(line)
                            arquivo.close()
                            print('HOUVE OVERWRITE NO ARQUIVO TXT')
                            cond_nova_escrita = 0
                            
            arquivo.close()                
                 ################
            if cond_nova_escrita != 0:
                arquivo = open('VISUALIZADOR_DE_TAREFAS.txt','a+')
                arquivo.write('\n' + mensagem[0] + '\n') 
                arquivo.write(mensagem[1] + '\n')
                mensagem[2] = '00:00:00'
                arquivo.write(mensagem[2] + '\n')              
                arquivo.close()
                start_time = time.time()
                tempo_anterior = 0 
                print("ESCREVERAM-SE NOVOS DADOS NO ARQUIVO TXT")


            cond_nova_escrita = -3            
            contador_linha = -1
            booleano = 3
            numero_linha = -1
            


            ###############################
            
    
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
     tempo_convertido = hours+":"+mins+":"+sec

     return tempo_convertido


            
serversocket.listen(5)
print ('Conexão do Servidor estabelecida e disponível para receber/transmitir mensagens!')

while 1:
    
    def atualizar():
        arquivo = open('VISUALIZADOR_DE_TAREFAS.txt', 'r')
        CAIXINHA = arquivo.readlines()        
        arquivo.close()         
        return CAIXINHA

    CAIXINHA = atualizar()
    root = tk.Tk()
    w = tk.Label(root, text=CAIXINHA)
    w.pack()
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)        
    root.after(1, atualizar)   
    root.mainloop() 
    

    


    
    
    
    


    
            