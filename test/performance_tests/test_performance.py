import logging
import random
import string
import time

import requests

LOGGER = logging.getLogger(__name__)
SAMPLE_SIZE = 100


def test_add_todo():
    LOGGER.info('Performance Test For Add todo')
    # Empties the file for each test run, in order to generate new data
    open("test_add_todo.csv", "w").close()
    f = open("test_add_todo.csv", "a")
    for i in range(10001):
        start = time.time()
        requests.post("http://localhost:4567/todos", json={"title": "test"},
                      headers={'content-type': 'application/json'})
        end = time.time()
        delta = end - start

        # Power of 10, log the time
        if i in [10, 100, 1000, 10000]:
            LOGGER.info(f'Add Test For {i} todos in the System: {delta}s')

        f.write(f"{i},{delta}\n")
    f.close()
    LOGGER.info('--------------------------------')


def test_delete_todo():
    LOGGER.info('Performance Test For Delete todo')
    # Empties the file for each test run, in order to generate new data
    open("test_delete_todo.csv", "w").close()
    f = open("test_delete_todo.csv", "a")
    for i in range(10001):
        # First request is to arm the test with data
        requests.post("http://localhost:4567/todos", json={"title": "test"},
                      headers={'content-type': 'application/json'})
        # Second request is to insert something we know exists so we can delete it.
        r = requests.post("http://localhost:4567/todos", json={"title": "test"},
                          headers={'content-type': 'application/json'})
        id = None
        try:
            id = r.json()['id']
        except KeyError:
            assert False

        start = time.time()
        requests.delete(f"http://localhost:4567/todos/{id}")
        end = time.time()
        delta = end - start
        # Power of 10, log the time
        if i in [10, 100, 1000, 10000]:
            LOGGER.info(f'Delete Test For {i} todos in the System: {delta}s')

        f.write(f"{i},{delta}\n")
    f.close()
    LOGGER.info('--------------------------------')


def test_modify_todo():
    LOGGER.info('Performance Test For Modify todo')
    # Empties the file for each test run, in order to generate new data
    open("test_modify_todo.csv", "w").close()
    f = open("test_modify_todo.csv", "a")
    for i in range(10001):
        # First request is to arm the test with data
        requests.post("http://localhost:4567/todos", json={"title": "test"},
                      headers={'content-type': 'application/json'})
        # Second request is to insert something we know exists so we can modify it.
        r = requests.post("http://localhost:4567/todos", json={"title": "test"},
                          headers={'content-type': 'application/json'})
        id = None
        try:
            id = r.json()['id']
        except KeyError:
            assert False

        start = time.time()
        requests.post(f"http://localhost:4567/todos/{id}",
                      json={
                          "title": "test tasks amended again",
                          "doneStatus": False,
                          "description": "Something useful!"
                      })
        end = time.time()
        delta = end - start
        # Power of 10, log the time
        if i in [10, 100, 1000, 10000]:
            LOGGER.info(f'Delete Test For {i} todos in the System: {delta}s')

        f.write(f"{i},{delta}\n")
    f.close()
    LOGGER.info('--------------------------------')


def test_performance_add_project():
    size = 0
    LOGGER.info('Performance Test For Add Project')
    for i in [10, 100, 1000, 10000]:
        for _ in range(i - size):
            __add_project()  # create up to i project
        size = i
        time = 0
        for _ in range(SAMPLE_SIZE):  # test 500 time to get the average value
            time = time + __get_add_project_time()
        avg_time = time / SAMPLE_SIZE
        LOGGER.info(f'Add Test For {i} Projects in the System: {avg_time}s')
    LOGGER.info('--------------------------------')


def test_performance_change_project():
    size = 0
    LOGGER.info('Performance Test For Change Project')
    for i in [10, 100, 1000, 10000]:
        for _ in range(i - size):
            __add_project()  # create up to i project
        size = i
        time = 0
        for _ in range(SAMPLE_SIZE):  # test 500 time to get the average value
            time = time + __get_change_project_time()
        avg_time = time / SAMPLE_SIZE
        LOGGER.info(f'Change Test For {i} Projects in the System: {avg_time}s')
    LOGGER.info('--------------------------------')


def test_performance_delete_project():
    size = 0
    LOGGER.info('Performance Test For Delete Project')
    for i in [10, 100, 1000, 10000]:
        for _ in range(i - size):
            __add_project()  # create up to i project
        size = i
        time = 0
        for _ in range(SAMPLE_SIZE):  # test 500 time to get the average value
            time = time + __get_delete_project_time()
        avg_time = time / SAMPLE_SIZE
        LOGGER.info(f'Delete Test For {i} Projects in the System: {avg_time}s')
    LOGGER.info('--------------------------------')


def __add_project():
    title = __get_random_string(6)
    r = requests.post("http://localhost:4567/projects", json={"title": title},
                      headers={'content-type': 'application/json'})
    assert r.status_code == 201


def __get_add_project_time():
    title = 'sample title'
    time_before = time.time()
    r = requests.post('http://localhost:4567/projects', json={"title": title},
                      headers={'content-type': 'application/json'})
    time_after = time.time()
    assert r.status_code == 201
    project_id = str(r.json()['id'])
    r = requests.delete(f'http://localhost:4567/projects/{project_id}')
    assert r.status_code == 200  # delete the created project to restore to remove side effect.
    return time_after - time_before


def __get_delete_project_time():
    title = 'sample title'
    # Create a sample project
    r = requests.post('http://localhost:4567/projects', json={"title": title},
                      headers={'content-type': 'application/json'})
    assert r.status_code == 201
    project_id = str(r.json()['id'])
    time_before = time.time()
    r = requests.delete(f'http://localhost:4567/projects/{project_id}')
    time_after = time.time()
    assert r.status_code == 200  # delete the created project to restore to remove side effect.
    return time_after - time_before


def __get_change_project_time():
    title = 'sample title'
    # Create a sample project
    r = requests.post('http://localhost:4567/projects', json={"title": title},
                      headers={'content-type': 'application/json'})
    assert r.status_code == 201
    project_id = str(r.json()['id'])
    new_body = {
        'title': __get_random_string(6),
        'completed': bool(random.getrandbits(1)),
        'active': bool(random.getrandbits(1)),
        'description': __get_random_string(10)
    }
    time_before = time.time()
    r = requests.post(f'http://localhost:4567/projects/{project_id}', json=new_body,
                      headers={'content-type': 'application/json'})
    time_after = time.time()
    assert r.status_code == 200
    r = requests.delete(f'http://localhost:4567/projects/{project_id}')
    assert r.status_code == 200  # delete the created project to restore to remove side effect.
    return time_after - time_before


def __get_random_string(length):
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(length))
    return title
