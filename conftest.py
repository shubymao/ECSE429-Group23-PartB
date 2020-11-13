import pytest
import subprocess
import os
import requests
import socket

@pytest.fixture(autouse=True, scope="function")
def setup():
    subprocess.Popen(['java', '-jar', os.environ['JAR_PATH']])
    while socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(("localhost", 4567)) != 0:
        continue
    yield
    try:
        requests.get("http://localhost:4567/shutdown")
        pass
    except Exception:
        pass
