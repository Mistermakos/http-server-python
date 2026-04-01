import socket
from handler import handle_connection

TCP_IP_LOCAL = "0.0.0.0"
PORT = 5000

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        while True:
            conn, address = s.accept()
            with conn:
                handle_connection(conn, address)

start_server(TCP_IP_LOCAL, PORT)