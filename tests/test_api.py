from unittest.mock import Mock
from handlers.api import api_handler


def test_api_handler():
    conn = Mock()
    api_handler("GET", "/users", conn)
    expected = b'{"DATA": ["GET", "/users"]}'
    conn.sendall.assert_called_once_with(expected)
