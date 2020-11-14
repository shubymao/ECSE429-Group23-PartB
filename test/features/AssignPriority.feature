Feature: Assign Priority
    As a student,
    I categorize tasks as HIGH, MEDIUM or LOW priority, so I can better manage my time.

    Scenario Outline: Student add priority on existing tasks (Normal Flow)
        Given the system is running
        And the task with title <title> exists
        When the student assign task to <new_priority> priority
        Then the priority of the task should be <new_priority>
        Examples:
            | title                 | new_priority |
            | large assignment      | HIGH         |
            | term paper            | MEDIUM       |
            | TA assignment marking | LOW          |

    Scenario Outline: Student fetches all tasks of certain priority (Alt Flow)
        Given the system is running
        And the following tasks exists:
            | task 1  | LOW    |
            | task 2  | LOW    |
            | task 3  | MEDIUM |
            | task 4  | MEDIUM |
            | task 5  | MEDIUM |
            | task 6  | MEDIUM |
            | task 7  | MEDIUM |
            | task 8  | MEDIUM |
            | task 9  | HIGH   |
            | task 10 | HIGH   |
            | task 11 | HIGH   |
        When the student fetch the task with <target_priority> priority
        Then the system should display <expected_task_count> number of task
        Examples:
            | target_priority | expected_task_count |
            | LOW             | 2                   |
            | MEDIUM          | 6                   |
            | HIGH            | 3                   |

    Scenario Outline: Student assign priority to non-existing task (Error Flow)
        Given the system is running
        And the task with id <task_id> does not exists
        When the student change task with id <task_id> to <new_priority> priority
        Then the system shall inform the user that the task doesn't exist
        Examples:
            | task_id | new_priority |
            | 5000    | LOW          |
            | 9999    | MEDIUM       |
            | 1595    | HIGH         |
