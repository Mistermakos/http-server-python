from unittest.mock import patch, mock_open, Mock
from handlers.static import parse_static_request, load_file, static_handler
from http_response import http_response


def test_parse_static_request():
    res = parse_static_request("/static/file.txt")
    assert res[0] == "txt" and res[1] == "file.txt"


def test_loading_file():
    # creating mock (false file) to check if it reads file
    mock_data = b"Hello world"
    with patch("builtins.open", mock_open(read_data=mock_data)) as s:
        res = load_file("test.txt")
    assert res == mock_data


def test_loading_file_exeption():
    with patch("builtins.open", side_effect=OSError):
        res = load_file("test.txt")
    assert res is None


def test_handler_file_exists():
    # given
    conn = Mock()
    with patch(
        "handlers.static.parse_static_request", return_value=("html", "index.html")
    ), patch("handlers.static.load_file", return_value=b"Hello world"), patch(
        "handlers.static.http_response"
    ) as mock_response:

        res_instance = Mock()
        mock_response.return_value = res_instance

        # when
        static_handler("GET /index.html", conn)

        # then
        mock_response.assert_called_once_with(200, "html")
        res_instance.send.assert_called_once_with(conn)
        conn.sendall.assert_called_once_with(b"Hello world")
        # res_instance.send.assert_called_once_with(conn)
        # conn.sendall.assert_called_once_with(b"DATA")


# def test_handler_file_not_existing():
