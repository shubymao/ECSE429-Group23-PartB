Feature: Delete a todo list
  As a student,
  I remove a to do list for a class which I am no longer taking, to declutter my schedule.

  Scenario Outline: Delete a to do list for a class with tasks in it
    Given the system is running
    And the system contains a to do list with entry id <id>
    And entry id <id> with taskID "<taskid>" exists
    When I delete an existing to do list with id <id>
    Then I should see the to do list entry with id <id> disappear from the application
    And I should see a success message
    Examples:
      | id | taskid |
      | 1  | 3      |
      | 2  | 3      |
    #TODO: Not sure what to do here for success.

  Scenario Outline: Delete a to do list for a class with no tasks in it
    Given the system is running
    And the system contains a to do list with entry id <id>
    And entry id <id> contains no tasks
    When I delete an empty to do list with id <id>
    Then I should see the to do list entry with id <id> disappear from the application
    And I should see a success message
    Examples:
      | id |
      | 1  |
      | 2  |
    # TODO: not sure what to do here for success.

  Scenario Outline: Delete a to do list which does not exist
    Given the system is running
    And a to do list with id <id> does not exist
    When I delete a nonexistent to do list with id <id>
    Then I should see an error message
    Examples:
      | id |
      | 55 |
      | 22 |
    # TODO: not sure what to do here for failure
