import socket

def start_server(host='0.0.0.0', port=6790):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}...")
        
        while True:
            connection, address = server_socket.accept()
            with connection:
                print(f"Connected by {address}")
                message = connection.recv(1024).decode('utf-8')
                print(f"Message received: {message}")
                connection.sendall("Got it!".encode('utf-8'))

if __name__ == "__main__":
    start_server()
