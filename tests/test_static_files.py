import pytest
from handlers.static import parse_static_request

def test_parse_static_request():
    res = parse_static_request("/static/file.txt")
    assert res 