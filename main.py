

import socket
import threading



choice = input("Serveur(1) ou client (2):")
if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.0.223", 9999))
    server.listen()
    
    client, _ = server.accept()

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.0.223", 9999))

else:
    exit()
    

def sending_messages(c):
    while True:
        message = input("")
        c.send(message.encode())
        print("Votre_Message: " + message)

def receiving_messages(c):
    while True:
        print("Message_Reçu: " + c.recv(1024).decode())


threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()
        
        