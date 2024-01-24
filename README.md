**Readme.md**

# Chat Application

## Server Code (server.py)

### Description
This Python script implements a simple chat server using sockets and multithreading. The server allows multiple clients to connect, choose a nickname, and engage in a chat conversation. The communication protocol is ASCII-based.

### Dependencies
- Python 3.x
- threading module
- socket module

### Usage
1. Run the server script (`server.py`) on a host machine.
2. Clients can connect to the server using the appropriate IP address and port.

### Code Overview
- The server listens for incoming connections on a specified IP address (`127.0.0.1`) and port (`55555`).
- Multiple clients can connect, each providing a unique nickname.
- The server supports both global chat messages and direct messages using the '@' symbol.
- If a client sends a message starting with '@', it is treated as a direct message to a specific user.
- The server handles disconnections and broadcasts messages to all connected clients.

### Execution
```bash
python server.py
```

## Client Code (client.py)

### Description
This Python script implements a simple chat client that can connect to the server, choose a nickname, and engage in a chat conversation. The client supports both receiving and sending messages concurrently using multithreading.

### Dependencies
- Python 3.x
- threading module
- socket module

### Usage
1. Run the client script (`client.py`) on a client machine.
2. Enter a unique nickname when prompted.
3. Start sending and receiving messages.

### Code Overview
- The client connects to the server using the server's IP address (`127.0.0.1`) and port (`55555`).
- The client can send global messages to all connected users or direct messages to a specific user.
- The communication protocol involves encoding and decoding messages in ASCII.
- The client uses multithreading to handle both message reception and user input simultaneously.

### Execution
```bash
python client.py
```

## Important Note
Make sure to run the server script before connecting any clients. Adjust the server's IP address and port if needed.

**Disclaimer**: This is a basic implementation for educational purposes. It may not cover all edge cases and security considerations for a production-level application.
