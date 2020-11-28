import time

import requests


def test_add_todo():
    # Empties the file for each test run, in order to generate new data
    open("test_add_todo.csv", "w").close()
    f = open("test_add_todo.csv", "a")
    for i in range(10000):
        start = time.time()
        requests.post("http://localhost:4567/todos", json={"title": "test"},
                      headers={'content-type': 'application/json'})
        end = time.time()
        delta = end - start

        f.write(f"{i},{delta}\n")
    f.close()


def test_delete_todo():
    # Empties the file for each test run, in order to generate new data
    open("test_delete_todo.csv", "w").close()
    f = open("test_delete_todo.csv", "a")
    for i in range(10000):
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

        f.write(f"{i},{delta}\n")
    f.close()


def test_modify_todo():
    # Empties the file for each test run, in order to generate new data
    open("test_modify_todo.csv", "w").close()
    f = open("test_modify_todo.csv", "a")
    for i in range(10000):
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

        f.write(f"{i},{delta}\n")
    f.close()

# def test_categories_performance():
#     raise NotImplemented
#
#
# def test_projects_performance():
#     raise NotImplemented
