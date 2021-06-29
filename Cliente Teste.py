import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.0.6"
port =8000
s.connect((host,port))

def ts(str,r):
   s.send(r.encode()) 
   data = ''
   data = s.recv(1024).decode()
   print (data)
while 1:
   r = input('Insira a mensagem que você gostaria de enviar: ')
   ts(s,r)
   

s.close ()