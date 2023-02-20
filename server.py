import socket
from datetime import datetime
import requests as req

#Proxy Server
serverPort = 12000 #assigning port to be listened to
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('',serverPort))
    server_socket.listen(1)
    
    def time():
        time_now = datetime.now()
        return time_now.strftime("%H:%M:%S")
    
    print(f"Proxy Server is listening on {serverPort}")
    
    while True:
        
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]} at {time()}")

        # Receive the request of the client
        request = client_socket.recv(1024).decode()
        # we can also creste a destination socket here to send to it the request and receive it
        # Send the client's request to the destination server
        request_2 = "http://" + request
        current_time = time()
        
        # Parse the request to get the destination server IP address
        try:
            webIP=socket.gethostbyname(request)
        except:
            print("Cannot get the ip address of the website")
            client_socket.send("Cannot get the ip address of the website".encode())
        
        
        print("Accessing the webpage of IP: ",webIP,", exact time of the request is: ",current_time)
    
        print("Exact time of the http request: ",time())
        
        # Receive the response from the destination server
        resp = req.get(request_2)
        print("Exact time of the receiving response: ",time())

        # Send the response back to the client
        client_socket.send(resp.text.encode())
        print("Response was sent to the client at: ",time())
        

        # Close the socket
        client_socket.close()
