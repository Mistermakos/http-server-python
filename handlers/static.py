import os
from httpResponse import httpResponse


def staticHandler(requested, conn):
    requestedFile = requested.split("/")[2]  # name of file

    # ex for file (needed for Content-Type in response)
    requestedEx = requestedFile.split(".")[1]

    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, f"../website/{requestedFile}")

    try:
        filetosend = open(path, "rb")
    except OSError:
        print("Could not open/read file")
        res = httpResponse(404, f"application/json")
        res.addConnection(0)
        res.send(conn)

    data = filetosend.read(1024)
    while data:
        print(f"Sending {requestedFile}...")
        res = httpResponse(200, f"text/{requestedEx}")
        res.send(conn)
        conn.sendall(data)
        data = filetosend.read(1024)
    filetosend.close()
