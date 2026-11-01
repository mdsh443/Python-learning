import socket

# Create a TCP socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Give the server an address and port.
server.bind(("127.0.0.1", 7001))

# Start listening for connections.
server.listen()
print("Server is waiting for a client...")

# Wait until a client connects.
connection, address = server.accept()
print(f"Client connected: {address}")

# Receive and display the client's message.
message = connection.recv(1024).decode()
print(f"Client says: {message}")

# Send a reply.
connection.sendall("Router1 is ready".encode())

# Close the connection and server socket.
connection.close()
server.close()



