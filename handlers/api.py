import json
from httpResponse import httpResponse


def apiHandler(type, path, conn):
    response_body = json.dumps({"DATA": [type, path]})
    res = httpResponse(200, f"application/json")
    res.addConnection(0)
    res.addData(response_body)
    print("Server: Api: Responding Successfully")
    res.send(conn)
