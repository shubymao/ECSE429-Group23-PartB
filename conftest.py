import pytest
import subprocess
import os
import requests
import socket
import time

class GLOBAL_CONTEXT:
    todo_id = None
    task_id = None
    project_id = None
    category_id = None
    json_object = None
    response_json = None
    high_priority_response = None
    status_code = None

@pytest.fixture(autouse=True, scope="function")
def setup():
    # Attempts to start the process.
    subprocess.Popen(['java', '-jar', os.environ['JAR_PATH']])
    # Start timer for timeout which is current time + 3 seconds for timeout
    timeout = time.time() + 3
    # We loop until we either reach a time upper bound, or a socket with this program's expected port opens
    while socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(("localhost", 4567)) != 0:
        # It's not gonna come up by this point :(
        if time.time() > timeout:
            raise ConnectionError("Cannot connect to program/server. Test cannot continue")
    # Loop terminates here because the socket connection has opened. Start testing.
    yield
    # This section corresponds to post-test teardown.
    try:
        requests.get("http://localhost:4567/shutdown")
    except Exception:
        pass
