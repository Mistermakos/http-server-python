from http_response import http_response
from handlers.error import error_handler
from unittest.mock import patch, Mock


def test_error_404():
    # given
    conn = Mock()
    with patch("handlers.error.http_response") as mock_response:
        res_instance = Mock()
        mock_response.return_value = res_instance
        # when
        error_handler(conn, 404)
        # then
        mock_response.assert_called_once_with(404, "json")
        res_instance.send.assert_called_once_with(conn)


def test_error_500():
    # given
    conn = Mock()
    with patch("handlers.error.http_response") as mock_response:
        res_instance = Mock()
        mock_response.return_value = res_instance
        # when
        error_handler(conn, 500)
        # then
        mock_response.assert_called_once_with(500, "json")
        res_instance.send.assert_called_once_with(conn)
