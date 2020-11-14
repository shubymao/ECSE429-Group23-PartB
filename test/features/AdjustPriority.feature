Feature: Adjust Priority
  As a student,
  I want to adjust the priority of a task, to help better manage my time.

  Scenario Outline: Student changed priority to a different priority (Normal Flow)
    Given the system is running
    And the task with title <title> exists
    And the task has <oldPriority> priority
    When the student change task to <new_priority> priority
    Then the priority of the task should be <new_priority>
    Examples:
      | title                  | oldPriority | new_priority |
      | group project          | LOW         | HIGH        |
      | large assignment       | MEDIUM      | HIGH        |
      | programming assignment | LOW         | MEDIUM      |
      | term paper             | HIGH        | MEDIUM      |
      | open source project    | MEDIUM      | LOW         |
      | TA assignment marking  | HIGH        | LOW         |

  Scenario Outline: Student changed priority to the same priority (Alt Flow)
    Given the system is running
    And the task with title <title> exists
    And the task has <oldPriority> priority
    When the student change task to <new_priority> priority
    Then the priority of the task should be <new_priority>
    Examples:
      | title                  | oldPriority | new_priority |
      | some small assignment  | LOW         | LOW         |
      | some medium assignment | MEDIUM      | MEDIUM      |
      | some large assignment  | HIGH        | HIGH        |

  Scenario Outline: Student changed priority to non-existing task (Error Flow)
    Given the system is running
    And the task with id <task_id> does not exists
    When the student change task with id <task_id> to <new_priority> priority
    Then the system shall inform the user that the task doesn't exist
    Examples:
      | task_id | new_priority |
      | 5000    | LOW         |
      | 9999    | MEDIUM      |
      | 1595    | HIGH        |
