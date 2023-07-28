import socket
 
# Create a connection to the server application on port 81
tcp_socket = socket.create_connection(('localhost', 81))
 
try:
    data = str.encode('Hi. I am a TCP client sending data to the server')
    tcp_socket.sendall(data)
 
finally:
    print("Closing socket")
    tcp_socket.close()