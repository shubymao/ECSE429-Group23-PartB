Feature: Removing a task from a todo list
  As a student,
  I remove an unnecessary task from my course to do list, so I can forget about it.

  Background:
    Given the system is running

  Scenario Outline: Removing a completed task from a todo list (Normal Flow)
    Given there exists a todo list in the system with title <course>
    And the task with title <title> exists
    And the task has done status of <status>
    And the task is part of the todo list
    When I remove the task from the todo list
    Then I should not see the task with title <title> in the todo list with title <course>
    Examples:
      | course   | title         | status    |
      | ECSE 345 | Do Assignment | Completed |

  Scenario Outline: Removing an uncompleted task from a todo list (Alternate Flow)
    Given there exists a todo list in the system with title <course>
    And the task with title <title> exists
    And the task has done status of <status>
    And the task is part of the todo list
    When I remove the task from the todo list
    Then I should not see the task with title <title> in the todo list with title <course>
    Examples:
      | course   | title         | status      |
      | ECSE 429 | Do Assignment | Incompleted |

  Scenario Outline: Removing a task not on a todo list (Error Flow)
    Given there exists a todo list in the system with title <course>
    And the task with title <title> exists
    And the task is not part of the todo list
    When I remove the task from the todo list
    Then the system will inform the user that the task is not on the todo list
    Examples:
      | course   | title         |
      | ECSE 345 | Do Assignment |


