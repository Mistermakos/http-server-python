class httpResponse:
    def __init__(self, codeNum, contentType):
        self.codeNum = codeNum
        self.contentType = contentType
        self.response = f"HTTP/1.1 {codeNum}\r\n" f"Content-Type: {contentType}\r\n"

    def addConnection(self, connection):
        if connection == 0:
            self.response += "Connection: close\r\n"

    def addContentLength(self, data):
        self.response += f"Content-Length: {len(data.encode())}\r\n"

    def send(self, conn):
        self.response += "\r\n"
        conn.send(self.response.encode())
