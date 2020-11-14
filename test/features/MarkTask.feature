Feature: Marking a task on a todo list
  As a student, 
  I mark a task as done on my course to do list, so I can track my accomplishments.

  Scenario Outline: Marking a completed task as done on a todo list (Normal Flow)
    Given the system is running
    And there exists a todo list in the system with list id <id> 
    And the todo list contains the task with task id <id>
    When I change the new progress of the task with id <id> to "<newProgress>"
    Then I should see the new progress of task with id <id> be marked to "<newProgress>"
     
     Examples:
      | tasks for Course 1 (id 1)    | oldProgress  | newProgress  |
      | Edit Draft Report1           | Incomplete   | Incomplete   |
      | Study for Midterm Exam       | Incomplete   | Incomplete   |
      | Work on the Third Assignment | Incomplete   | Complete     |

   Scenario Outline: Marking an Already-Completed Task as Done (Alternate Flow)
    Given the system is running
    And there exists a todo list in the system with list id <id> 
    And the todo list contains the task with task id <id>
    When I change the new progress of the task with id <id> to "<newProgress>"
    Then I should see the new progress of task with id <id> be marked to "<newProgress>"
     
     Examples:
      | tasks for Course 1 (id 1)    | oldProgress  | newProgress  |
      | Edit Draft Report1           | Complete     | Complete     |
      | Study for Midterm Exam       | Incomplete   | Incomplete   |
      | Work on the Third Assignment | Incomplete   | Incomplete   |

   Scenario Outline: Marking a Task which does not exist on the to do list (Error Flow)
    Given the system is running
    And there exists a todo list in the system with list id <id> 
    And the todo list does not contain the task with task id <id>
    When I change the new progress of the task with task id <id> to "<newProgress>"
    Then the system will inform the user that the task doesn't exist

