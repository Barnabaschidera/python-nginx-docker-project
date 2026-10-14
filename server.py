
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("0.0.0.0",8080))
server.listen()
print("listening on port 8080...")

while True:
    conn, addr = server.accept()
    request = conn.recv(1024)
    print(request.decode())

    response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
    conn.sendall(response.encode())
    conn.close()
