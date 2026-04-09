from http_response import http_response


def error_handler(conn, type):
    res = http_response(type, "json")
    if type == 404:
        print("Server: Responding Error 404")
    else:
        print("Server: Responding Error 500")
    res.addConnection(0)
    return res.send(conn)
