import pytest 
from pytest_bdd import scenarios, given, when, then, parsers
from conftest import GLOBAL_ID
import requests
import json


scenarios('../features/AdjustPriority.feature')
# scenarios('../features/ChangeDescription.feature')
# scenarios('../features/CreateTodoList.feature')
# scenarios('../features/RemoveTodoList.feature')

@given(parsers.parse('the system is running'))
def theSystemIsSetup():
    r = requests.get(url="http://localhost:4567/todos")
    assert r.status_code == 200

@given(parsers.parse('the task with id {id} exist'))
def checkOrCreateTodoWithID(id):
    assert True

@given(parsers.parse('the task with title "{title}" exists'))
def checkOrCreateTodoWithTitle(title):
    r = requests.get(url= f"http://localhost:4567/todos?title={title}")
    if(len(r.json()['todos']) == 0):
        body = {'title': title}
        requests.post(url="http://localhost:4567/todos", json=body)
    r = requests.get(url= f"http://localhost:4567/todos?title={title}")
    assert len(r.json()['todos'])>0
    GLOBAL_ID.todoId = str(r.json()['todos'][0]['id'])

@given(parsers.parse('the system contains a to do list with entry id {id}'))
def ensureCategoryWithIDExists(id):
    assert True

@given(parsers.parse('the system does not contain a to do list with entry id {id}'))
def ensureCategoryWithIDDoesNotExist(id):
    assert True

@given(parsers.parse('entry id {categoryID} with taskID {todoID} exists'))
def addTodoToCategory(categoryID, todoID):
    assert True

@given(parsers.parse('entry id {categoryID} contains no tasks'))
def ensureCategoryHasNoTasks(categoryID):
    assert True

@given(parsers.parse('a to do list with id {categoryID} does not exist'))
def ensureCategoryDoesNotExist(categoryID):
    assert True

@given(parsers.parse('the task with id {id} does not exists'))
def checkOrRemoveTodo(id):
    assert True

@given(parsers.parse('the task with id {id} has no description'))
def checkOrRemoveTodoDescription(id):
    assert True

@given(parsers.parse('the task has "{priority}" priority'))
def checkOrSetTodoPriority(priority):
    checkOrCreateTodoPriority(priority)
    body = {'id' : GLOBAL_ID.categoryId}
    url = f'http://localhost:4567/todos/{GLOBAL_ID.todoId}/categories'
    print("URL = " + url)
    r = requests.post(url=url, json=body)
    assert r.status_code == 201
    r = requests.get(url = f'http://localhost:4567/todos/{GLOBAL_ID.todoId}/categories')
    assert r.status_code == 200
    exist = len(list(filter(lambda x: x['id'] == GLOBAL_ID.categoryId, r.json()['categories']))) > 0
    assert exist
    

@given(parsers.parse('the task with id {id} has description of "{description}"'))
def checkOrSetTodoDescription(id, description):
    assert True

@given(parsers.parse('I can see a list with "{categoryName}" within the application'))
def initializeExistingCategory(categoryName):
    assert True
    
@when(parsers.parse('I delete an existing to do list with id {id}'))
def deleteExistingCategories(id):
    assert True

@when(parsers.parse('I delete an empty to do list with id {id}'))
def deleteEmptyCategories(id):
    assert True

@when(parsers.parse('I delete a nonexistent to do list with id {id}'))
def deleteNonExistentCategories(id):
    assert True

@when(parsers.parse('I add a new course with title "{categoryName}"'))
def addCategoryNoConflict(categoryName):
    assert True

@when(parsers.parse('the student change task to "{priority}" priority'))
def changeTaskPriority(priority):
    todo = GLOBAL_ID.todoId
    category = GLOBAL_ID.categoryId
    print(f"Category: {category}")
    print(f"todo: {todo}")
    r = requests.delete(url = f'http://localhost:4567/todos/{todo}/categories/{category}')
    assert r.status_code == 200
    checkOrCreateTodoPriority(priority)
    category = GLOBAL_ID.categoryId
    body = { 'id' : category }
    r = requests.post(url=f'http://localhost:4567/todos/{todo}/categories', json=body)
    assert r.status_code == 201

@when(parsers.parse('the student change task with {id} to "{priority}" priority'))
def changeTaskPriorityWithID(id,priority):
    assert True
    
@when(parsers.parse('the student change description of task with id {id} to "{description}"'))
def changeTaskDescription(id, description):
    assert True
    
@when(parsers.parse('I add a new task entry to "{categoryName}"'))
def addTodoToCategory(categoryName):
    assert True
    
@then(parsers.parse('I should see the to do list entry with id {id} disappear from the application'))
def getCategory(id):
    assert True

@then(parsers.parse('I should see a new list named "{courseName}" within the application'))
def getCategories(courseName):
    assert True

@then(parsers.parse('the priority of the task should be "{priority}"'))
def checkIfTaskHasPriority(priority):
    todo = GLOBAL_ID.todoId
    r = requests.get(url = f"http://localhost:4567/todos/{todo}/categories")
    assert r.status_code == 200
    categories = r.json()['categories']
    exist = len(list(filter (lambda x : x['id'] == GLOBAL_ID.categoryId, categories))) > 0
    assert exist

@then(parsers.parse('the system shall inform the user that the task doesn\'t exist'))
def checkIfMessageEqualsTaskDoNotExist():
    assert True
    
@then(parsers.parse('the priority status should stay the same'))
def checkIfPriorityStaySame():
    assert True
    
@then(parsers.parse('the description of the task with {id} should be "{description}"'))
def checkTaskDescriptionEqual(id, description):
    assert True

@then(parsers.parse('I should not see any duplicate entries named "{courseName}" within the application'))
def checkUniquenessCategory(courseName):
    assert True

@then(parsers.parse('I should see a new task in "{courseName}"'))
def checkTaskAdded(courseName):
    assert True

# Helper functions

def checkOrCreateTodoPriority(priority):
    r = requests.get(url= f"http://localhost:4567/categories?title={priority}")
    if(len(r.json()['categories']) == 0):
        body = {'title': priority}
        requests.post(url="http://localhost:4567/categories", json=body)
    r = requests.get(url= f"http://localhost:4567/categories?title={priority}")
    GLOBAL_ID.categoryId = str(r.json()['categories'][0]['id'])
    assert len(r.json()['categories'])>0