Feature: Adding a task to a todo list 
  As a student,
  I add a task to a course to do list, so I can remember it.
  
  Background:
    Given the system is running

  Scenario Outline: Adding a task to a course to do list (Normal Flow)
    Given there exists a todo list in the system with title <course> 
    When I add a new task with title <title> to the todo list with title <course> 
    Then I will see a new task with title <title> in the todo list with title <course>
     
     Examples:
      | title                        | course   |
      | Edit Draft Report1           | ECSE 429 |
      | Study for Midterm Exam       | ECSE 429 |
      | Work on the Third Assignment | ECSE 429 |
      | new task due soon!! do it!   | ECSE 429 |

   Scenario Outline: Adding an already existing task to the to do list (Alternate Flow) 
    Given there exists a todo list in the system with title <course> 
    When I add a new task with title <title> to the todo list with title <course> 
    Then I will see a new task with title <title> in the todo list with title <course>
     
     Examples:
      | title                        | course   |
      | new task due soon!! do it!   | ECSE 429 |
      | new task due soon!! do it!   | ECSE 429 |

   Scenario Outline: Adding a task on a todo list that doesn't exist (Error Flow)
    Given there does not exist a todo list in the system with title <course> 
    When I add a new task with title <title> to the todo list with title <course> 
    Then the system will inform the user that the todo list does not exist  
    
    Examples:
      | title                        | course   |
      | no task                      | 429      |
      
