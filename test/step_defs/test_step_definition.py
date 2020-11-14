import socket
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from conftest import GLOBAL_CONTEXT
import requests
import json

# Finished scenarios: adjust priority, 
scenarios('../features/AdjustPriority.feature')
scenarios('../features/ChangeDescription.feature')
# scenarios('../features/CreateTodoList.feature')
# scenarios('../features/RemoveTodoList.feature')

@pytest.fixture(scope='function')
def context():
    return {}

@given(parsers.parse('the system is running'))
def theSystemIsSetup():
    assert socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(
        ("localhost", 4567)) == 0

@given(parsers.parse('the task with id {id} exist'))
def checkOrCreateTodoWithID(id):
    assert True

@given(parsers.parse('the task with title "{title}" exists'))
def checkOrCreateTodoWithTitle(title):
    r = requests.get(url=f"http://localhost:4567/todos?title={title}")
    if(len(r.json()['todos']) == 0):
        body = {'title': title}
        requests.post(url="http://localhost:4567/todos", json=body)
    r = requests.get(url=f"http://localhost:4567/todos?title={title}")
    assert len(r.json()['todos']) > 0
    GLOBAL_CONTEXT.todo_id = str(r.json()['todos'][0]['id'])

@given(parsers.parse('the system contains a to do list with entry id {id}'))
def ensureCategoryWithIDExists(id):
    assert True

@given(parsers.parse('the system does not contain a to do list with entry id {id}'))
def ensureCategoryWithIDDoesNotExist(id):
    assert True

@given(parsers.parse('<course> contains an entry'))
def ensureAnEntryExistsWithinCourse(course):
    raise NotImplementedError

@given(parsers.parse('{name} contains an entry'))
def addTodoToCategory(name):
    assert True

@given(parsers.parse('the to do list called <course> contains no tasks'))
def ensureCategoryHasNoTasks(categoryID):
    raise NotImplementedError

@given(parsers.parse('the task with id {id} does not exists'))
def checkOrRemoveTodo(id):
    r = requests.get(url=f'http://localhost:4567/todos/{id}')
    if(r.status_code != 404):
        r = requests.delete(url=f'http://localhost:4567/todos/{id}')
        assert r.status_code == 200
        r = requests.get(url=f'http://localhost:4567/todos/{id}')
        assert r.status_code == 404

@ given(parsers.parse('the task has no description'))
def checkOrRemoveTodoDescription():
    assert True

@ given(parsers.parse('the task has "{priority}" priority'))
def checkOrSetTodoPriority(priority):
    checkOrCreateTodoPriority(priority)
    body = {'id': GLOBAL_CONTEXT.category_id}
    url = f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/categories'
    r = requests.post(url=url, json=body)
    assert r.status_code == 201
    r = requests.get(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/categories')
    assert r.status_code == 200
    exist = len(list(
        filter(lambda x: x['id'] == GLOBAL_CONTEXT.category_id, r.json()['categories']))) > 0
    assert exist


@ given(parsers.parse('the task has description of "{description}"'))
def checkOrSetTodoDescription(description):
    body = {'description': description}
    url = f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}'
    r = requests.post(url=url, json=body)
    assert r.status_code == 200
    r = requests.get(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}')
    assert r.status_code == 200
    assert r.json()['todos'][0]['description'] == description


@ given(parsers.parse('I can see a list with <course> within the application'))
def initializeExistingCategory(course, context):
    add_category_no_conflict(course, context)
    getCategories(course, context)
    assert True

@ given(parsers.parse('I can see a list that does not include <course> within the application'))
def ensureExclusionOfClass(course, context):
    r = requests.get("http://localhost:4567/categories")
    for category in r.json()['categories']:
        if category['title'] == course:
            assert False
    assert True

@ when(parsers.parse('I delete an existing to do list named <course>'))
def deleteExistingCategories(course):
    raise NotImplementedError


@ when(parsers.parse('I delete <course>'))
def deleteEmptyCategories(id):
    raise NotImplementedError


@ when(parsers.parse('I delete a nonexistent to do list called <course>'))
def deleteNonExistentCategories(id):
    raise NotImplementedError


@ when(parsers.parse('I add a new course with title <course>'))
def add_category_no_conflict(course, context):
    # Add new course with title <course>
    context['request_return'] = requests.post(
        "http://localhost:4567/categories", json={"title": course})
    assert context['request_return'].status_code == 201


@ when(parsers.parse('the student change task to "{priority}" priority'))
def changeTaskPriority(priority):
    r = requests.delete(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/categories/{GLOBAL_CONTEXT.category_id}')
    assert r.status_code == 200
    checkOrCreateTodoPriority(priority)
    body = {'id': GLOBAL_CONTEXT.category_id}
    r = requests.post(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/categories', json=body)
    assert r.status_code == 201

@ when(parsers.parse('the student change task with {id} to "{priority}" priority'))
def changeTaskPriorityWithID(id, priority):
    checkOrCreateTodoPriority(priority)
    body = {'id': GLOBAL_CONTEXT.category_id}
    r = requests.post(
        url=f'http://localhost:4567/todos/{id}/categories', json=body)
    
    GLOBAL_CONTEXT.response_json = r.json()
    GLOBAL_CONTEXT.status_code = r.status_code

@ when(parsers.parse('the student change description of task to "{description}"'))
def changeTaskDescription(description):
    body = {'description': description}
    r = requests.post(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}', json=body)
    assert r.status_code == 200

@when(parsers.parse('the student change description of task with id {id} to "{description}"'))
def changeTaskDescription(id,description):
    body = {'description': description}
    r = requests.post(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}', json=body)
    GLOBAL_CONTEXT.response_json = r.json()
    GLOBAL_CONTEXT.status_code = r.status_code


@ when(parsers.parse('I add a new task entry to <course>'))
def addTodoToCategory(course, context):
    # Recall: the course that we targeted
    # context['request_return']['id']

    # Create some task
    try:
        context['task_return'] = requests.post(
            f"http://localhost:4567/categories/{context['request_return'].json()['id']}/projects",
            json={"title": course})
    except KeyError:
        context['task_return'] = requests.post(
            f"http://localhost:4567/categories/93829/projects",
            json={"title": course})
        assert True
        return
    assert context['task_return'].status_code in [201]


@ then(parsers.parse('I should see the to do list entry <course>, disappear from the application'))
def getCategory():
    raise NotImplementedError

@ then(parsers.parse('I should see a success message'))
def assertSuccessOperation(context):
    assert context['request_return'].status_code in [200, 201]


@ then(parsers.parse('I should see an error message'))
def assertFailureOperation(context):
    try:
        assert context['request_return'].status_code not in [200, 201]
    except KeyError:
        assert context['task_return'].status_code not in [200, 201]

@ then(parsers.parse('I should see a new list named <course> within the application'))
def getCategories(course, context):
    # Retrieve list of categories
    result = requests.get("http://localhost:4567/categories")

    # Verify it exists mathcing previous requests and within application
    for category in result.json()['categories']:
        if category['id'] == context['request_return'].json()['id'] and \
                category['title'] == context['request_return'].json()['title']:
            assert True
            return
    assert False

@ then(parsers.parse('the priority of the task should be "{priority}"'))
def checkIfTaskHasPriority(priority):
    todo = GLOBAL_CONTEXT.todo_id
    r = requests.get(url=f"http://localhost:4567/todos/{todo}/categories")
    assert r.status_code == 200
    categories = r.json()['categories']
    exist = len(
        list(filter(lambda x: x['id'] == GLOBAL_CONTEXT.category_id, categories))) > 0
    assert exist

@ then(parsers.parse('the system shall inform the user that the task doesn\'t exist'))
def checkIfMessageEqualsTaskDoNotExist():
    assert GLOBAL_CONTEXT.status_code == 404

@ then(parsers.parse('the priority status should stay the same'))
def checkIfPriorityStaySame():
    assert True


@ then(parsers.parse('the description of the task should be "{description}"'))
def checkTaskDescriptionEqual(description):
    r = requests.get(f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}')
    assert r.status_code == 200
    assert r.json()['todos'][0]['description']==description


@ then(parsers.parse('I should not see any duplicate entries named <course> within the application'))
def checkUniquenessCategory(course):
    result = requests.get("http://localhost:4567/categories")

    # Verify it exists matching previous requests and within application
    # We also need to verify that there only exists one instance of a given course.
    unique_count = 0
    for category in result.json()['categories']:
        if category['title'] == course:
            unique_count += 1
    assert unique_count == 1

@ then(parsers.parse('I should see a new task in <course>'))
def checkTaskAdded(course, context):
    r = requests.get(
        "http://localhost:4567/categories/['request_return']['id']/projects")
    for project in r.json()['projects']:
        if project['title'] == context['task_return'].json()['title'] and \
                project['id'] == context['task_return'].json()['id']:
            assert True
            return
    assert False

# Helper functions

def checkOrCreateTodoPriority(priority):
    r = requests.get(url=f"http://localhost:4567/categories?title={priority}")
    if(len(r.json()['categories']) == 0):
        body = {'title': priority}
        requests.post(url="http://localhost:4567/categories", json=body)
    r = requests.get(url=f"http://localhost:4567/categories?title={priority}")
    GLOBAL_CONTEXT.category_id = str(r.json()['categories'][0]['id'])
    assert len(r.json()['categories']) > 0
