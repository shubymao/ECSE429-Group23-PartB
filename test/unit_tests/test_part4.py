import requests
import json
import pytest

const_file = open('test/resources/test4-constants.json',)
TEST4_CONSTANTS = json.load(const_file)

# Tests for HEAD /categories/:id
def test_head_categories_return_code():
    r = requests.head(url="http://localhost:4567/categories/1")
    assert r.status_code == 200
def test_head_categories_return_payload():
    r = requests.head(url="http://localhost:4567/categories/1")
    try:
        r.json()
    except json.decoder.JSONDecodeError:
        assert True
        return
    assert False

# Tests for POST /categories/:id
def test_post_categories_return_code():
    data = TEST4_CONSTANTS['UPDATE_CATEGORIES']
    r = requests.post(url="http://localhost:4567/categories/1", json=data)
    assert r.status_code == 200

def test_post_categories_return_payload():
    data = TEST4_CONSTANTS['UPDATE_CATEGORIES']
    r = requests.post(url="http://localhost:4567/categories/1", json=data)
    assert r.json() == TEST4_CONSTANTS['EXPECTED_CATEGORIES']

#PUT /categories/:id
def test_put_categories_return_code():
    data = TEST4_CONSTANTS['UPDATE_PUT_CATEGORIES']
    r = requests.put(url="http://localhost:4567/categories/1", json=data)
    assert r.status_code == 200
def test_put_categories_return_payload():
    data = TEST4_CONSTANTS['UPDATE_PUT_CATEGORIES']
    r = requests.put(url="http://localhost:4567/categories/1", json=data)
    assert r.json() == TEST4_CONSTANTS['EXPECTED_PUT_CATEGORIES']

#Tests for DELETE /categories/:id/
def test_delete_categories_return_code():
    r = requests.delete(url="http://localhost:4567/categories/2")
    assert r.status_code == 200
def test_delete_categories_return_payload():
    r = requests.delete(url="http://localhost:4567/categories/2")
    r2 = requests.get(url="http://localhost:4567/categories/2")
    assert r2.status_code == 404

#GET /categories/:id/todos
def test_get_categories_todos_return_code():
    r = requests.get(url="http://localhost:4567/categories/1/todos")
    assert r.status_code == 200
def test_get_categories_todos_return_payload():
    r = requests.get(url="http://localhost:4567/categories/1/todos")
    assert r.json() == TEST4_CONSTANTS['EXPECTED_GET_CATEGORIES_TODOS']

# Tests for HEAD /categories/:id/todos
def test_head_categories_todos_return_code():
    r = requests.head(url="http://localhost:4567/categories/1/todos")
    assert r.status_code == 200
def test_head_categories_todos_return_payload():
    r = requests.head(url="http://localhost:4567/categories/1/todos")
    try:
        r.json()
    except json.decoder.JSONDecodeError:
        assert True
        return
    assert False

# Tests for POST /categories/:id/todos
def test_post_categories_todos_return_code():
    data = TEST4_CONSTANTS['UPDATE_CATEGORIES_TODOS']
    r = requests.post(url="http://localhost:4567/categories/1/todos", json=data)
    assert r.status_code == 201
def test_post_categories_todos_return_payload():
    data = TEST4_CONSTANTS['UPDATE_CATEGORIES_TODOS']
    r = requests.post(url="http://localhost:4567/categories/1/todos", json=data)
    assert r.json() == TEST4_CONSTANTS['EXPECTED_CATEGORIES_TODOS']


#Tests for DELETE /categories/:id/todos/:id
def test_delete_categories_todos_return_code():
    data = TEST4_CONSTANTS['NEW_DELETE_ID']
    r0 = requests.post(url="http://localhost:4567/categories/1/todos", json=data)
    r1 = requests.delete(url="http://localhost:4567/categories/1/todos/1")
    assert r1.status_code == 200
def test_delete_categories_todos_return_payload():
    data = TEST4_CONSTANTS['NEW_DELETE_ID']
    r0 = requests.post(url="http://localhost:4567/categories/1/todos", json=data)
    r1 = requests.delete(url="http://localhost:4567/categories/1/todos/1")
    r2 = requests.get(url="http://localhost:4567/categories/1/todos/1")
    assert r2.status_code == 404

#GET /categories/:id/projects
def test_get_categories_projects_return_code():
    r = requests.get(url="http://localhost:4567/categories/1/projects")
    assert r.status_code == 200

def test_get_categories__projects_return_payload():
    r = requests.get(url="http://localhost:4567/categories/1/projects")
    assert r.json() == TEST4_CONSTANTS['EXPECTED_GET_CATEGORIES_PROJECTS']

# Tests for HEAD /categories/:id/projects
def test_head_categories_projects_return_code():
    r = requests.head(url="http://localhost:4567/categories/1/projects")
    assert r.status_code == 200
def test_head_categories_projects_return_payload():
    r = requests.head(url="http://localhost:4567/categories/1/projects")
    try:
        r.json()
    except json.decoder.JSONDecodeError:
        assert True
        return
    assert False

# POST /categories/:id/projects
def test_post_categories_projects_return_code():
    data = TEST4_CONSTANTS['UPDATE_CATEGORIES_PROJECTS']
    r = requests.post(url="http://localhost:4567/categories/1/projects", json=data)
    assert r.status_code == 201
def test_post_categories_projects_return_payload():
    data = TEST4_CONSTANTS['UPDATE_CATEGORIES_PROJECTS']
    r = requests.post(url="http://localhost:4567/categories/1/projects", json=data)
    assert r.json() == TEST4_CONSTANTS['EXPECTED_CATEGORIES_PROJECTS']

#Tests for DELETE /categories/:id/projects/:id
def test_delete_categories_todos_projects_return_code():
    data = TEST4_CONSTANTS['NEW_DELETE_ID']
    r0 = requests.post(url="http://localhost:4567/categories/1/projects", json=data)
    r1 = requests.delete(url="http://localhost:4567/categories/1/projects/1")
    assert r1.status_code == 200
def test_delete_categories_todos_projects_return_payload():
    data = TEST4_CONSTANTS['NEW_DELETE_ID']
    r0 = requests.post(url="http://localhost:4567/categories/1/projects", json=data)
    r1 = requests.delete(url="http://localhost:4567/categories/1/projects/1")
    r2 = requests.get(url="http://localhost:4567/categories/1/projects/1")
    assert r2.status_code == 404


