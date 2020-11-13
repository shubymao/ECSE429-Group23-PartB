Feature: Adjust Priority
  As a student,
  I want to adjust the priority of a task, to help better manage my time.

  Scenario Outline: Student changed priority on existing tasks (Normal Flow)
    Given the system is running
    And the task with id <id> exists
    And the task with id <id> has "<oldPriority>" priority
    When the student change task with id <id> to "<newPriority>" priority
    Then the priority of the task with <id> should be "<newPriority>"
    
    Examples:
    | id | oldPriority | newPriority |
    | 1  | LOW         | HIGH        |
    | 1  | MEDIUM      | HIGH        |
    | 1  | HIGH        | HIGH        |
    | 1  | LOW         | MEDIUM      |
    | 1  | HIGH        | MEDIUM      |
    | 1  | MEDIUM      | LOW         |
    | 1  | HIGH        | LOW         |

  Scenario Outline: Student changed priority to the same priority (Alt Flow)
    Given the system is running
    And the task with id <id> exists
    And the task with id <id> has "<oldPriority>" priority
    When the student change task with id <id> to "<newPriority>" priority
    Then the priority of the task with <id> should be "<newPriority>"
    And the priority status should stay the same
    
    Examples:
    | id | oldPriority | newPriority |
    | 1  | LOW         | LOW         |
    | 1  | MEDIUM      | MEDIUM      |
    | 1  | HIGH        | HIGH        |

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
