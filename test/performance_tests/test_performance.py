import random
import string
import requests
import time
import logging

LOGGER = logging.getLogger(__name__)
SAMPLE_SIZE = 100

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

def test_performance_add_project():
    size = 0
    LOGGER.info('Performance Test For Add Project')
    for i in [10, 100, 1000, 10000]:
        for _ in range(i-size):
            __add_project() #create up to i project
        size = i
        time = 0
        for _ in range(SAMPLE_SIZE): # test 500 time to get the average value
            time = time + __get_add_project_time()
        avg_time = time / SAMPLE_SIZE
        LOGGER.info(f'Add Test For {i} Projects in the System: {avg_time}s')
    LOGGER.info('--------------------------------')

def test_performance_change_project():
    size = 0
    LOGGER.info('Performance Test For Change Project')
    for i in [10, 100, 1000, 10000]:
        for _ in range(i-size):
            __add_project() #create up to i project
        size = i
        time = 0
        for _ in range(SAMPLE_SIZE): # test 500 time to get the average value
            time = time + __get_change_project_time()
        avg_time = time / SAMPLE_SIZE
        LOGGER.info(f'Change Test For {i} Projects in the System: {avg_time}s')
    LOGGER.info('--------------------------------')

def test_performance_delete_project():
    size = 0
    LOGGER.info('Performance Test For Delete Project')
    for i in [10, 100, 1000, 10000]:
        for _ in range(i-size):
            __add_project() #create up to i project
        size = i
        time = 0
        for _ in range(SAMPLE_SIZE): # test 500 time to get the average value
            time = time + __get_delete_project_time()
        avg_time = time / SAMPLE_SIZE
        LOGGER.info(f'Delete Test For {i} Projects in the System: {avg_time}s')
    LOGGER.info('--------------------------------')

    
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
    assert r.status_code == 200 # delete the created project to restore to remove side effect.
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
    assert r.status_code == 200 # delete the created project to restore to remove side effect.
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
    r = requests.post('http://localhost:4567/projects', json=new_body,
                  headers={'content-type': 'application/json'})
    time_after = time.time()
    assert r.status_code == 200
    r = requests.delete(f'http://localhost:4567/projects/{project_id}')
    assert r.status_code == 200 # delete the created project to restore to remove side effect.
    return time_after - time_before

def __get_random_string(length):
    letters = string.ascii_lowercase
    title = ''.join(random.choice(letters) for i in range(length))
    return title

# def test_categories_performance():
#     raise NotImplemented
#
#
# def test_projects_performance():
#     raise NotImplemented
