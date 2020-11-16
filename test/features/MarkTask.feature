Feature: Marking a task on a todo list
  As a student,
  I mark a task as done on my course to do list, so I can track my accomplishments.

  Background:
    Given the system is running

  Scenario Outline: Marking a completed task as done on a todo list (Normal Flow)
    Given there exists a todo list in the system with title <course>
    And the todo list contains the task with title <title>
    And the current progress <progress> of the task with <title> is "Incomplete"
    When I change the progress <progress> of the task with title <title> to "Complete"
    Then the progress of the task <title> should be "Complete"

    Examples:
      | title              | course   | progress   |
      | Edit Draft Report1 | ECSE 429 | Incomplete |
  # | Study for Midterm Exam       | ECSE 429  | Incomplete   |
  # | Work on the Third Assignment | ECSE 429  | Incomplete   |

  Scenario Outline: Marking an Already-Completed Task as Done (Alternate Flow)
    Given there exists a todo list in the system with title <course>
    And the todo list contains the task with title <title>
    And the current progress <progress> of the task with <title> is "Complete"
    When I change the progress <progress> of the task with title <title> to "Complete"
    Then the progress of the task <title> should be "Complete"

    Examples:
      | title              | course   | progress |
      | Edit Draft Report1 | ECSE 429 | Complete |
  # | Study for Midterm Exam       | ECSE 429  | Incomplete   |
  # | Work on the Third Assignment | ECSE 429  | Incomplete   |

  Scenario Outline: Marking a Task which does not exist on the to do list (Error Flow)
    Given there exists a todo list in the system with title <course>
    And the todo list does not contain the task with title <title>
    When I change the progress <progress> of the task with title <title> to "Complete"
    Then the system will inform the user that the task does not exist

    Examples:
      | title              | course   | progress   |
      | Edit Draft Report1 | ECSE 429 | Incomplete |

