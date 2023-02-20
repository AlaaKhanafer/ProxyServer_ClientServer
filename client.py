import socket
import time
from datetime import datetime
#from getmac import get_mac_address as gma
import uuid

def timeT():
    time_now = datetime.now()
    return time_now.strftime("%H:%M:%S")

#Client Server
serverName = socket.gethostname()
serverPort = 12000

#Create a TCP client socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket: 
    client_socket.connect((serverName,serverPort))      #connect the client to the proxy server
    
    website = input('Please give the website you wish to access: ')
    
    startTime = time.time()  #start time
    client_socket.send(website.encode())        #send the request to the proxy server
    currentTime = timeT()
    print("Sending a request to the proxy server to get http webpage: ",website,"\t at exact time: ",currentTime)

    result = client_socket.recv(1024)       #receive the repply from the proxy server
    currentTime2 = timeT()
    print('\nReceived at: ',currentTime2,'\tfrom the server: ', result.decode())
    
    finishTime=time.time()
    RTT = finishTime - startTime
    print("\nRound Trip Time = ", RTT)
    #print("MAC Address: ",gma())
    
    myMac=uuid.getnode()        #get the mac address
    print("MAC Address: ", myMac) #or print("MAC Address: ", hex(myMac)) to get the mac address in hexadecimal form like the ipconfig shows it
    client_socket.close()