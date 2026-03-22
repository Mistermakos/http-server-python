import os
from httpResponse import httpResponse


def siteHandler(conn):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "../website/index.html")
    filetosend = open(path, "rb")

    data = filetosend.read(1024)
    while data:
        print("Sending main site...")
        res = httpResponse(200, "text/html")
        res.send(conn)
        conn.sendall(data)
        data = filetosend.read(1024)
    filetosend.close()
