Feature: Removing a task from a todo list
  As a student,
  I remove an unnecessary task from my course to do list, so I can forget about it.

  Background:
    Given the system is running

  Scenario Outline: Removing an unnecessary task from a todo list (Normal Flow)
    Given there exists a todo list in the system with title <course> 
    And there exists a task with title <title>
    And the task with title <title> has <necessary> as no
    When I remove the task with title <title> from the todo list with title <course> 
    Then I should not see the task with title <title> in the todo list with title <course>

   Scenario Outline: Removing a necessary task from a todo list (Alternate Flow)
    Given there exists a todo list in the system with title <course> 
    And there exists a task with title <title>
    And the task with title <title> has <necessary> as yes
    When I remove the task with title <title> from the todo list with title <course> 
    Then I should not see the task with title <title> in the todo list with title <course>

   Scenario Outline: Removing a task on a todo list that doesn't exist (Error Flow)
    Given there exists a todo list in the system with title <course> 
    And there does not exist a task with title <title>
    When I remove the task with title <title> from the todo list with title <course> 
    Then the system will inform the user that the task does not exist


