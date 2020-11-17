Feature: Create a TODO List
  As a student,
  I (would like to) create a to do list for a new class I am taking, so I can manage course work.

  Background:
    Given the system is running

  Scenario Outline: Create a to do list with a unique name (Normal Flow)
    When I add a new course with title <course>
    Then I should see a new list named <course> within the application
    And I should see a success message
    Examples:
      | course                     |
      | ECSE-429                   |
      | COMP-330                   |
      | ATOC-185                   |
      | somethingunrelatedtoMcGill |

  # This test should fail because it's not behaving.
  Scenario Outline: Create a to do list with a conflicting name (Error Flow)
    Given I can see a list with <course> within the application
    When I add a new course with title <course>
    Then I should not see any duplicate entries named <course> within the application
    And I should see an error message
    Examples:
      | course                     |
      | ECSE-429                   |
      | COMP-330                   |
      | ATOC-185                   |
      | somethingunrelatedtoMcGill |
  # Semantically, this is a bug. You should not be able to have multiple todo lists that are named the same thing.

  Scenario Outline: Create a to do list with a very long name (Alternative Flow)
    When I add a new course with title <course>
    Then I should see a new list named <course> within the application
    And I should see a success message
    Examples:
      | course                                                                           |
      | ECSE-4299128391283912839183981293819238192381238                                 |
      | COMPCOICPOMCOMOCMCOCPMCPMCPMCOMCOMCPOCMPMCOCMOCM-330                             |
      | ATOCTOCOTOFOCOOTOCTOCOTOCTOCTOCTOTOCOTCOTCOTCOTOCTOCTOCT-185                     |
      | somethingunrelatedtoMcGillMcGillMcGillMcGillMcGillMcGillMcGillMcGillMcGillMcGill |

  Scenario Outline: Create a task for an existing class (Normal Flow)
    Given I can see a list with <course> within the application
    When I add a new task entry to <course>
    Then I should see a new task in <course>
    And I should see a success message
    Examples:
      | course                     |
      | ECSE-429                   |
      | COMP-330                   |
      | ATOC-185                   |
      | somethingunrelatedtoMcGill |

  Scenario Outline: Create a task for a non existing class (Error Flow)
    Given I can see a list that does not include <course> within the application
    When I add a new task entry to <course>
    Then I should see an error message
    Examples:
      | course                     |
      | ECSE-429                   |
      | COMP-330                   |
      | ATOC-185                   |
      | somethingunrelatedtoMcGill |