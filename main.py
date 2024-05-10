import socket
import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

# SOCK_STREAM is a tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# port 0 to 123 are used by system os
server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(request)    
    headers = request.split("\n")
    header_components = headers[0].split()

    http_method = header_components[0]
    path = header_components[1]

    if path == '/':
        file_input = open("index.html")
        body = file_input.read()
        file_input.close()

        resp = 'HTTP/1.1 200 OK\n\n' + body
        # resp is a string but we neet it in the format of readable buffer
        # send function could hv been used but there is no guarantee that it will send all the data whenever the network is busy or any other reason
        client_socket.sendall(resp.encode())