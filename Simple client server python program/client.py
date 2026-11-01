import socket

# Create a TCP socket.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server.
client.connect(("127.0.0.1", 7001))

# Send a message.
message = input("Enter a message: ")
client.sendall(message.encode())

# Receive and display the server's reply.
reply = client.recv(1024).decode()
print(f"Server says: {reply}")

# Close the connection.
client.close()