import socket

# Define server IP address (replace with server IP from Table 4)
SERVER_IP = "172.16.0.10"  # Example server IP from Table 4

# Define port number (change if needed)
PORT = 5000

def send_data(message):
  """
  Sends a message to the server on the specified port.
  """
  # Create a TCP socket
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Connect to the server
  client_socket.connect((SERVER_IP, PORT))

  # Send the message
  client_socket.sendall(message.encode())

  # Receive response (optional)
  # response = client_socket.recv(1024).decode()
  # print(f"Received from server: {response}")

  # Close the socket
  client_socket.close()

# Example usage (replace message with data specific to your application)
message = "Hello from the client!"
send_data(message)

print(f"Sent message: {message} to server {SERVER_IP}")
