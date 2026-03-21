import os


def staticHandler(requested, conn):
    requestedFile = requested.split("/")[1]
    requestedEx = requestedFile.split(".")[1]
    print(requestedFile)
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, f"../website/{requestedFile}")
    filetosend = open(path, "rb")

    data = filetosend.read(1024)
    while data:
        print("Sending...")
        print(requestedFile, requestedEx)
        conn.send((f"HTTP/1.1 200 OK\nContent-Type: text/{requestedEx}\n\n").encode())
        conn.sendall(data)
        data = filetosend.read(1024)
    filetosend.close()
