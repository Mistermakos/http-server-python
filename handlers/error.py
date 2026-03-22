from httpResponse import httpResponse


def errorHandler(conn):
    print("Server: Responding Error 404")
    res = httpResponse(404, "application/json")
    res.addConnection(0)
    res.send(conn)
