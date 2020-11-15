Feature: Marking a task on a todo list
  As a student, 
  I mark a task as done on my course to do list, so I can track my accomplishments.

  Background:
    Given the system is running

  Scenario Outline: Marking a completed task as done on a todo list (Normal Flow)
    Given there exists a todo list in the system with title <course> 
    And the todo list contains the task with title <title>
    When I change the progress of the task with title <title> to <newProgress>
    Then I should see the progress of task with title <title> be <newProgress>
     
     Examples:
      | title                        | oldProgress  | newProgress  |
      | Edit Draft Report1           | Incomplete   | Incomplete   |
      | Study for Midterm Exam       | Incomplete   | Incomplete   |
      | Work on the Third Assignment | Incomplete   | Complete     |

   Scenario Outline: Marking an Already-Completed Task as Done (Alternate Flow)
    Given there exists a todo list in the system with title <course> 
    And the todo list contains the task with title <title>
    When I change the progress of the task with title <title> to <newProgress>
    Then I should see the progress of task with title <title> be <newProgress>
     
     Examples:
      | tasks for Course 1 (id 1)    | oldProgress  | newProgress  |
      | Edit Draft Report1           | Complete     | Complete     |
      | Study for Midterm Exam       | Incomplete   | Incomplete   |
      | Work on the Third Assignment | Incomplete   | Incomplete   |

   Scenario Outline: Marking a Task which does not exist on the to do list (Error Flow)
    Given there exists a todo list in the system with title <course> 
    And the todo list does not contain the task with title <title>
    When I change the progress of the task with title <title> to <newProgress>
    Then the system will inform the user that the task does not exist

