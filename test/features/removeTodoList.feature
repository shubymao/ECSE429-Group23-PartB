Feature: Delete a todo list
  As a student,
  I remove a to do list for a class which I am no longer taking, to de-clutter my schedule.

  Scenario Outline: Delete a to do list for a class with tasks still left in it
    Given the system is running
    And I can see a list with <course> within the application
    And <course> contains an entry
    When I delete an existing to do list named <course>
    Then I should see the to do list entry <course>, disappear from the application
    And I should see a success message
    Examples:
      | course |
      | test  |
      | something  |
    #TODO: Not sure what to do here for success.

  Scenario Outline: Delete a to do list for a class with no tasks in it
    Given the system is running
    And I can see a list with <course> within the application
    And the to do list called <course> contains no tasks
    When I delete <course>
    Then I should see the to do list entry <course>, disappear from the application
    And I should see a success message
    Examples:
      | name |
      | wah  |
      | gah  |
    # TODO: not sure what to do here for success.

  Scenario Outline: Delete a to do list which does not exist
    Given the system is running
    And I can see a list that does not include <course> within the application
    When I delete a nonexistent to do list called <course>
    Then I should see an error message
    Examples:
      | course |
      | test |
      | ok |
    # TODO: not sure what to do here for failure
