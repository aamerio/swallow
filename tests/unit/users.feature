Feature: Users
    An API where you receive a list of users

Scenario: Reclaim the users list
    Given I'm an authorized user
    And I have an environment
    When I go to the users list page
    Then I should not see the error message
    And the list is pushed  # Note: will query the database