Feature: Querying incomplete tasks
   As a student,
   I query the incomplete tasks for a class I am taking, to help manage my time.

   Background:
      Given the system is running

   Scenario: Querying incomplete tasks for a class (Normal Flow)
      Given there exists a todo list in the system with title <course>
      And there exists at least one task with progress <newProgress> as Incomplete
      When I query all tasks with progress <newProgress> as Incomplete for the todo list with title <course>
      Then I should see a query list with title <query> that lists all tasks with title <title> that have <newProgress> as Incomplete

   Scenario: Querying complete tasks for a class (Alternate Flow)
      Given there exists a todo list in the system with title <course>
      And there exists at least one task with progress <newProgress> as Complete
      When I query all tasks with progress <newProgress> as Complete for the todo list with title <course>
      Then I should see a query list with title <query> that lists all tasks with title <title> that have <newProgress> as Complete

   Scenario: Querying incomplete tasks on an empty todo list (Error Flow)
      Given there exists a todo list in the system with title <course>
      And the todo list with title <course> is empty
      When I query all tasks with progress <newProgress> as Complete for the todo list with title <course>
      Then the system will inform the user that there are no incomplete tasks
