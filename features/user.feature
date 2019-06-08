Feature: User
    An API where you receive an user

Scenario: Reclaim the user
    Given The auth dict is valid
    And The user has a token
    And The user has an environment
    Then The list is pushed  
    And User details are pushed
#    When User goes to the users list page
#    Then User not see the error message
# 	 Note: will query the database