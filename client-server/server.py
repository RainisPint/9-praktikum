import socket

def main():
    host = '0.0.0.0'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"[+] Connection from {address}")

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Received message: {data}")
            client_socket.send(("You said: " + data).encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    main()