Feature: Change Description
  As a student,
  I want to change a task description, to better represent the work to do.

  Scenario Outline: Student changed description on tasks with description(Normal Flow)
    Given the system is running
    And the task with id <id> exists
    And the task with id <id> has description of "<oldDescription>"
    When the student change description of task with id <id> to "<newDescription>"
    Then the priority of the task with <id> should be "<newDescription>"
    Examples:
      | id | oldDescription        | newDescription             |
      | 1  | hello world           | some coding event          |
      | 1  | bad event             | terrible event             |
      | 1  | terrible life choices | why is this still not done |
      | 1  | wonderful task        | almost finished!!!         |

  Scenario Outline: Student change description on tasks no existing description(Alt Flow)
    Given the system is running
    And the task with id <id> exists
    And the task with id <id> has no description
    When the student change description of task with id <id> to "<newDescription>"
    Then the description of the task with <id> should be "<newDescription>"
    Examples:
      | id | newDescription             |
      | 1  | what a bait                |
      | 1  | will this ever be finished |
      | 1  | archived todos             |

  Scenario Outline: Student changed description on non-existing task (Error Flow)
    Given the system is running
    And the task with id <id> does not exists
    When the student change description of task with id <id> to "<newDescription>"
    Then the system shall inform the user that the task doesn't exist
    Examples:
      | id   | newDescription              |
      | 5000 | Totally a thing             |
      | 9999 | Yep totally have 9999 todos |
      | 1595 | why is this todo here       |
