import socket
import threading

nickname = input("Choose a nickname: ")

#Inicializa el socket, direccion y puerto
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

#Recibe información
def receive():
    while True:
        try:
            #Recibe mensajes de un cliente y lo decodifica mediante protocolo ascii
            message = client.recv(1024).decode('ascii')
            #Se envia el nickname
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            #Posible error y cierra conexión
            print("An error ocurred")
            client.close()
            break

#Cliente escribe
def write():
    while True:
        #Envia nick y mensaje
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

#Hilos
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()