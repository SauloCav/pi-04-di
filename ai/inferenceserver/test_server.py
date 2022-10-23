import pytest
import requests
import multiprocessing
from time import sleep

from env import HOST, PORT
from server import serve


ENDPOINT = f"http://{HOST}:{PORT}"


@pytest.fixture(autouse=True, scope="session")
def setup_server():
    """Setups server for endpoint testing"""
    server_process = multiprocessing.Process(target=serve, args=(HOST, PORT))
    server_process.start()
    # Awaits for server to start
    sleep(5)
    yield
    server_process.terminate()


def test_server():
    res = requests.get(
        ENDPOINT,
        params={
            "comment": "welcome to Narnia",
        },
    )
    assert res.status_code == 200
