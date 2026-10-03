# server.py
# Networking module - clinic info server (TCP)

import socket

HOST = "127.0.0.1"
PORT = 65432

# clinic data
HOURS = "Monday-Friday 8am-5pm, closed weekends and holidays"
APPOINTMENTS = ["Oct 10, 9:00 AM", "Oct 10, 2:30 PM", "Oct 11, 11:00 AM", "Oct 13, 3:00 PM"]
FAQS = {
    "1": "Q: Do I need a referral? A: No, you can self-refer for a general checkup.",
    "2": "Q: What insurance do you accept? A: Most major providers, call to confirm yours.",
    "3": "Q: Can I reschedule online? A: Not yet, please call the front desk.",
}

# tracks which appointment slot to hand out next
next_appt_index = 0


# builds the response text for a given request
def request):
    global next_appt_index
    command = request.strip()

    if command == "HOURS":
        return HOURS

    if command == "NEXT_APPT":
        if next_appt_index < len(APPOINTMENTS):
            slot = APPOINTMENTS[next_appt_index]
            next_appt_index += 1
            return f"Next available: {slot}"
        return "No more slots available"

    if command.startswith("FAQ"):
        parts = command.split()
        if len(parts) == 2 and parts[1] in FAQS:
            return FAQS[parts[1]]
        return "Unknown FAQ number. Try FAQ 1, FAQ 2, or FAQ 3"

    return "Unknown request. Try HOURS, NEXT_APPT, or FAQ <number>"


# starts the server and handles one client request at a time
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        connection, address = server_socket.accept()
        with connection:
            print(f"Connected by {address}")
            data = connection.recv(1024)
            if not data:
                continue

            request = data.decode("utf-8")
            print(f"Received: {request.strip()}")

            if request.strip() == "QUIT":
                connection.sendall("Server shutting down".encode("utf-8"))
                print("Shutdown request received")
                break

            response = handle_request(request)
            connection.sendall(response.encode("utf-8"))
            print(f"Sent: {response}")

    server_socket.close()
    print("Server stopped")


if __name__ == "__main__":
    main()
