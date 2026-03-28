import socket
from handlers.api import apiHandler
from handlers.error import errorHandler
from handlers.static import staticHandler
from handlers.site import siteHandler

TCP_IP_LOCAL = "0.0.0.0"
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
            # reciving, decoding, taking important info
            conn.settimeout(5)
            try:
                dataRaw = conn.recv(2048)
            except socket.timeout:
                continue
            dataDecoded = dataRaw.decode()
            requestMainData = dataDecoded.split("\r\n")[0].split(" ")
            requestType, requestPath, requestVersion = requestMainData[0:3]
            
            
            # Console report
            print(
                "Server: Connected by: "
                + str(address)
                + " Type: "
                + requestType
                + " Path: "
                + requestPath
            )
            # if data recived, pass it to handlers
            print(requestPath)
            if dataRaw:
                if requestPath.startswith("/api/v1"):
                    apiHandler(requestType, requestPath, conn)
                elif requestPath.startswith("/static/"):
                    staticHandler(requestPath, conn)
                elif requestPath == ("/"):
                    siteHandler(conn)
                else:
                    print("Server: Error with receving data")
                    errorHandler(conn, 404)
