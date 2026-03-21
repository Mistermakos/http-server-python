import json


def apiHandler(type, path, conn):
    response_body = json.dumps({"DATA": [type, path]})

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: application/json\r\n"
        "Connection: close\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"
        f"{response_body}"
    )
    print("Server: Api: Responding Successfully")
    conn.sendall(response.encode())
