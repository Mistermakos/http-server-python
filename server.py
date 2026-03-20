import socket
from api import apiHandler
from error import errorHandler

TCP_IP_LOCAL = "127.0.0.1"
PORT = 5000
CONN_TUPLE = (TCP_IP_LOCAL, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Building a brige
    s.bind(CONN_TUPLE)
    # Only 1 device
    s.listen(1)

    # Listening without limit
    while True:
        conn, address = s.accept()
        with conn:
            print("Server: Connected by:" + str(address))
            # reciving, decoding, taking important info
            dataRaw = conn.recv(1024)
            dataDecoded = dataRaw.decode()
            requestMainData = dataDecoded.split("\r\n")[0].split(" ")
            requestType, requestPath, requestVersion = requestMainData[0:3]

            # if data recived, pass it to handlers
            if dataRaw:
                match requestPath:
                    case "/v1/api":
                        apiHandler(requestType, requestPath, conn)
                    case "/":
                        print("")  # to be implemented
                    case _:
                        print("Server: Error with receving data")
                        errorHandler(conn)
