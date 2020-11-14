Feature: Adding a task to a todo list 
  As a student,
  I add a task to a course to do list, so I can remember it.

  Scenario Outline: Adding a task to a course to do list (Normal Flow)
    Given the system is running
    And there exists a todo list in the system with list id <id> 
    When I add the task with task id <id> to the todo list with list id <id> 
    Then I should see a new task with task id <id> in the todo list with list id <id>
     
     Examples:
      | tasks for Course 1 (id 1)    |
      | Edit Draft Report1           |
      | Study for Midterm Exam       |
      | Work on the Third Assignment |
      | new task due soon!! do it!   |

   Scenario Outline: Adding an already existing task to the to do list (Alternate Flow) 
    Given the system is running
    And there exists a todo list in the system with list id <id> 
    When I add the task with task id <id> to the todo list with list id <id> 
    Then I should see a new task with task id <id> in the todo list with list id <id>
     
     Examples:
      | tasks for Course 1 (id 1)    |
      | new task due soon!! do it!   |
      | new task due soon!! do it!   |

   Scenario Outline: Adding a task on a todo list that doesn't exist (Error Flow)
    Given the system is running
    And there does not exist a todo list in the system with list id <id> 
    When I add the task with task id <id> to the todo list with list id <id> 
    Then the system will inform the user that the todo list does not exist  

