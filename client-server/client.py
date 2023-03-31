import socket

def main():
    server_ip = input("Enter server IP address: ")
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message == 'exit':
            break

        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received from server: {data}")

    client_socket.close()

if __name__ == "__main__":
    main()