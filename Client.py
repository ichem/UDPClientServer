from datetime import datetime
from socket import *
from time import time

def main():

    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    counter = 10
    i = 0
    #print ('Now attempting ', counter, 'pings')
    while i < counter:
        i+= 1
        print 'Ping Attempt: ', i
        start = datetime.now()
        clientSocket.sendto(b'Ping '+str(i)+' '+str(start),(serverName,serverPort))
        clientSocket.settimeout(1)
        try:
            modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
            current = datetime.now()
            c = start-current
            print (modifiedMessage)
           # print 'elapsed time in microseconds is ',c.microseconds
        except timeout:
            print ('Request timed out. ')
        if i == 10:
            print ('Bye!')
    clientSocket.close()
    print ('Socket has been closed! No more pings!')
    pass

main()
