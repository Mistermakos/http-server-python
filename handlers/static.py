import os
from httpResponse import httpResponse

def parse_static_request(requested):
    requestedFile = requested.split("/")[2]  # name of file
    # ex for file (needed for Content-Type in response)
    requestedEx = requestedFile.split(".")[1]
    return requestedEx, requestedFile

def load_file(file_name):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, f"../website/{file_name}")
    try:
        with open(path, "rb") as f:
            return f.read()
    except OSError:
        return None

def static_handler(requested, conn):
    file_extension, file_name = parse_static_request(requested)
    file_to_send = load_file(file_name)
    if file_to_send is None:
        print("Could not open/read file")
        res = httpResponse(404, "json")
        res.addConnection(0)
        res.send(conn)
        return 
    res = httpResponse(200, file_extension)
    res.send(conn) 
    print(f"Sending {file_name}...")
    conn.sendall(file_to_send)
    return
