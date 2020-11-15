Feature: Adding a task to a todo list 
  As a student,
  I add a task to a course to do list, so I can remember it.
  
  Background:
    Given the system is running

  Scenario Outline: Adding a task to a course to do list (Normal Flow)
    Given there exists a todo list in the system with title <course> 
    When I add a new task with title <title> to the list with title <course> 
    Then I will see a new task with title <title> in the list with title <course>
     
     Examples:
      | title                        |
      | Edit Draft Report1           |
      | Study for Midterm Exam       |
      | Work on the Third Assignment |
      | new task due soon!! do it!   |

   Scenario Outline: Adding an already existing task to the to do list (Alternate Flow) 
    Given there exists a todo list in the system with title <course> 
    When I add a new task with title <title> to the list with title <course> 
    Then I will see a new task with title <title> in the list with title <course>
     
     Examples:
      | title                        |
      | new task due soon!! do it!   |
      | new task due soon!! do it!   |

   Scenario Outline: Adding a task on a todo list that doesn't exist (Error Flow)
    Given there does not exist a todo list in the system with title <course> 
    When I add a new task with title <title> to the list with title <course> 
    Then the system will inform the user that the list does not exist  

