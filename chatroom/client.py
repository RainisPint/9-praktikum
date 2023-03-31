import socket
import threading


def main():
    def receive():
        while True:
            try:
                message = client.recv(1024).decode("utf-8")
                if message == "USER":
                    client.send(username.encode("utf-8"))
                else:
                    print(message)
            except:
                print("An error occurred.")
                client.close()
                break

    def write():
        while True:
            message = f"{username}: {input('')}"
            client.send(message.encode("utf-8"))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server, port))

    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()


if __name__ == "__main__":
    server = input("Enter server IP address: ")
    # server = "127.0.0.1"
    port = 12345
    username = input("Enter your username: ")
    main()
