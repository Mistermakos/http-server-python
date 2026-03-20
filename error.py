def errorHandler(conn):
    response = (
        "HTTP/1.1 500 ERR\r\n"
        "Content-Type: application/json\r\n"
        "Connection: close\r\n"
    )
    print("Server: Responding Error")
    conn.sendall(response.encode())
