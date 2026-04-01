from handlers.api import api_handler
from handlers.error import error_handler
from handlers.static import static_handler
from handlers.site import site_handler


def route_request(request_type, request_path, conn):
    # reciving, decoding, taking important info
    # if data recived, pass it to handlers
    print(request_path)
    if request_path.startswith("/api/v1"):
        api_handler(request_type, request_path, conn)
    elif request_path.startswith("/static/"):
        static_handler(request_path, conn)
    elif request_path == ("/"):
        site_handler(conn)
    else:
        print("Server: Error with receving data")
        error_handler(conn, 404)


def handle_connection(conn, address):
    conn.settimeout(5)
    data_raw = conn.recv(2048)

    if not data_raw:
        return

    data_decoded = data_raw.decode()
    request_main_data = data_decoded.split("\r\n")[0].split(" ")
    request_type, request_path, request_version = request_main_data[0:3]
    # Console report
    print(
        "Server: Connected by: "
        + str(address)
        + " Type: "
        + request_type
        + " Path: "
        + request_path
    )

    route_request(request_type, request_path, conn)
