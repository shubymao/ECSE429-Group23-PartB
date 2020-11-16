Feature: Querying incomplete HIGH priority tasks
   As a student,
   I query all incomplete HIGH priority tasks from all my classes, to identify my short-term goals. 

   Background:
    Given the system is running

   Scenario: Querying all incomplete HIGH priority tasks for a class (Normal Flow)
    Given there exists a todo list in the system with title <course> 
    And there exists at least one task with priority <newPriority> as HIGH and the progress <newProgress> as Incomplete
    When I query all tasks with progress <newProgress> as Incomplete and the progress <newProgress> as Incomplete for the todo list with title <course> 
    Then I should see a query list with title <query> that lists all tasks with title <title> that have <newProgress> as Incomplete and priority <new_priority> as HIGH

     Examples:
      | title                        | course   | newProgress | newPriority   |
      | type the assignment          | ECSE 429 | Incomplete  | HIGH          |
      | do that reading              | ECSE 429 | Complete    | HIGH          |
      | check the exam results       | ECSE 429 | Incomplete  | LOW           |
      | work on next assignment      | ECSE 429 | Complete    | MEDIUM        |

   Scenario: Querying all incomplete LOW priority tasks for a class (Alternate Flow)
    Given there exists a todo list in the system with title <course> 
    And there exists at least one task with priority <new_priority> as LOW and the progress <newProgress> as Incomplete
    When I query all tasks with progress <newProgress> as Incomplete and the priority <new_priority> as LOW for the todo list with title <course> 
    Then I should see a query list with title <query> that lists all tasks with title <title> that have <newProgress> as Incomplete and priority <new_priority> as LOW

     Examples:
      | title                        | course   | newProgress | newPriority   |
      | type the assignment          | ECSE 429 | Incomplete  | HIGH          |
      | do that reading              | ECSE 429 | Complete    | HIGH          |
      | check the exam results       | ECSE 429 | Incomplete  | LOW           |
      | work on next assignment      | ECSE 429 | Complete    | MEDIUM        |

   Scenario: Querying incomplete LOW priority tasks on an empty todo list (Error Flow)
    Given there exists a todo list in the system with title <course> 
    And the todo list with title <course> is empty
    When I query all tasks with progress <newProgress> as Complete and priority <newPriority> as HIGH for the todo list with title <course> 
    Then the system will inform the user that there are no incomplete tasks 

     Examples:
      | title                        | course   | newProgress | newPriority   |
      | do that reading              | ECSE 429 | Complete    | HIGH          |
      | work on next assignment      | ECSE 429 | Complete    | MEDIUM        |
