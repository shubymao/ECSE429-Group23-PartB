Feature: Removing a task from a todo list
  As a student,
  I remove an unnecessary task from my course to do list, so I can forget about it.

  Scenario Outline: Removing an unnecessary task from a todo list (Normal Flow)
    Given the system is running
    And there exists a todo list in the system with list id <id> 
    And there exists a task with task id <id>
    And the task with id <id> has "<necessary>" as no
    When I remove the task with task id <id> from the todo list with list id <id> 
    Then I should not see the task with task id <id> in the todo list with list id <id>

   Scenario Outline: Removing a necessary task from a todo list (Alternate Flow)
    Given the system is running
    And there exists a todo list in the system with list id <id> 
    And there exists a task with task id <id>
    And the task with id <id> has "<necessary>" as yes
    When I remove the task with task id <id> from the todo list with list id <id> 
    Then I should not see the task with task id <id> in the todo list with list id <id>

   Scenario Outline: Removing a task on a todo list that doesn't exist (Error Flow)
    Given the system is running
    And there exists a todo list in the system with list id <id> 
    And there does not exist a task with task id <id>
    When I remove the task with task id <id> from the todo list with list id <id> 
    Then the system will inform the user that the task does not exist


