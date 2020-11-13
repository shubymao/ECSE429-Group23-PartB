import pytest 
from pytest_bdd import scenarios, given, when, then, parsers

@given('the system is running')
def theSystemIsSetup() :

@given('the task with id {id} exists')
def checkOrCreateTodo(id):

@given('the system contains a to do list with entry id {id}')
def ensureCategoryWithIDExists(id):

@given('the system does not contain a to do list with entry id {id}')
def ensureCategoryWithIDDoesNotExist(id):

@given('entry id {categoryID} with taskID {todoID} exists')
def addTodoToCategory(categoryID, todoID):

@given('entry id {categoryID} contains no tasks')
def ensureCategoryHasNoTasks(categoryID):

@given('a to do list with id {categoryID} does not exist')
def ensureCategoryDoesNotExist(categoryID):

@given('the task with id {id} does not exists')
def checkOrRemoveTodo(id) :

@given('the task with id {id} has no description')
def checkOrRemoveTodoDescription(id) :

@given('the task with id {id} has "{priority}" priority')
def checkOrSetTodoPriority(id,priority) :

@given('the task with id {id} has description of "{description}"')
def checkOrSetTodoDescription(id, description):

@given('I can see a list with "{categoryName}" within the application')
def initializeExistingCategory(categoryName):
    
@when('I delete an existing to do list with id {id}')
def deleteExistingCategories(id) :

@when('I delete an empty to do list with id {id}')
def deleteEmptyCategories(id) :

@when('I delete a nonexistent to do list with id {id}')
def deleteNonExistentCategories(id) :

@when('I add a new course with title "{categoryName}"')
def addCategoryNoConflict(categoryName):

@when('the student change task with id {id} to "{priority}" priority')
def changeTaskPriority(id, priority) :
    
@when('the student change description of task with id {id} to "{description}"')
def changeTaskDescription(id, description):
    
@when('I add a new task entry to "{categoryName}"')
def addTodoToCategory(categoryName):
    
@then('I should see the to do list entry with id {id} disappear from the application')
def getCategory(id) :

@then('I should see a new list named "{courseName}" within the application')
def getCategories(courseName):

@then('the priority of the task with {id} should be "{priority}"')
def checkIfTaskHasPriority(id, priority) :

@then('the system shall inform the user that the task doesn\'t exist')
def checkIfMessageEqualsTaskDoNotExist() :
    
@then('the priority status should stay the same')
def checkIfPriorityStaySame():
    
@then('the description of the task with {id} should be "{description}"')
def checkTaskDescriptionEqual(id, description):

@then('I should not see any duplicate entries named "{courseName}" within the application')
def checkUniquenessCategory(courseName):

@then('I should see a new task in "{courseName}"')
def checkTaskAdded(courseName):

    