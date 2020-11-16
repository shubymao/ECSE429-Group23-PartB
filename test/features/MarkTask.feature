Feature: Marking a task on a todo list
  As a student,
  I mark a task as done on my course to do list, so I can track my accomplishments.

  Background:
    Given the system is running

  Scenario Outline: Marking a completed task as done on a todo list (Normal Flow)
    Given there exists a todo list in the system with title <course>
    And the task with title <title> exists
    And the task has done status of <status>
    And the task is part of the todo list
    When I change the done status to <new_status>
    Then the status of the task should be <new_status>
    Examples:
      | title                        | course   | status     | new_status |
      | Edit Draft Report1           | ECSE 429 | Incomplete | Complete   |
      | Study for Midterm Exam       | ECSE 429 | Incomplete | Complete   |
      | Work on the Third Assignment | ECSE 429 | Incomplete | Complete   |

  Scenario Outline: Marking an Already-Completed Task as Done (Alternate Flow)
    Given there exists a todo list in the system with title <course>
    And the task with title <title> exists
    And the task has done status of <status>
    And the task is part of the todo list
    When I change the done status to <new_status>
    Then the status of the task should be <new_status>
    Examples:
      | title                        | course   | status   | new_status |
      | Edit Draft Report1           | ECSE 429 | Complete | Complete   |
      | Study for Midterm Exam       | ECSE 429 | Complete | Complete   |
      | Work on the Third Assignment | ECSE 429 | Complete | Complete   |

  Scenario Outline: Marking a Task which does not exist (Error Flow)
    Given there exists a todo list in the system with title <course>
    And the task with id <task_id> does not exists
    When I change the done status to <new_status>
    Then the system will inform the user that the task does not exist

    Examples:
      | task_id | course   | new_status |
      | 9999    | ECSE 429 | Incomplete |
      | 5678    | ECSE 310 | Complete   |
      | 1256    | ECSE 850 | Incomplete |

