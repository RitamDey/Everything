import socket


HOST, PORT = '127.0.0.1', 8888

# We first create a TCP socket object that binds to a IPv4
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# We set some options for the socket
# We pass at which level the option lies. Here its at the socket's API level
# We want to set the socket's binding address reuse behaviour
# And sent it to 1 which means On
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# We bind the socket to the HOST and PORT
listen_socket.bind((HOST, PORT))

# We only want to listen to only one client
listen_socket.listen(1)
print(f"Serving HTTP on port {PORT}")
try:
    while True:  # Main listen loop

        # When a connection is accpted by a socket,
        # it returns the clien's connection type and its connecting IP
        client_connection, client_address = listen_socket.accept()
        print(f"Connected to {client_address[0]}:{client_address[1]}")

        # Here we recieve 1024 bytes of what the client sends.
        # Here the client only sents the headers
        request = client_connection.recv(1024)
        print(request)

        # A really basic response
        http_response = """\
HTTP/1.1 200 OK

Hello World!
        """

        # Here we send all the response to all the clients
        # We need to send the bytes represntation of the string
        # This is donw via encode() and is only required for Py3
        client_connection.sendall(http_response.encode())
        client_connection.close()  # Clost client connection
except KeyboardInterrupt:
    print("Closing down")
