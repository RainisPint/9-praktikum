import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 12345
server.bind((host, port))
server.listen()

clients = []
usernames = []


def main():
    def broadcast(message):
        for client in clients:
            client.send(message)

    def handle(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message)
            except:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                username = usernames[index]
                usernames.remove(username)
                broadcast(f"{username} left the chat.".encode("utf-8"))
                break

    def receive():
        while True:
            client, address = server.accept()
            print(f"Connected with {str(address)}")

            client.send("USER".encode("utf-8"))
            username = client.recv(1024).decode("utf-8")
            usernames.append(username)
            clients.append(client)

            print(f"Username is {username}")
            broadcast(f"{username} joined the chat.".encode("utf-8"))
            client.send("Connected to the server.".encode("utf-8"))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

    print("Server is listening...")
    receive()


if __name__ == "__main__":
    main()
