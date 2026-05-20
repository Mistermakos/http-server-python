from unittest.mock import patch, mock_open
from handlers.site import open_file


def test_open_file_works():
    fake_html = "<html>Hello world</html>"

    with patch("builtins.open", mock_open(read_data=fake_html)):
        res = open_file()
        assert res == fake_html


def test_open_file_not_working():
    with patch("builtins.open", side_effect=IOError):
        res = open_file()
        assert res is None
