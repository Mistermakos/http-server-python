import os
from http_response import http_response


def site_handler(conn):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "../website/index.html")
    filetosend = open(path, "rb")

    data = filetosend.read(1024)
    print("Sending main site...")
    res = http_response(200, "html")
    res.send(conn)
    conn.sendall(data)
    filetosend.close()
