Feature: Delete a todo list
  As a student,
  I remove a to do list for a class which I am no longer taking, to de-clutter my schedule.

  Background:
    Given the system is running

  Scenario Outline: Delete a to do list for a class with tasks still left in it (Normal Flow)
    Given I can see a list with <course> within the application
    And <course> contains at least one entry
    When I delete an existing to do list named <course>
    Then I should see the to do list entry <course>, disappear from the application
    And I should see a success message
    Examples:
      | course    |
      | test      |
      | something |

  Scenario Outline: Delete a to do list for a class with no tasks in it (Alternative Flow)
    Given I can see a list with <course> within the application
    And the to do list called <course> contains no tasks
    When I delete an existing to do list named <course>
    Then I should see the to do list entry <course>, disappear from the application
    And I should see a success message
    Examples:
      | course |
      | wah    |
      | gah    |


  Scenario Outline: Delete a to do list which does not exist (Error Flow)
    Given I can see a list that does not include <course> within the application
    When I delete a nonexistent to do list called <course>
    Then I should see an error message
    Examples:
      | course |
      | test   |
      | ok     |
