# client.py
# Networking module - clinic info client (TCP)

import socket
import time

HOST = "127.0.0.1"
PORT = 65432


# connects, sends one request, and returns the server's response
def send_request(command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall(command.encode("utf-8"))
    data = client_socket.recv(1024)
    client_socket.close()
    return data.decode("utf-8")


# runs a demo sequence of the three request types, plus one bad request
def main():
    requests = [
        "HOURS",
        "NEXT_APPT",
        "FAQ 1",
        "FAQ 2",
        "NEXT_APPT",
        "FAQ 9",
    ]

    for command in requests:
        print(f"\nClient sending: {command}")
        response = send_request(command)
        print(f"Server responded: {response}")
        time.sleep(1)

    print("\nSending QUIT to stop the server")
    print(send_request("QUIT"))


if __name__ == "__main__":
    main()
