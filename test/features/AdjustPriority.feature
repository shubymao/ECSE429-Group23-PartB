Feature: Adjust Priority
  As a student,
  I want to adjust the priority of a task, to help better manage my time.

  Scenario Outline: Student changed priority on existing tasks (Normal Flow)
    Given the system is running
    And the task with title "<title>" exists
    And the task has "<oldPriority>" priority
    When the student change task to "<newPriority>" priority
    Then the priority of the task should be "<newPriority>"

    Examples:
      | title                  | oldPriority | newPriority |
      | group project          | LOW         | HIGH        |
      | large assignment       | MEDIUM      | HIGH        |
      | programming assignment | LOW         | MEDIUM      |
      | term paper             | HIGH        | MEDIUM      |
      | open source project    | MEDIUM      | LOW         |
      | TA assignment marking  | HIGH        | LOW         |

  Scenario Outline: Student changed priority to the same priority (Alt Flow)
    Given the system is running
    And the task with title "<title>" exists
    And the task has "<oldPriority>" priority
    When the student change task to "<newPriority>" priority
    Then the priority of the task should be "<newPriority>"
    And the priority status should stay the same

    Examples:
      | title                  | oldPriority | newPriority |
      | some small assignment  | LOW         | LOW         |
      | some medium assignment | MEDIUM      | MEDIUM      |
      | some large assignment  | HIGH        | HIGH        |

  Scenario Outline: Student changed priority unsuccessfully (Error Flow)
    Given the system is running
    And the task with id <id> does not exists
    When the student change task with id <id> to "<newPriority>" priority
    Then the system shall inform the user that the task doesn't exist

    Examples:
      | id   | newPriority |
      | 5000 | HIGH        |
      | 9999 | HIGH        |
      | 1595 | HIGH        |
