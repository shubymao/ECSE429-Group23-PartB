import pytest 
from pytest_bdd import scenarios, given, when, then, parsers

# scenarios('../features/AdjustPriority.feature')
# scenarios('../features/ChangeDescription.feature')
scenarios('../features/CreateTodoList.feature')
# scenarios('../features/RemoveTodoList.feature')

@given(parsers.parse('the system is running'))
def theSystemIsSetup():
    assert True
#  is used for indication that it's a number
@given(parsers.parse('the task with id {id} exists'))
def checkOrCreateTodo(id):
    assert True

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

@given(parsers.parse('the task with id {id} has "{priority}" priority'))
def checkOrSetTodoPriority(id,priority):
    assert True

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

@when(parsers.parse('the student change task with id {id} to "{priority}" priority'))
def changeTaskPriority(id, priority):
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

@then(parsers.parse('the priority of the task with {id} should be "{priority}"'))
def checkIfTaskHasPriority(id, priority):
    assert True

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

    