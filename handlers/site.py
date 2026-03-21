import os


def siteHandler(conn):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "../website/index.html")
    filetosend = open(path, "rb")

    data = filetosend.read(1024)
    while data:
        print("Sending...")
        conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n".encode())
        conn.sendall(data)
        data = filetosend.read(1024)
    filetosend.close()
