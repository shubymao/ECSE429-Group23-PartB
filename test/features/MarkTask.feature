Feature: Marking a task on a todo list
  As a student,
  I mark a task as done on my course to do list, so I can track my accomplishments.

  Background:
    Given the system is running

  Scenario Outline: Marking a completed task as done on a todo list (Normal Flow)
    Given there exists a todo list in the system with title <course>
    # Post /projects with body {title : course} gets project_id
    And the todo list contains the task with title <title>
    # Post /todos with body {title : title} gets todo_id here
    # Post /todos/todo_id/taskof with body {id: project_id}
    And the current progress of the task with <title> is <progress>
    # get /todos?title={title}  receives an json j, tid = j['todos'][0]['id']
    # post /todos/tid with body {"completeStatus": {TRUE/FALSE:COMPLETE}}
    # Assert 201
    When I change the progress of the task with title <title> to <newProgress>
    # get /todos?title={title}  receives an json j
    # Assert j['todos'][0]['completeStatus'] == 'true'
    Then the progress of the task <title> should be <newProgress>

    Examples:
      | title              | course   | progress   | newProgress |
      | Edit Draft Report1 | ECSE 429 | Incomplete | Complete    |
# | Study for Midterm Exam       | ECSE 429  | Incomplete   | Complete |
# | Work on the Third Assignment | ECSE 429  | Incomplete   | Complete |

Scenario Outline: Marking an Already-Completed Task as Done (Alternate Flow)
  Given there exists a todo list in the system with title <course>
  And the todo list contains the task with title <title>
  And the current progress of the task with <title> is <progress>
  When I change the progress of the task with title <title> to <newProgress>
  Then the progress of the task <title> should be <newProgress>

  Examples:
    | title              | course   | progress | newProgress |
    | Edit Draft Report1 | ECSE 429 | Complete | Complete    |
# | Study for Midterm Exam       | ECSE 429  | Incomplete   | Complete    |
# | Work on the Third Assignment | ECSE 429  | Incomplete   | Complete    |

Scenario Outline: Marking a Task which does not exist on the to do list (Error Flow)
  Given there exists a todo list in the system with title <course>
  And the todo list does not contain the task with title <title>
  When I change the progress of the task with title <title> to <newProgress>
  Then the system will inform the user that the task does not exist

  Examples:
    | title              | course   | newProgress   |
    | Edit Draft Report1 | ECSE 429 | Incomplete    |

