# Overview

For this module I wanted to actually build something with sockets instead of just reading about the client-server model, so I wrote a small clinic information server in Python. It's a TCP server and client pair: the server holds basic clinic info (office hours, a list of open appointment slots, and a few FAQ answers), and the client connects to it and asks for one of those things by sending a short text command.

To run it, start the server first with `python3 server.py`, then in a separate terminal run `python3 client.py`. The client automatically sends a sequence of requests (HOURS, NEXT_APPT, FAQ 1, FAQ 2, another NEXT_APPT, and an invalid FAQ number to show error handling), prints the server's response for each one, and then sends QUIT to shut the server down cleanly.

I picked a healthcare-admin style client/server because it ties into the Healthcare Admin focus area I'm using for my AI master's degree coursework this semester, and because sockets are the foundation underneath a lot of the client-server and agent-to-service communication I'll eventually be building there.

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

This uses the client-server model: `server.py` listens for connections and `client.py` connects to it. The server handles one connection at a time, in a simple loop (no threading), which keeps the request/response flow easy to follow.

It uses TCP (`socket.SOCK_STREAM`) over port 65432 on localhost. Messages are plain UTF-8 text, newline-free single commands: `HOURS`, `NEXT_APPT`, `FAQ <number>`, or `QUIT`. The server replies with a plain text string, and the connection closes after each request/response pair.

# Development Environment

- VS Code
- Python 3
- Built entirely with Python's standard `socket` library, no external networking packages

# Useful Websites

- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- [Real Python - Socket Programming in Python](https://realpython.com/python-sockets/)
- [Wikipedia - Client-server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)

# Future Work

- Add threading so the server can handle more than one client at a time
- Let the client take typed input instead of only running the fixed demo sequence
- Store the clinic data in a small file or database instead of hardcoding it in the server
