import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

# SOCK_STREAM is a tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# setting server to be non blocking
# server_socket.setblocking(False)
# this happens because the server is not able to accept the connection and the client is not able to connect to the server and the queue becomes empty

# 1-> on and 0-> off
# port 0 to 123 are used by system os
# Binding the server to the host and port

server_socket.bind((SERVER_HOST, SERVER_PORT))
# listening to the client. 5 is the maximum number of connections that can be in the queue
# if the 6th connection comes it will be refused or accepted based on the server

server_socket.listen(5)

print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")

# connections are getting piled up in a queue. So lets take the front element from the queue using server_socket.accept()

# Receiving multiple requests from the client
while True:
    client_socket, client_address = server_socket.accept()
    # client_socket is the socket object that is used to communicate with the client
    
    request = client_socket.recv(1500).decode()
    # 1500 is the buffer size for handling the maximum amount of data that can be received in bytes
    print(request)    
    # Getting all headers
    headers = request.split("\n")
    header_components = headers[0].split()

    # Method and path
    http_method = header_components[0]
    path = header_components[1]
    # Returning the path specific content
    # we have the method and path we can change the content based on the path
    if http_method == 'GET':
        if path == '/':
            file_input = open("index.html")
            body = file_input.read()
            file_input.close()
            # Returning the response of the https request.

            """
            Structure of HTTP 1.1 response - 
            STATUS LINE - HTTP version, status code, status message
            HEADERS - key value pair
            Message body - data
            """

            resp = 'HTTP/1.1 200 OK\n\n' + body
            # resp is a string but we need it in the format of readable buffer
            # send function could hv been used but there is no guarantee that it will send all the data whenever the network is busy or any other reason
        elif path == '/time':
            resp = 'HTTP/1.1 200 OK\n\n' + time.ctime()
    else:
        resp = 'HTTP/1.1 405 Method Not Allowed\n\nAllow GET, POST'
    client_socket.sendall(resp.encode())
    client_socket.close()