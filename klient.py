import socket

TCP_IP_LOCAL = "127.0.0.1"
PORT = 5000
CONN_TUPLE = (TCP_IP_LOCAL, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(CONN_TUPLE)
    print("Wysyłam halo")
    s.sendall(b"Halo")
    data = s.recv(1024)
print("Odebrałem: " + str(data))