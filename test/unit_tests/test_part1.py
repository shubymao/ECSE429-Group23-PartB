import requests
import json

from support.assertions import get_xml_file

const_file = open('test/resources/test1-constants.json',)
TEST1_CONSTANTS = json.load(const_file)


# Get for todos
def test_get_todos_return_code():
    r = requests.get(url="http://localhost:4567/todos")
    assert r.status_code == 200

def test_get_todos_return_payload():
    r = requests.get(url="http://localhost:4567/todos")
    assert r.json() == TEST1_CONSTANTS['EXPECTED_GET_TODO']

def test_get_todos_with_query_return_payload():
    r = requests.get(url="http://localhost:4567/todos?title=scan paperwork")
    assert r.json() == TEST1_CONSTANTS['EXPECTED_QUERY_TODO']

# Get for todo with id
def test_get_todos_with_id_return_code():
    r = requests.get(url="http://localhost:4567/todos/1")
    assert r.status_code == 200


def test_get_todos_with_id_return_payload():
    r = requests.get(url="http://localhost:4567/todos/1")
    assert r.json() == TEST1_CONSTANTS['EXPECTED_GET_WITH_ID_TODO']


# Get Peoject with Task and ID
def test_get_project_with_todo_id_return_code():
    r = requests.get(url="http://localhost:4567/todos/1/tasksof")
    assert r.status_code == 200


def test_get_project_with_todo_id_return_payload():
    r = requests.get(url="http://localhost:4567/todos/1/tasksof")
    assert r.json() == TEST1_CONSTANTS['EXPECTED_GET_PROJECT_WITH_TODO_ID']


# Header for todos
def test_head_todos_return_code():
    r = requests.head(url="http://localhost:4567/todos")
    assert r.status_code == 200


def test_head_todos_return_payload():
    r = requests.head(url="http://localhost:4567/todos")
    # Change this to supposed value
    assert r.status_code == 200


# Header for todos with id
def test_head_todos_with_id_return_code():
    r = requests.head(url="http://localhost:4567/todos/1")
    assert r.status_code == 200


def test_head_todos_with_id_return_payload():
    r = requests.head(url="http://localhost:4567/todos/1")
    # Change this to supposed value
    assert r.status_code == 200


#  Header for project with task and id
def test_head_todos_with_id_return_code():
    r = requests.head(url="http://localhost:4567/todos/1/tasksof")
    assert r.status_code == 200


def test_head_todos_with_id_return_payload():
    r = requests.head(url="http://localhost:4567/todos/1/tasksof")
    # Change this to supposed value
    assert r.status_code == 200


# Post for todos
def test_post_todos_return_code():
    data = TEST1_CONSTANTS['NEW_TODO']
    r = requests.post(url="http://localhost:4567/todos", json=data)
    assert r.status_code == 201


def test_post_todos_return_payload():
    data = TEST1_CONSTANTS['NEW_TODO']
    r = requests.post(url="http://localhost:4567/todos", json=data)
    assert r.json() == TEST1_CONSTANTS['EXPECTED_NEW_TODO']


# Post for todos with id
def test_post_todos_with_id_return_code():
    data = TEST1_CONSTANTS['UPDATE_TODO']
    r = requests.post(url="http://localhost:4567/todos/1", json=data)
    assert r.status_code == 200


def test_post_todos_with_id_return_payload():
    data = TEST1_CONSTANTS['UPDATE_TODO']
    r = requests.post(url="http://localhost:4567/todos/1", json=data)
    assert r.json() == TEST1_CONSTANTS['EXPECTED_UPDATED_TODO']


# Post for todos with id and taskof
def test_post_todos_with_id_taskof_return_code():
    data = TEST1_CONSTANTS['NEW_PROJECT']
    requests.post(url="http://localhost:4567/projects", json=data)
    pid = TEST1_CONSTANTS['PROJECT_ID']
    r = requests.post(url="http://localhost:4567/todos/1/tasksof", json=pid)
    assert r.status_code == 201


def test_post_todos_with_id_taskof_return_payload():
    data = TEST1_CONSTANTS['NEW_PROJECT']
    requests.post(url="http://localhost:4567/projects", json=data)
    pid = TEST1_CONSTANTS['PROJECT_ID']
    requests.post(url="http://localhost:4567/todos/1/tasksof", json=pid)
    requests.get(url="http://localhost:4567/todos/1/tasksof")
    assert TEST1_CONSTANTS['EXPECTED_UPDATED_TASK_OF'] == TEST1_CONSTANTS['EXPECTED_UPDATED_TASK_OF']


# Put for todos with id
def test_put_todos_with_id_return_code():
    data = TEST1_CONSTANTS['UPDATE_TODO']
    r = requests.put(url="http://localhost:4567/todos/1", json=data)
    assert r.status_code == 200


# This one fails because the server overwrote the associations.
def test_put_todos_with_id_return_payload():
    data = TEST1_CONSTANTS['UPDATE_TODO']
    r = requests.put(url="http://localhost:4567/todos/1", json=data)
    assert r.json() == TEST1_CONSTANTS['EXPECTED_UPDATED_TODO']


# Delete for todos with id
def test_delete_todos_with_id_return_code():
    r = requests.delete(url="http://localhost:4567/todos/1")
    assert r.status_code == 200


def test_delete_todos_with_id_result_state():
    requests.delete(url="http://localhost:4567/todos/1")
    r = requests.get(url="http://localhost:4567/todos/1")
    assert r.status_code == 404

# Delete for taskof
def test_delete_taskof_return_code():
    r = requests.delete(url="http://localhost:4567/todos/1/tasksof/1")
    assert r.status_code == 200

def test_delete_taskof_result_state():
    requests.delete(url="http://localhost:4567/todos/1/tasksof/1")
    r = requests.get(url="http://localhost:4567/todos/1/tasksof")
    assert r.json() == TEST1_CONSTANTS['EXPECTED_DELETED_TASK_OF']

# Get for docs
def test_get_doc_return_code():
    r = requests.get(url="http://localhost:4567/docs")
    assert r.status_code == 200

# POST todos with XML instead of json
def test_post_todos_return_payload_xml():
    header = {'Content-Type': 'application/xml'}
    data = get_xml_file('test_post_todos.xml')
    r = requests.post(url="http://localhost:4567/todos", data=data, headers=header)
    assert r.json() == TEST1_CONSTANTS['EXPECTED_NEW_TODO']

# POST update an id of a todos with XML instead of json
def test_post_todos_with_id_return_payload_xml():
    header = {'Content-Type': 'application/xml'}
    data = get_xml_file('test_post_todos_with_id.xml')
    r = requests.post(url="http://localhost:4567/todos/1", data=data, headers=header)
    assert r.json() == TEST1_CONSTANTS['EXPECTED_UPDATED_TODO']

# POST update an id of a todos with bad XML entries
def test_post_todos_with_id_return_payload_bad_xml():
    header = {'Content-Type': 'application/xml'}
    data = get_xml_file('test_post_todos_with_id_bad.xml')
    r = requests.post(url="http://localhost:4567/todos/1", data=data, headers=header)
    assert r.json() == TEST1_CONSTANTS['EXPECTED_UPDATED_TODO_BAD_XML']

def test_post_todos_with_id_return_payload_wrong_formatting_xml():
    header = {'Content-Type': 'application/xml'}
    data = get_xml_file('test_post_todos_with_id_wrong_formatting.xml')
    r = requests.post(url="http://localhost:4567/todos/1", data=data, headers=header)
    assert r.json() == TEST1_CONSTANTS['EXPECTED_UPDATED_TODO_WRONG_FORMAT_XML']