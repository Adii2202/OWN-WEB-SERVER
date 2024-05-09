import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

# SOCK_STREAM is a tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# port 0 to 123 are used by system os
server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Listening on {SERVER_HOST}:{SERVER_PORT}")