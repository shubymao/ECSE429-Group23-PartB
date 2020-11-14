import socket
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import requests

# scenarios('../features/AdjustPriority.feature')
# scenarios('../features/ChangeDescription.feature')
scenarios('../features/CreateTodoList.feature')


# scenarios('../features/RemoveTodoList.feature')

@pytest.fixture(scope='function')
def context():
    return {}


@given(parsers.parse('the system is running'))
def the_system_is_set_up():
    assert socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(("localhost", 4567)) == 0


@given(parsers.parse('the task with id {id} exists'))
def checkOrCreateTodo(id):
    assert True


@given(parsers.parse('the system contains a to do list named <name>'))
def ensureCategoryWithIDExists(name):
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
    assert True


@given(parsers.parse('the task with id {id} has no description'))
def checkOrRemoveTodoDescription(id):
    assert True


@given(parsers.parse('the task with id {id} has "{priority}" priority'))
def checkOrSetTodoPriority(id, priority):
    assert True


@given(parsers.parse('the task with id {id} has description of "{description}"'))
def checkOrSetTodoDescription(id, description):
    assert True


@given(parsers.parse('I can see a list with <course> within the application'))
def initializeExistingCategory(course, context):
    add_category_no_conflict(course, context)
    getCategories(course, context)
    assert True

@given(parsers.parse('I can see a list that does not include <course> within the application'))
def ensureExclusionOfClass(course, context):
    r = requests.get("http://localhost:4567/categories")
    for category in r.json()['categories']:
        if category['title'] == course:
            assert False
    assert True

@when(parsers.parse('I delete an existing to do list named <course>'))
def deleteExistingCategories(course):
    raise NotImplementedError


@when(parsers.parse('I delete <course>'))
def deleteEmptyCategories(id):
    raise NotImplementedError


@when(parsers.parse('I delete a nonexistent to do list called <course>'))
def deleteNonExistentCategories(id):
    raise NotImplementedError


@when(parsers.parse('I add a new course with title <course>'))
def add_category_no_conflict(course, context):
    # Add new course with title <course>
    context['request_return'] = requests.post("http://localhost:4567/categories", json={"title": course})
    assert context['request_return'].status_code == 201


@when(parsers.parse('the student change task with id {id} to "{priority}" priority'))
def changeTaskPriority(id, priority):
    assert True


@when(parsers.parse('the student change description of task with id {id} to "{description}"'))
def changeTaskDescription(id, description):
    assert True


@when(parsers.parse('I add a new task entry to <course>'))
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


@then(parsers.parse('I should see the to do list entry <course>, disappear from the application'))
def getCategory():
    raise NotImplementedError


@then(parsers.parse('I should see a success message'))
def assertSuccessOperation(context):
    assert context['request_return'].status_code in [200, 201]


@then(parsers.parse('I should see an error message'))
def assertFailureOperation(context):
    try:
        assert context['request_return'].status_code not in [200, 201]
    except KeyError:
        assert context['task_return'].status_code not in [200, 201]

@then(parsers.parse('I should see a new list named <course> within the application'))
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


@then(parsers.parse('I should not see any duplicate entries named <course> within the application'))
def checkUniquenessCategory(course):
    result = requests.get("http://localhost:4567/categories")

    # Verify it exists matching previous requests and within application
    # We also need to verify that there only exists one instance of a given course.
    unique_count = 0
    for category in result.json()['categories']:
        if category['title'] == course:
            unique_count += 1
    assert unique_count == 1


@then(parsers.parse('I should see a new task in <course>'))
def checkTaskAdded(course, context):
    r = requests.get("http://localhost:4567/categories/['request_return']['id']/projects")
    for project in r.json()['projects']:
        if project['title'] == context['task_return'].json()['title'] and \
                project['id'] == context['task_return'].json()['id']:
            assert True
            return
    assert False
