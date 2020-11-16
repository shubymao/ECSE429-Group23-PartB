Feature: Querying incomplete tasks
  As a student,
  I query the incomplete tasks for a class I am taking, to help manage my time.

  Background:
    Given the system is running

  Scenario: Querying tasks for a class with some incomplete task(Normal Flow)
    Given there exists a todo list in the system with title <course>
    # Done already project id in the GLOBAL CONTEXT

    And there are <count> tasks in the todo list that are incomplete
    # for i in range(count) :
    #    todo_id = create_task(f"task {i}") <- this helper function exists
    #    post todos/todo_id body {'doneStatus' : false}
    #    post todos/todo_id/tasksof with body {id: project_id}
    #    post projects/project_id/tasks with body {id: todo_id}
    When I query all the incomplete task in the todo list
    #    get projects/project_id/tasks?doneStatus=false
    #    store the status codes in GLOBAL CONTEXT 
    #    store the json response in GLOBAL CONTEXT
    Then I should see that <count> tasks are found
    #    assert len(json['todos']) == count
    Examples:
      | course   | count |
      | ECSE 429 | 1     |
    # | ECSE 310 | 2     |
    # | COMP 251 | 3     |

  Scenario: Querying tasks for a class with no incomplete task (Alternate Flow)
    Given there exists a todo list in the system with title <course>
    And there are no tasks in the todo list that are incomplete
    # r = post projects/project_id/tasks
    #    for todo in r.json()['todos']: this theoreically should be empty but still should remove
    #        delete projects/project_id/tasks/todo['id']
    #        delete todos/todo['id']/tasksof/project_id
    When I query all the incomplete task in the todo list
    Then I should see that <count> tasks are found
    # assert len(json['todos']) == 0
    Examples:
      | course   | count |
      | ECSE 429 | 0     |
    # | ECSE 310 | 0     |
    # | COMP 251 | 0     |

  Scenario: Querying incomplete tasks on an non-existing todo list (Error Flow)
    Given there does not exist a todo list in the system with title <course>
      # r = get projects?title=course
      # for project in r.json()['projects']: <- this technically should be empty but just verification
      #   delete projects/project['id']
    When I query all the incomplete task in the todo list
    Then the system will inform the user that the todo list does not exist
      # check error codes 404 and errorMessages <- check yourself 
    Examples:
      | course          |
      | Phylo 2000      | 
