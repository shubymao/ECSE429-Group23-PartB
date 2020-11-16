Feature: Querying incomplete HIGH priority tasks
  As a student,
  I query all incomplete HIGH priority tasks from all my classes, to identify my short-term goals.

  Background:
    Given the system is running

  Scenario: Querying tasks for a class with some high priority incomplete task (Normal Flow)
    Given there exists a todo list in the system with title <course>
    # done
    And there exist a high priority category in the system
    # check_or_create_todo_priority(priority) <- this was my helper function
    # the helper function puts id into the GLOBAL_CONTEXT.category_id
    And there exist <count> high prioirty, incomplete tasks in the todo list
    # First steps same as create incomplete task in todo list (refer to query incomplete job)
    # within the for loop, use another one of my helper function 
    # assign_priority_to_task(task_id, priority_id) <- you're welcome
    When I query all the high priority, incomplete task in the todo list
    # Query first with the same as query incomplete task (refer to query incomplete job)
    # filter the array with the todos with the correct category_id
    # place the array into GLOBAL_CONTEXT.json_object
    Then I should see that <count> tasks are found
    # Done
    Examples:
      | course   | count |
      | ECSE 310 | 1     |
      | ECSE 429 | 2     |
      | COMP 251 | 3     |

  Scenario: Querying tasks for a class with no high priority incomplete task (Alternate Flow)
    Given there exists a todo list in the system with title <course>
    And there exist a high priority category in the system
    And there exist no high prioirty, incomplete tasks in the todo list
    # Get all tasks in the project with doneStatus=false (refer to query incomplete job)
    # for each task, if tasks is high priority <- this is the only extra step 
    # delete /todos/task['id']/taskof/project_id
    # delete /projects/project_id/tasks/task['id']
    When I query all the high priority, incomplete task in the todo list
    Then I should see that no tasks are found
    Examples:
      | course   | count |
      | COMP 403 | 0     |
      | ECSE 311 | 0     |

  Scenario: Querying incomplete high priority tasks on an non-existing todo list (Error Flow)
    Given there does not exists a todo list in the system with title <course>
    And there exist a high priority category in the system
    When I query all the high priority, incomplete task in the todo list
    Then the system will inform the user that the todo list does not exist
    Examples:
      | course   | count |
      | 7800     | 0     |
      | 1433     | 0     |
      | 2008     | 0     |
