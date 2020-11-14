Feature: Change Description
  As a student,
  I want to change a task description, to better represent the work to do.

  Scenario Outline: Student changed description on tasks with description(Normal Flow)
    Given the system is running
    And the task with title "<title>" exists
    And the task has description of "<oldDescription>"
    When the student change description of task to "<newDescription>"
    Then the description of the task should be "<newDescription>"
    Examples:
      | title                  | oldDescription        | newDescription             |
      | group project          | assign first meeting  | assign member task         |
      | assignment             | bad event             | terrible event             |
      | programming assignment | terrible life choices | why is this still not done |
      | term paper             | wonderful task        | almost finished!!!         |

  Scenario Outline: Student change description on tasks no existing description(Alt Flow)
    Given the system is running
    And the task with title "<title>" exists
    And the task has no description
    When the student change description of task to "<newDescription>"
    Then the description of the task should be "<newDescription>"
    Examples:
      | title                 | newDescription             |
      | open source project   | what a bait                |
      | TA assignment marking | will this ever be finished |
      | overdue assignment    | archived task              |

  Scenario Outline: Student changed description on non-existing task (Error Flow)
    Given the system is running
    And the task with id <id> does not exists
    When the student change description of task with id <id> to "<newDescription>"
    Then the system shall inform the user that the task doesn't exist
    Examples:
      | id   | newDescription              |
      | 5000 | Totally a thing             |
      | 9999 | Yep totally have 9999 todos |
      | 1595 | is this for real!!!         |
