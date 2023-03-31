import socket
import threading


def receive(client, username):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if message == "USER":
                client.send(username.encode("utf-8"))
            else:
                print(message)

        except (socket.error, KeyboardInterrupt, EOFError):
            print("\nConnection closed.")
            client.close()
            break


def write(client):
    while True:
        try:
            message = input()
            client.send(message.encode("utf-8"))

        except (socket.error, KeyboardInterrupt, EOFError):
            print("\nConnection closed.")
            client.close()
            break


def main():
    port = 12345
    while True:
        host = input("Enter server IP address: ")
        
        username_right = True
        
        while not username_right:
            username = input("Enter your username: ")
            usernames = []
            usernames.append(username)
            if username in usernames:
                not username_right
                print('Username on kasutusel juba')
            
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client.connect((host, port))

            receive_thread = threading.Thread(target=receive, args=(client, username))
            receive_thread.start()

            write_thread = threading.Thread(target=write, args=(client,))
            write_thread.start()
            break

        except socket.error:
            print("No connection established. Please try again.")
            continue


if __name__ == "__main__":
    main()
