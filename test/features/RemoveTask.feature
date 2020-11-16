Feature: Removing a task from a todo list
  As a student,
  I remove an unnecessary task from my course to do list, so I can forget about it.

  Background:
    Given the system is running

  Scenario Outline: Removing an unnecessary task from a todo list (Normal Flow)
    Given there exists a todo list in the system with title <course> 
    And there exists a task with title <title>
    And the task with title <title> has <necessary> as "No"
    When I remove the task with title <title> from the todo list with title <course> and <necessary> as "No"
    Then I should not see the task with title <title> in the todo list with title <course>

     Examples:
      | title                        | course   | necessary |
      | Edit Draft Report1           | ECSE 429 | No        |
      | Study for Midterm Exam       | ECSE 429 | Yes       |
      | Work on the Third Assignment | ECSE 429 | No        |
      | do the readings              | ECSE 429 | No        |

   Scenario Outline: Removing a necessary task from a todo list (Alternate Flow)
    Given there exists a todo list in the system with title <course> 
    And there exists a task with title <title>
    And the task with title <title> has <necessary> as "Yes"
    When I remove the task with title <title> from the todo list with title <course> and <necessary> as "Yes"
    Then I should not see the task with title <title> in the todo list with title <course>

     Examples:
      | title                        | course   | necessary |
      | Edit Draft Report1           | ECSE 429 | No        |
      | Study for Midterm Exam       | ECSE 429 | Yes       |
      | Work on the Third Assignment | ECSE 429 | Yes       |
      | done task                    | ECSE 429 | No        |

   Scenario Outline: Removing a task on a todo list that doesn't exist (Error Flow)
    Given there exists a todo list in the system with title <course> 
    And there does not exist a task with title <title>
    When I remove the task with title <title> from the todo list with title <course> 
    Then the system will inform the user that the task does not exist

     Examples:
      | title                        | course   | necessary |
      | Edit Draft Report1           | ECSE 429 | No        |

