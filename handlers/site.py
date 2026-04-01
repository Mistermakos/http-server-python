import os
from httpResponse import httpResponse


def site_handler(conn):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "../website/index.html")
    filetosend = open(path, "rb")

    data = filetosend.read(1024)
    print("Sending main site...")
    res = httpResponse(200, "html")
    res.send(conn)
    conn.sendall(data)
    filetosend.close()
