import json
from http_response import http_response


def api_handler(type, path, conn):
    response_body = json.dumps({"DATA": [type, path]})
    res = http_response(200, "json")
    res.addConnection(0)
    res.addContentLength(response_body)
    res.send(conn)
    conn.sendall(response_body.encode())
    print("Server: Api: Responding Successfully")
