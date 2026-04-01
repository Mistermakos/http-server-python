from httpResponse import httpResponse


def error_handler(conn, type):
    res = httpResponse(type, "json")
    if(type == 404):
        print("Server: Responding Error 404")
    else:
        print("Server: Responding Error 500")
    res.addConnection(0)
    res.send(conn)
    return