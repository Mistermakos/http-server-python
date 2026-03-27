# tests/test_tcp.py
import pytest
import socket

def test_server_connects():
    s = socket.socket()
    s.connect(("localhost", 5000))
    s.send(b"Hello")
    resp = s.recv(1024)
    s.close()
    assert b"Hello" in resp