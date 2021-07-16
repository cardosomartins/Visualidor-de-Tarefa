Trabalho Renan Nunes e Cardoso Martins:
_______________________________________
Sumário:
Este programa tem como o propósito de registrar a quantia de tempo destinadas
a determinada atividade por certo indivíduo.
Existem duas interfaces, a do servidor e a do cliente.
_______________________________________
Requisitos:
1. Instalar pyqt5 e tkinter
2. Verificar se a porta escolhida para a tranmissão está aberta.
3. Deve-se assegurar que não há arquivo .txt com o nome de "VISUALIZADOR DE TAREFAS"
no diretório onde o Python salva os arquivos.
4. O "Servidor.py" deve ser ligado ANTES do "Cliente.py".

_______________________________________
Instruções de uso(CLIENTES):

0. Configurar a opção "host" com o IP do computador utilizado e "port" com uma
possível porta de envio/recebimento de dados.
1. Para início do registro de tempo, digitar o nome e a atividade na caixa de diálogo,
caso seja este o INÍCIO da atividade, selecionar a opção "1".
Caso se esteja terminando o tempo destinado a atividade, selecionar "0".
2. O programa não contém limitações quanto a quantia de atividades e quantia de 
pessoas, no entanto, deve-se observar que só se pode realizar UMA atividade por vez.
Caso, queira-se iniciar outra atividade, deve-se finalizar a antiga com o 
procedimento acima descrito.
3. A interface demonstrando o tempo de trabalho de cada pessoa só aparece quando
a conexão com o SERVIDOR é realizada.
4. Para que seja atualizado essa interface, é necessário fechar o programa do
servidor e executá-lo novamente.

_______________________________________
Instruções de uso(SERVIDOR):

0. Configurar a opção "host" com o IP do computador utilizado e "port" com uma
possível porta de envio/recebimento de dados.
1. A interface do servidor mostra quanto tempo a pessoa destinou a determinada 
atividade.
2. A parte do status indica a última seleção que o CLIENTE fez. Caso esteja 1,
o cliente está trabalhando na atividade nesse momento. Caso esteja 0, já finalizou.

_______________________________________


Restrições:

A. O programa só permite a contabiliadde de UMA atividade por vez.


