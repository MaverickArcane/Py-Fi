# Simple HTTP/1.0 server from scratch
import socket
import threading

banner = """
'||'''|,              '||''''|      
 ||   ||               ||  .    ''  
 ||...|' '||  ||` ---  ||''|    ||  
 ||       `|..||       ||       ||  
.||           ||      .||.     .||. 
           ,  |'                    
            ''                      
"""

print(banner)


def handle_connection(client_connection, client_address):
    # Receive the client request
    request = client_connection.recv(1024).decode()
    if request:
        f = open("./logs/AccessLog.txt", "a")
        print("Connection received, Connection details: \n%s\n\n" % request)
        f.write("Connection received, Connection details: \n%s\n\n" % request)
        f.close()
    
    # Parse headers
    headers = request.split('\n')
    filename = headers[0].split()[1]

    # Set root directory to html page
    if filename == '/':
        filename = '/index.html'

    # Try to access the parsed GET request
    try:
        fin = open('htdocs' + filename)
        content = fin.read()
        fin.close()
        # Send 200 response and content of the page
        response = "HTTP/1.0 200 OK\n\n" + content
    except FileNotFoundError:
        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    client_connection.sendall(response.encode())
    client_connection.close()
    pass

# Define hosted IP and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
print("Server Started! Listening on port %s...\n" % SERVER_PORT)

while True:
    # Listening for incoming connections & create a new thread to handle it
    client_connection, client_address = server_socket.accept()
    connection_thread = threading.Thread(target=handle_connection, args=(client_connection, client_address))
    connection_thread.start()
    


# Close socket
server_socket.close()
