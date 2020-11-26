import requests
import time


def test_add_todo():
    size = 0
    for i in [10, 100, 1000, 10000]:
        __todo_adder_helper(i - size)
        size = i
        start_time = time.time()
        for _ in range(500):
            __add_todo()
        end_time = time.time()
        delta = end_time - start_time
        print(f"Add size {i}: {delta}")

    assert False

def test_delete_todo():
    size = 0
    for i in [10, 100, 1000, 10000]:
        __todo_adder_helper(i - size)
        size = i
        start_time = time.time()
        __delete_todo(size - 1)
        end_time = time.time()
        delta = end_time - start_time
        print(f"Delete size {i}: {delta}")

    assert False


# Adds a to do entry without the overhead of randomization or whatnot.
def __add_todo():
    requests.post("http://localhost:4567/todos", json={"title": "test add random items"},
                  headers={'content-type': 'application/json'})


# Deletes a to do entry
def __delete_todo(id):
    assert 200 == requests.delete(f"http://localhost:4567/todos/{id}").status_code


# Adds a to do list to the REST API Server
def __todo_adder_helper(amount):
    # TODO: Generate random_string
    for _ in range(amount):
        assert 201 == requests.post("http://localhost:4567/todos", json={"title": "test"},
                      headers={'content-type': 'application/json'}).status_code

# def test_categories_performance():
#     raise NotImplemented
#
#
# def test_projects_performance():
#     raise NotImplemented
