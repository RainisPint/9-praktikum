import socket
import threading
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 12345
server.bind((host, port))
server.listen()

clients = []
usernames = []


def broadcast(message, sender_client):
    for client in clients:
        if client != sender_client:
            client.send(message)


def private_message(message, recipient, sender_client):
    for client, username in zip(clients, usernames):
        if username == recipient:
            client.send(f"Private message from {usernames[clients.index(sender_client)]}: {message}".encode("utf-8"))
            break


def broadcast_with_username(message, sender_client):
    broadcast(f"{usernames[clients.index(sender_client)]}: {message}".encode("utf-8"), sender_client)


def handle_message(message, client):
    if message.startswith("PRIVATE "):
        recipient, private_msg = message[8:].split(" ", 1)
        private_message(private_msg, recipient, client)
    else:
        broadcast_with_username(message, client)


def handle(client):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            handle_message(message, client)
        except (socket.error, UnicodeDecodeError):
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            usernames.remove(username)
            print(f"{username} left the server.")
            broadcast(f"{username} left the chat.".encode("utf-8"), client)
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
        broadcast(f"{username} joined the chat.".encode("utf-8"), client)
        client.send("Connected to the server.".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

def main():
    print("Server is listening...")
    receive()


if __name__ == '__main__':
    main()
