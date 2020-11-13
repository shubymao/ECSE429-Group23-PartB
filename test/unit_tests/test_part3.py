import requests
import json
import pytest
from operator import attrgetter


const_file = open('test/resources/test3-constants.json',)
TEST3_CONSTANTS = json.load(const_file)
baseUrl = "http://localhost:4567"
# GET /todos/:id/categories
URL_TODOS_CATEGORY = baseUrl + "/todos/1/categories"
def test_get_todos_with_id_categories_return_code():
    r = requests.get(url=URL_TODOS_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']

def test_get_todos_with_id_categories_return_payload():
    r = requests.get(url=URL_TODOS_CATEGORY)
    response, expected = json.dumps(r.json(), sort_keys=True), json.dumps(TEST3_CONSTANTS['EXPECTED_GET_TODOS_WITH_ID_CATEGORY'], sort_keys=True)
    assert response == expected 

# HEAD /todos/:id/categories
def test_head_todos_with_id_categories_return_code():
    r = requests.head(url=URL_TODOS_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']
def test_head_todos_with_id_categories_return_payload():
    r = requests.head(url=URL_TODOS_CATEGORY)
    try:
        r.json()
    except json.decoder.JSONDecodeError:
        assert True
        return
    assert False
# POST /todos/:id/categories
body = TEST3_CONSTANTS['NEW_TODOS_CATEGORY']
def test_post_todos_with_id_categories_return_code():
    r = requests.post(url=URL_TODOS_CATEGORY, json=body)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_201']
def test_post_todos_with_id_categories_return_payload():
    r = requests.post(url=URL_TODOS_CATEGORY, json=body)
    response, expected = json.dumps(r.json(), sort_keys=True), json.dumps(TEST3_CONSTANTS['EXPECTED_NEW_TODOS_CATEGORY'], sort_keys=True)
    assert response == expected 

# DELETE /todos/:id/categories/:id
def test_delete_todos_with_id_categories_return_code():
    body={"id": 1}
    r = requests.delete(url=URL_TODOS_CATEGORY, json=body)
    """ 
    This delete method from the exploration testing return a 405(method not allowed error). 
    when we send a DELETE request witb url = http://localhost:4567/todos/:id/categories 
    and body: {"id": 1}; which is the intended behavior. To actaully delete you will need 
    to send a delete request for the todos with url = http://localhost:4567/todos/1
    """
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_405']

def test_delete_todos_with_id_categories_return_state():
    body={"id": 1}
    """
    Since delete method is not allowed. Assert that after deleting object should still exist.
    """
    requests.delete(url=URL_TODOS_CATEGORY, json=body)
    r = requests.get(url=URL_TODOS_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']
# GET /projects/:id/categories
URL_PROJECTS_CATEGORY = baseUrl + "/projects/1/categories"
def test_get_projects_with_id_categories_return_code():
    r = requests.get(url=URL_PROJECTS_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']

def test_get_projects_with_id_categories_return_payload():
    r = requests.get(url=URL_PROJECTS_CATEGORY)
    response, expected = json.dumps(r.json(), sort_keys=True), json.dumps(TEST3_CONSTANTS['EXPECTED_GET_PROJECTS_WITH_ID_CATEGORY'], sort_keys=True)
    assert response == expected 
# HEAD /projects/:id/categories
def test_head_projects_with_id_categories_return_code():
    r = requests.head(url=URL_PROJECTS_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']
def test_head_projects_with_id_categories_return_payload():
    r = requests.head(url=URL_PROJECTS_CATEGORY)
    try:
        r.json()
    except json.decoder.JSONDecodeError:
        assert True
        return
    assert False
# POST /projects/:id/categories
def test_post_projects_with_id_categories_return_code():
    data = TEST3_CONSTANTS['NEW_PROJECT']
    requests.post(url="http://localhost:4567/projects", json=data)
    pid = TEST3_CONSTANTS['PROJECT_ID']
    r = requests.post(URL_PROJECTS_CATEGORY, json=pid)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_201']
def test_post_projects_with_id_categories_return_payload():
    data = TEST3_CONSTANTS['NEW_PROJECT']
    requests.post(url="http://localhost:4567/projects", json=data)
    pid = TEST3_CONSTANTS['PROJECT_ID']
    requests.post(URL_PROJECTS_CATEGORY, json=pid)
    r =  requests.get(URL_PROJECTS_CATEGORY)
    response, expected = json.dumps(r.json(), sort_keys=True), json.dumps(TEST3_CONSTANTS['EXPECTED_NEW_PROJECTS_CATEGORY'], sort_keys=True)
    assert response == expected 
# DELETE /projects/:id/categories/:id
def test_delete_projects_with_id_categories_return_code():
    body={"id": 1}
    r = requests.delete(url=URL_PROJECTS_CATEGORY, json=body)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_405']

def test_delete_projects_with_id_categories_return_state():
    body={"id": 1}
    requests.delete(url=URL_PROJECTS_CATEGORY, json=body)
    r = requests.get(url=URL_PROJECTS_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']
# GET /categories
URL_CATEGORY = baseUrl + "/categories"
def test_get_categories_return_code():
    r = requests.get(url=URL_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']

def test_get_categories_return_payload():
    r = requests.get(url=URL_CATEGORY)
    r.json()['categories'].sort(key = lambda x: x['id'], reverse = True)
    print(r.json()['categories'])
    TEST3_CONSTANTS['EXPECTED_GET_CATEGORY']['categories'].sort(key = lambda x: x['id'], reverse = True)
    print(TEST3_CONSTANTS['EXPECTED_GET_CATEGORY']['categories'])
    assert r.json() == TEST3_CONSTANTS['EXPECTED_GET_CATEGORY']
# HEAD /categories
def test_head_categories_return_code():
    r = requests.head(url=URL_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']
def test_head_categories_return_payload():
    r = requests.head(url=URL_CATEGORY)
    try:
        r.json()
    except json.decoder.JSONDecodeError:
        assert True
        return
    assert False
# POST /categories
def test_post_categories_return_code():
    data = TEST3_CONSTANTS['NEW_CATEGORY']
    r = requests.post(url=URL_CATEGORY, json=data)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_201']
def test_post_categories_return_payload():
    data = TEST3_CONSTANTS['NEW_CATEGORY']
    requests.post(url=URL_CATEGORY, json=data)
    getCreatedCategory  = baseUrl + "/categories/3"
    r =  requests.get(url=getCreatedCategory)
    response, expected = json.dumps(r.json(), sort_keys=True), json.dumps(TEST3_CONSTANTS['EXPECTED_NEW_CATEGORY'], sort_keys=True)
    assert response == expected 
# GET /categories/:id
URL_GET_CATEGORY = baseUrl + "/categories/1"
def test_get_categories_with_id_return_code():
    r = requests.get(url=URL_GET_CATEGORY)
    assert r.status_code == TEST3_CONSTANTS['EXPECTED_STATUS_CODE_200']

def test_get_categories_with_id_return_payload():
    r = requests.get(url=URL_GET_CATEGORY)
    response, expected = json.dumps(r.json(), sort_keys=True), json.dumps(TEST3_CONSTANTS['EXPECTED_GET_CATEGORY_ID'], sort_keys=True)
    assert response == expected 
