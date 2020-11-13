import pytest 
from pytest_bdd import scenarios, given, when, then, parsers

    @Given('the system is running')
    def theSystemIsSetup() :

    @Given('the task with id {id} exists')
    def checkOrCreateTodo(id) :

    @Given('the system contains a to do list with entry id {id}')
    def ensureCategoryWithIDExists(id):

    @Given('the system does not contain a to do list with entry id {id}')
    def ensureCategoryWithIDDoesNotExist(id):

    @Given('entry id {categoryID} with taskID {todoID} exists')
    def addTodoToCategory(categoryID, todoID):

    @Given('entry id {categoryID} contains no tasks')
    def ensureCategoryHasNoTasks(categoryID):

    @Given('a to do list with id {categoryID} does not exist')
    def ensureCategoryDoesNotExist(categoryID):

    @Given('the task with id {id} does not exists')
    def checkOrRemoveTodo(id) :

    @Given('the task with id {id} has no description')
    def checkOrRemoveTodoDescription(id) :

    @Given('the task with id {id} has {priority} priority')
    def checkOrSetTodoPriority(id,priority) :

    @Given('the task with id {id} has description of {description}')
    def checkOrSetTodoDescription(id, description):

    @Given('I can see a list with {categoryName} within the application')
    def initializeExistingCategory(categoryName):
    
    @When('I delete an existing to do list with id {id}')
    def deleteExistingCategories(id) :

    @When('I delete an empty to do list with id {id}')
    def deleteEmptyCategories(id) :

    @When('I delete a nonexistent to do list with id {id}')
    def deleteNonExistentCategories(id) :

    @When('I add a new course with title {categoryName}')
    def addCategoryNoConflict(categoryName):

    @When('the student change task with id {id} to {priority} priority')
    def changeTaskPriority(id, priority) :
    
    @When('the student change description of task with id {id} to {description}')
    def changeTaskDescription(id, description):
    
    @When('I add a new task entry to {categoryName}')
    def addTodoToCategory(categoryName):
    
    @Then('I should see the to do list entry with id {id} disappear from the application')
    def getCategory(id) :

    @Then('I should see a new list named {courseName} within the application')
    def getCategories(courseName):

    @Then('the priority of the task with {id} should be {priority}')
    def checkIfTaskHasPriority(id, priority) :

    @Then('the system shall inform the user that the task doesn\'t exist')
    def checkIfMessageEqualsTaskDoNotExist() :
    
    @Then('the priority status should stay the same')
    def checkIfPriorityStaySame():
    
    @Then('the description of the task with {id} should be {description}')
    def checkTaskDescriptionEqual(id, description):

    @Then('I should not see any duplicate entries named {courseName} within the application')
    def checkUniquenessCategory(courseName):

    @Then('I should see a new task in {courseName}')
    def checkTaskAdded(courseName):

    