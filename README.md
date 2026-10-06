# computer-networks-tcp-client-server# Computer Networks – TCP Client-Server Communication

## Project Overview

This project demonstrates basic client-server communication using Python TCP sockets. A server listens for a client connection, establishes communication, sends a welcome message, and records the connection time.

## Technologies Used

* Python
* Socket Programming
* TCP Protocol
* Windows

## Project Structure

```text
cn
│
├── server.py
├── client.py
└── README.md
```

## How It Works

1. The server starts and listens on port `6060`.
2. The client connects to the server.
3. The server sends a welcome message to the client.
4. The connection time is recorded.
5. The client sends a connection completion message.
6. The server calculates the connection duration.

## How to Run

First, start the server:

```bash
python server.py
```

Then open another terminal and run:

```bash
python client.py
```

## Learning Outcome

This project helped us understand TCP socket communication, client-server architecture, IP addresses, ports, connections, and basic network communication using Python.
