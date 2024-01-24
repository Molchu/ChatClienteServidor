import threading
import socket

#Valores de conexión
host = "127.0.0.1" #localhost
port = 55555

#Se inicializa el socket con ipv4 y TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Se dan los parametros de host y puerto y ubicamos modo escucha
server.bind((host, port))
server.listen()

#Lista de clentes y nombres
clients = []
nicknames = []

#Se envia mensaje a todos los usuarios conectados
def broadcast(message):
    for client in clients:
        client.send(message)

#Administran mensajes de los clientes
def handle(client):
    while True:
        try:
            #Mensaje
            message = client.recv(1024)
            #posicion del cliente en la lista clientes
            index = clients.index(client)
            #msn es el mensaje decodificado incluido el nombre
            msn = message.decode('ascii')
            #Tamanio nombre del cliente que envia el mensaje
            tam = int(len(nicknames[index]))
            fl = msn[tam+2] #Primer caracter del mensaje
            #name almacena el nombre del usuario al que se desea enviawr el mensaje
            name = ''
            #Si el primer caracter enviado es un @, entonces se lee el caracter despues de este y antes de recibir un espacio
            if fl == '@':
                i = msn[tam+3]
                c = 0
                #Itera en el mensaje almacenando cada unidad del string y guarda el nombre destino en name
                while i != ' ':
                    name = name + i
                    c += 1
                    i = msn[tam+3+c]
                    #Si el nombre esta en la lista nicknames, entonces se almacena su posicion y se ubica el cliente respectivo
                if name in nicknames:
                    pos = nicknames.index(name)
                    clients[int(pos)].send(message)
                else:
                    #De no cumplirse lo anterior, se envia mensaje de advertencia
                    print("No existe un usuario con ese nombre")
            else:
                #Mensaje al cchat global
                broadcast(message)
        except:
            #Se cierra el cliente y se envia mensaje de "Cliente ha salido"
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        #Se aceptan conexiones y se imprime la información
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to server'.encode('ascii'))
        #Se inician los hillos
        thread = threading.Thread(target = handle, args = (client,))
        thread.start()

print('Waiting')
receive()