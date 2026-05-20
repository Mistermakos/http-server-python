import os
from http_response import http_response


# Opens main page, returns error if the file is not found
# main page should be named index.html in that case, may be changed ofc
def open_file():
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "../website/index.html")
    try:
        with open(path, "rb") as f:
            return f.read(1024)
    except IOError:
        return None


def site_handler(conn):
    filetosend = open_file()

    if filetosend is None:
        return None

    print("Sending main site...")
    res = http_response(200, "html")
    res.send(conn)
    conn.sendall(filetosend)
    filetosend.close()
