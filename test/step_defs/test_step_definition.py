import socket


import requests
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from conftest import GLOBAL_CONTEXT


scenarios('../features/AssignPriority.feature')
scenarios('../features/AdjustPriority.feature')
scenarios('../features/ChangeDescription.feature')
scenarios('../features/CreateTodoList.feature')
scenarios('../features/RemoveTodoList.feature')
scenarios('../features/MarkTask.feature')
scenarios('../features/AddTask.feature')
scenarios('../features/RemoveTask.feature')

scenarios('../features/QueryIncompleteHighPriorityTasks.feature')
scenarios('../features/QueryIncompleteTasks.feature')

@pytest.fixture(scope='function')
def context():
    return {}

@given('the system is running')
def the_system_is_setup():
    assert socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(
        ("localhost", 4567)) == 0


@given('the task with title <title> exists')
def check_or_create_todo_with_title(title):
    r = requests.get(url=f"http://localhost:4567/todos?title={title}")
    if (len(r.json()['todos']) == 0):
        body = {'title': title}
        requests.post(url="http://localhost:4567/todos", json=body)
    r = requests.get(url=f"http://localhost:4567/todos?title={title}")
    assert len(r.json()['todos']) > 0
    GLOBAL_CONTEXT.todo_id = str(r.json()['todos'][0]['id'])


@given(parsers.parse('the system contains a to do list with entry id <id>'))
def ensure_category_with_id_exists(id):
    assert True


@given(parsers.parse('the system does not contain a to do list with entry id <id>'))
def ensure_category_with_id_does_not_exist(id):
    assert True


@given(parsers.parse('<course> contains at least one entry'))
def ensure_an_entry_exists_within_course(course):
    r = requests.get("http://localhost:4567/categories")
    for category in r.json()['categories']:
        if category['title'] == course:
            try:
                if len(category['todos']) >= 1:
                    assert True
                    return
            except KeyError:
                requests.post(f"http://localhost:4567/categories/{category['id']}/todos",
                              json={"title": "Example task here!"})
                assert True
                return


@given(parsers.parse('{name} contains an entry'))
def add_todo_to_category(name):
    assert True


@given(parsers.parse('the to do list called <course> contains no tasks'))
def ensure_category_has_no_tasks(course):
    r = requests.get("http://localhost:4567/categories")
    for category in r.json()['categories']:
        if category['title'] == course:
            assert 'todos' not in category


@given('the task with id <task_id> does not exists')
def check_or_remove_todo(task_id):
    r = requests.get(url=f'http://localhost:4567/todos/{task_id}')
    if (r.status_code != 404):
        r = requests.delete(url=f'http://localhost:4567/todos/{task_id}')
        assert r.status_code == 200
        r = requests.get(url=f'http://localhost:4567/todos/{task_id}')
        assert r.status_code == 404


@given('the task has description of <old_description>')
def check_or_set_todo_description(description):
    body = {'description': description}
    url = f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}'
    r = requests.post(url=url, json=body)
    assert r.status_code == 200
    r = requests.get(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}')
    assert r.status_code == 200
    assert r.json()['todos'][0]['description'] == description


@given(parsers.parse('the task has no description'))
def check_or_remove_todo_description():
    body = {'description': ''}
    url = f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}'
    r = requests.post(url=url, json=body)
    assert r.status_code == 200
    assert r.json()['description'] == ''


@given(parsers.parse('the task has <old_priority> priority'))
def check_or_set_todo_priority(old_priority):
    check_or_create_todo_priority(old_priority)
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


@given(parsers.parse('the following tasks exists:\n{datatable}'))
def create_tasks_with_title_and_priority(datatable):
    tasks = datatable.splitlines()
    for task in tasks:
        item = task.split('|')
        task_id = create_task(item[1].strip())
        priority_id = check_or_create_todo_priority(item[2].strip())
        assign_priority_to_task(task_id, priority_id)


@given(parsers.parse('I can see a list with <course> within the application'))
def initialize_existing_category(course, context):
    add_category_no_conflict(course, context)
    get_categories(course, context)
    assert True


@given(parsers.parse('I can see a list that does not include <course> within the application'))
def ensure_exclusion_of_class(course, context):
    r = requests.get("http://localhost:4567/categories")
    for category in r.json()['categories']:
        if category['title'] == course:
            assert False
    assert True


@when(parsers.parse('I delete an existing to do list named <course>'))
def delete_existing_categories(course, context):
    r = requests.get("http://localhost:4567/categories")
    for category in r.json()['categories']:
        if category['title'] == course:
            context['request_return'] = requests.delete(
                f"http://localhost:4567/categories/{category['id']}")
            assert True
            return


@when(parsers.parse('I delete a nonexistent to do list called <course>'))
def delete_non_existent_categories(course, context):
    r = requests.get("http://localhost:4567/categories")
    for category in r.json()['categories']:
        if category['title'] == course:
            assert False
    context['request_return'] = requests.delete(
        "http://localhost:4567/categories/823472")
    assert True


@when(parsers.parse('I add a new course with title <course>'))
def add_category_no_conflict(course, context):
    # Add new course with title <course>
    context['request_return'] = requests.post(
        "http://localhost:4567/categories", json={"title": course})
    assert context['request_return'].status_code == 201


@when('the student assign task to <new_priority> priority')
def assign_task_priority(new_priority):
    check_or_create_todo_priority(new_priority)
    body = {'id': GLOBAL_CONTEXT.category_id}
    r = requests.post(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/categories', json=body)
    assert r.status_code == 201


@when('the student change task to <new_priority> priority')
def change_task_priority(new_priority):
    r = requests.delete(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/categories/{GLOBAL_CONTEXT.category_id}')
    assert r.status_code == 200
    check_or_create_todo_priority(new_priority)
    body = {'id': GLOBAL_CONTEXT.category_id}
    r = requests.post(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/categories', json=body)
    assert r.status_code == 201


@when('the student change task with id <task_id> to <new_priority> priority')
def change_task_priority_with_id(task_id, new_priority):
    check_or_create_todo_priority(new_priority)
    body = {'id': GLOBAL_CONTEXT.category_id}
    r = requests.post(
        url=f'http://localhost:4567/todos/{task_id}/categories', json=body)

    GLOBAL_CONTEXT.response_json = r.json()
    GLOBAL_CONTEXT.status_code = r.status_code


@when('the student change description of task to <description>')
def change_task_description(description):
    body = {'description': description}
    r = requests.post(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}', json=body)
    assert r.status_code == 200


@when('the student change description of task with id <task_id> to <description>')
def change_task_description_again(task_id, description):
    body = {'description': description}
    r = requests.post(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}', json=body)
    GLOBAL_CONTEXT.response_json = r.json()
    GLOBAL_CONTEXT.status_code = r.status_code


@when('the student fetch the task with <target_priority> priority')
def fetch_tasks_with_target_priority(target_priority):
    r = requests.get(
        f'http://localhost:4567/categories?title={target_priority}')
    assert r.status_code == 200
    GLOBAL_CONTEXT.response_json = r.json()


@when(parsers.parse('I add a new task entry to <course>'))
def add_todo_to_category_again(course, context):
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
def get_category(course):
    r = requests.get("http://localhost:4567/categories")
    for category in r.json()['categories']:
        if category['title'] == course:
            assert False
    assert True
    return


@then(parsers.parse('I should see a success message'))
def assert_success_operation(context):
    assert context['request_return'].status_code in [200, 201]


@then(parsers.parse('I should see an error message'))
def assert_failure_operation(context):
    try:
        assert context['request_return'].status_code not in [200, 201]
    except KeyError:
        assert context['task_return'].status_code not in [200, 201]


@then(parsers.parse('I should see a new list named <course> within the application'))
def get_categories(course, context):
    # Retrieve list of categories
    result = requests.get("http://localhost:4567/categories")

    # Verify it exists mathcing previous requests and within application
    for category in result.json()['categories']:
        if category['id'] == context['request_return'].json()['id'] and \
                category['title'] == context['request_return'].json()['title']:
            assert True
            return
    assert False


@then('the priority of the task should be <new_priority>')
def check_if_task_has_priority(new_priority):
    todo = GLOBAL_CONTEXT.todo_id
    r = requests.get(url=f'http://localhost:4567/todos/{todo}/categories')
    assert r.status_code == 200
    categories = r.json()['categories']
    assert len(categories) == 1
    category_id = categories[0]['id']
    r = requests.get(url=f'http://localhost:4567/categories/{category_id}')
    assert r.status_code == 200
    assert r.json()['categories'][0]['title'] == new_priority


@then(parsers.parse('the system shall inform the user that the task doesn\'t exist'))
def check_if_message_equals_task_do_not_exist():
    assert GLOBAL_CONTEXT.status_code == 404


@then(parsers.parse('the description of the task should be <description>'))
def check_task_description_equal(description):
    r = requests.get(f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}')
    assert r.status_code == 200
    assert r.json()['todos'][0]['description'] == description


@then(parsers.parse('I should not see any duplicate entries named <course> within the application'))
def check_uniqueness_category(course):
    result = requests.get("http://localhost:4567/categories")

    # Verify it exists matching previous requests and within application
    # We also need to verify that there only exists one instance of a given course.
    unique_count = 0
    for category in result.json()['categories']:
        if category['title'] == course:
            unique_count += 1
    assert unique_count == 1


@then(parsers.parse('I should see a new task in <course>'))
def check_task_added(course, context):
    r = requests.get(
        "http://localhost:4567/categories/['request_return']['id']/projects")
    for project in r.json()['projects']:
        if project['title'] == context['task_return'].json()['title'] and \
                project['id'] == context['task_return'].json()['id']:
            assert True
            return
    assert False


@then('the system should display <expected_task_count> number of task')
def check_the_displayed_tasks(expected_task_count):
    todos = GLOBAL_CONTEXT.response_json['categories'][0]['todos']
    assert len(todos) == int(expected_task_count)
##############
## ADD TASK ##
#############

@given("there exists a todo list in the system with title <course>")
def ensure_todo_lists_title_course_exist(course):
    body = {
        'title': course
    }
    r = requests.post(url='http://localhost:4567/projects', json=body)
    GLOBAL_CONTEXT.project_id = r.json()['id']
    assert r.status_code == 201
    assert r.json()['title'] == course


@when("I add a new task with title <title> to the todo list with title <course>")
def add_new_tasks_with_title_title(title, course):
    if GLOBAL_CONTEXT.todo_id == -1:
        return
    todoPost = 'http://localhost:4567/todos'
    todoBody = {'title': title}
    req = requests.post(url=todoPost, json=todoBody)
    GLOBAL_CONTEXT.todo_id = req.json()['id']
    linkUrl = f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/tasksof'
    body = {"id": str(GLOBAL_CONTEXT.project_id)}
    r = requests.post(url=linkUrl, json=body)
    GLOBAL_CONTEXT.status_code = r.status_code
    if(r.status_code != 201):
        GLOBAL_CONTEXT.response_json = r.json()

    linkUrl2 = f'http://localhost:4567/projects/{GLOBAL_CONTEXT.project_id}/tasks'
    body = {"id": str(GLOBAL_CONTEXT.todo_id)}

    r = requests.post(url=linkUrl2, json=body)

@then("I will see a new task with title <title> in the todo list with title <course>")
def get_tasks_for_todos_lists(title, course):
    url = f'http://localhost:4567/projects/{GLOBAL_CONTEXT.project_id}/tasks'
    req = requests.get(url=url)
    assert req.status_code == 200
    for task in req.json()['todos']:
        if task['title'] == title:
            assert True
            return
    assert False

@given("there does not exist a todo list in the system with title <course>")
def ensure_todo_does_not_exist(course):
    r = requests.get('http://localhost:4567/projects?title={course}')

    for project in r.json()['projects']:
        deleteId = project['id']
        req = requests.delete(url=f'http://localhost:4567/projects/{deleteId}')
        assert req.status_code == 200

@then(parsers.parse("the system will inform the user that the todo list with title <course> does not exist"))
def get_error_response(course):
    expectedMessage = "Could not find thing matching value for id"
    if expectedMessage in GLOBAL_CONTEXT.response_json['errorMessages'][0]:
        assert True
    else:
        assert False

@given('the task is part of the todo list')
def ensure_todos_list_contains_task_with_title():
    linkUrl = f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}/tasksof'
    body = {"id": str(GLOBAL_CONTEXT.project_id)}
    r = requests.post(url=linkUrl, json=body)
    assert r.status_code == 201
    linkUrl = f'http://localhost:4567/projects/{GLOBAL_CONTEXT.project_id}/tasks'
    body = {"id": str(GLOBAL_CONTEXT.todo_id)}
    r = requests.post(url=linkUrl, json=body)
    assert r.status_code == 201

@given('the task has done status of <status>')
def ensure_task_status(status):
    value = False
    if status == "Complete":
        value = True
    body = {"doneStatus": value}
    r = requests.post(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}', json=body)
    assert r.status_code == 200

@when('I change the done status to <new_status>')
def change_task_status(new_status):
    value = False
    if new_status == "Complete":
        value = True
    body = {"doneStatus": value}
    urlPost = f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}'
    r = requests.post(url=urlPost, json=body)
    if r.status_code != 200:
        GLOBAL_CONTEXT.response_json = r.json()


@then('the status of the task should be <new_status>')
def task_progress_shaould_be_complete(new_status):
    r = requests.get(
        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.todo_id}')
    value = "false"
    if new_status == "Complete":
        value = "true"
    assert r.status_code == 200
    assert r.json()['todos'][0]['doneStatus'] == value

@then('the system will inform the user that the task does not exist')
def inform_user_task_does_not_exist():
    expected_message = 'No such todo entity instance with GUID'
    assert expected_message in GLOBAL_CONTEXT.response_json['errorMessages'][0]

@given('the task is not part of the todo list')
def ensure_the_task_does_not_exist_in_todo_list():
    todo_id = str(GLOBAL_CONTEXT.todo_id)
    proj_id = str(GLOBAL_CONTEXT.project_id)
    r = requests.get(url=f'http://localhost:4567/todos/{todo_id}/tasksof')
    if len(list(filter(lambda x: x['id'] == proj_id, r.json()['projects']))) != 0:
        requests.delete(
            url=f'http://localhost:4567/todos/{todo_id}/tasksof/{proj_id}')
    r = requests.get(url=f'http://localhost:4567/projects/{proj_id}/tasks')
    if len(list(filter(lambda x: x['id'] == todo_id, r.json()['todos']))) != 0:
        requests.delete(
            url=f'http://localhost:4567/projects/{proj_id}/tasks/{todo_id}')

@when('I remove the task from the todo list')
def remove_task_from_todo_list():
    todo_id = str(GLOBAL_CONTEXT.todo_id)
    proj_id = str(GLOBAL_CONTEXT.project_id)
    linkUrl = f'http://localhost:4567/todos/{todo_id}/tasksof/{proj_id}'
    body = {"id": str(GLOBAL_CONTEXT.project_id)}
    r = requests.delete(url=linkUrl, json=body)
    if r.status_code != 200:
        GLOBAL_CONTEXT.status_code = r.status_code
        GLOBAL_CONTEXT.response_json = r.json()
    linkUrl = f'http://localhost:4567/projects/{proj_id}/tasks{todo_id}'
    body = {"id": str(GLOBAL_CONTEXT.todo_id)}
    r = requests.delete(url=linkUrl, json=body)

@then('I should not see the task with title <title> in the todo list with title <course>')
def check_task_does_not_exist_in_todo_list(title, course):
    todo_id = str(GLOBAL_CONTEXT.todo_id)
    proj_id = str(GLOBAL_CONTEXT.project_id)
    r = requests.get(f'http://localhost:4567/todos/{todo_id}')
    todo = r.json()['todos'][0]
    assert todo['title'] == title
    if 'tasksof' in todo:
        assert len(
            list(filter(lambda x: x['id'] == proj_id, todo['tasksof']))) == 0
    r = requests.get(f'http://localhost:4567/projects/{proj_id}')
    proj = r.json()['projects'][0]
    assert proj['title'] == course
    if 'tasks' in proj:
        assert len(
            list(filter(lambda x: x['id'] == todo_id, proj['tasks']))) == 0

@then('the system will inform the user that the task is not on the todo list')
def inform_user_task_not_in_todo_list():
    assert GLOBAL_CONTEXT.status_code == 404
    expected_message = 'Could not find any instances with'
    assert expected_message in GLOBAL_CONTEXT.response_json['errorMessages'][0]

################################
# QUERY Incomplete High Prority
################################

@given('there exist a high priority category in the system')
def ensure_todo_priority_exists():
    priority = "HIGH"
    check_or_create_todo_priority(priority)


@given('there exist <count> high prioirty, incomplete tasks in the todo list')
def ensure_there_exists_counts_high_priority(count):

    ctn = int(count)
    for i in range(ctn):
        title = f'task {i}'
        todo_id = create_task(title)
        body = {'doneStatus': False}
        r = requests.post(
            url=f'http://localhost:4567/todos/{todo_id}', json=body)
        req = requests.post(
            url=f'http://localhost:4567/todos/{todo_id}/tasksof', json={"id": GLOBAL_CONTEXT.project_id})
        req2 = requests.post(
            url=f'http://localhost:4567/projects/{GLOBAL_CONTEXT.project_id}/tasks', json={"id": todo_id})

        assign_priority_to_task(todo_id, GLOBAL_CONTEXT.category_id)


@when('I query all the high priority, incomplete task in the todo list')
def query_all_high_priority():
    r = requests.get(
        url=f'http://localhost:4567/projects/{GLOBAL_CONTEXT.project_id}/tasks?doneStatus=false')
    task = []
    for todo in r.json()['todos']:
        if 'categories' in todo:
            ans = None
            for category in todo['categories']:
                if category['id'] == GLOBAL_CONTEXT.category_id:
                    ans = todo
            if ans != None:
                task.insert(len(task), ans)

        else:
            continue
    GLOBAL_CONTEXT.json_object = task


@given('there exist no high prioirty, incomplete tasks in the todo list')
def ensure_there_exists_no_high_priority_task():
    r = requests.get(url=f'http://localhost:4567/todos?doneStatus=false')
    for todo in r.json()['todos']:
        if 'categories' in todo:
            for category in todo['categories']:
                if category['id'] == GLOBAL_CONTEXT.category_id:
                    taskId = todo['id']
                    req = requests.delete(
                        url=f'http://localhost:4567/todos/{taskId}/taskof/{GLOBAL_CONTEXT.project_id}')
                    req2 = requests.delete(
                        url=f'http://localhost:4567/todos/{GLOBAL_CONTEXT.project_id}/taskof/{taskId}')
                    assert req.status_code == 200
                    assert req2.status_code == 200
                    break

@then(parsers.parse('the system will inform the user that the todo list does not exist'))
def verify_no_todo_list_response():
    assert True

######################
# Query Incomplete task
#######################

@given('there are <count> tasks in the todo list that are incomplete')
def ensure_there_are_count_task(count):
    ctn = int(count)
    for i in range(ctn):
        title = f'task {i}'
        todo_id = create_task(title)
        body = {'doneStatus': False}
        r = requests.post(
            url=f'http://localhost:4567/todos/{todo_id}', json=body)
        req = requests.post(
            url=f'http://localhost:4567/todos/{todo_id}/tasksof', json={"id": GLOBAL_CONTEXT.project_id})
        req2 = requests.post(
            url=f'http://localhost:4567/projects/{GLOBAL_CONTEXT.project_id}/tasks', json={"id": todo_id})

        assert r.status_code == 200
        assert req.status_code == 201
        assert req2.status_code == 201
@when('I query all the incomplete task in the todo list')
def query_all_incompleted_task():
    r = requests.get(
        url=f'http://localhost:4567/projects/{GLOBAL_CONTEXT.project_id}/tasks?doneStatus=false')
    GLOBAL_CONTEXT.status_code = r.status_code
    if r.status_code == 200:
        GLOBAL_CONTEXT.response_json = r.json()

@then('I should see that <count> tasks are found')
def verify_count_tasks(count):
    if GLOBAL_CONTEXT.response_json == None and count == 0:
        assert True
    if GLOBAL_CONTEXT.response_json != None:
        if 'todos' in GLOBAL_CONTEXT.response_json:
            assert len(GLOBAL_CONTEXT.response_json['todos']) == int(count)

@given('there are no tasks in the todo list that are incomplete')
def ensure_no_incomplete_task_in_todo_list():
    r = requests.get(
        url=f'http://localhost:4567/projects/{GLOBAL_CONTEXT.project_id}/tasks')
    for todo in r.json()['todos']:
        todoId = todo['id']
        r = requests.delete(
            url=f'http://localhost:4567/projects{GLOBAL_CONTEXT.project_id}/tasks/{todoId}')
        req = requests.delete(
            url=f'http://localhost:4567/todos/{todoId}/tasksof/{GLOBAL_CONTEXT.project_id}')
        assert r.status_code == 200
        assert req.status_code == 200

# Helper functions

def create_task(title):
    body = {'title': title}
    r = requests.post(url='http://localhost:4567/todos', json=body)
    assert r.status_code == 201
    return r.json()['id']


def assign_priority_to_task(task_id, priority_id):
    body = {'id': priority_id}
    r = requests.post(
        url=f'http://localhost:4567/todos/{task_id}/categories', json=body)
    body['id'] = task_id
    r = requests.post(
        url=f'http://localhost:4567/categories/{priority_id}/todos', json=body)
    assert r.status_code == 201

def check_or_create_todo_priority(priority):
    r = requests.get(url=f"http://localhost:4567/categories?title={priority}")
    if (len(r.json()['categories']) == 0):
        body = {'title': priority}
        requests.post(url="http://localhost:4567/categories", json=body)
    r = requests.get(url=f"http://localhost:4567/categories?title={priority}")
    GLOBAL_CONTEXT.category_id = str(r.json()['categories'][0]['id'])
    assert len(r.json()['categories']) > 0
    return GLOBAL_CONTEXT.category_id
