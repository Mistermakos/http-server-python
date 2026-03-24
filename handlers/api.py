import json
from httpResponse import httpResponse


def apiHandler(type, path, conn):
    response_body = json.dumps({"DATA": [type, path]})
    res = httpResponse(200, f"application/json")
    res.addConnection(0)
    res.addContentLength(response_body)
    res.send(conn)
    conn.sendall(response_body.encode())
    print("Server: Api: Responding Successfully")
