import Socket
import const

while True:
    type = input(const.SUCCESS_GREEN + 'Type of connection: ')
    if type == "":
        print(const.WARNING_ERROR + 'You have two type of connection: Client, Server')
    elif type.lower() == 'server':
        Socket.connectAs(const.TYPE_SERVER)
    elif type.lower() == 'client':
        s = Socket.connectAs(const.TYPE_CLIENT)
        check = input(const.SUCCESS_GREEN + 'Please tap Y for send a message or E for exit: ')
        if check.lower() == 'y':
            while True:
                send = input('CLIENT: ')
                if send is not "":
                    Socket.sendFromClient(s, send)
                elif send.lower() == 'exit':
                    print(const.SUCCESS_GREEN + 'You quit the server.')
                    Socket.closeClient(s)
                    break
        else:
            print(const.SUCCESS_GREEN + 'You quit the server.')
            Socket.closeClient(s)
            break