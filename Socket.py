import const
import socket

#IP localhost per default: 127.0.0.1
#If you want a remote connection you can see more information below:
#http://www.mon-ip.com/adresse-ip-locale.php

clients = []

def connectAs(type):
    if type is const.TYPE_SERVER:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if const.SERVER_IP.lower() == 'default':
            s.bind((socket.gethostname(), const.PORT))
            ip = socket.gethostname()
        else:
            s.bind((const.SERVER_IP, const.PORT))
            ip = const.SERVER_IP
        s.listen(5)
        if s is False:
            print(const.WARNING_ERROR + 'The server doesnt respond')
        else:
            print(const.SUCCESS_GREEN + '[*] You are now connected on the Server... (Waiting for client)')
            print(const.SUCCESS_GREEN + 'You listening to: ' + str(ip) + ':' + str(const.PORT))
            checkClient(s)
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if const.SERVER_IP.lower() == 'default':
            s.connect((socket.gethostname(), const.PORT))
        else:
            s.connect((const.SERVER_IP, const.PORT))
        return s

def insertNewClient(client):
    i = 0
    #for i in range(10): bad idea if you do not have much clients
    while True:
        i+=1
        if len(clients) < i:
            clients.insert(i, client)
            break

def totalOfClients():
    return clients.__len__()

def checkClient(socket):
    client, addr = socket.accept()
    print(const.SUCCESS_GREEN + 'New Client: ' + format(addr) + ' now connected.')
    insertNewClient(client)
    print(const.SUCCESS_GREEN + 'you have a total of ' + str(totalOfClients()) + ' clients')

    if client is False:
        print(const.WARNING_ERROR + 'Client: ' + format(client) + ' has been disconnected.')
        closeClient(client)
    else:
        checkResponseFromClient(client)

def checkResponseFromClient(client):
    while True:
        data = client.recv(4096)
        if not data:
            closeClient(client)
            print(const.WARNING_ERROR + 'Client: ' + format(client) + ' has been disconnected.')
            break
        else:
            print(const.SUCCESS_GREEN + 'Client: ' + data.decode())

def sendFromClient(s, msg):
    s.send(msg.encode())

def closeClient(s):
    clients.remove(s)
    s.close()