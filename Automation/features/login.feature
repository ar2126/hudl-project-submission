#
# Hudl Login Page
#
# @author aidanrubenstein
# @since 08/02/2022
#
Feature: LoginTest
  As a Hudl user,
  I want to login
  So that I may use the Hudl application

  Scenario: Login with valid credentials
    Given I am a user
    When I enter my email and password on the login screen
    And I click on the login button
    Then I expect to be redirected to the home page

  Scenario: Login with valid credentials with keyboard shortcuts
    Given I am a user
    When I enter my email and password on the login screen using the tab key
    And I use the enter key to login
    Then I expect to be redirected to the home page

  Scenario: Login with valid credentials go back/forward
    Given I am a user
    When I enter my email and password on the login screen
    And I click on the login button
    Then I expect to be redirected to the home page
    When I navigate back using the browser
    # NOTE: With more time I would check to make sure that we end up at the login page again, but there was a data
    # error when attempting to go backwards via the browser
    And I navigate forward using the browser
    Then I expect to be redirected to the home page


  Scenario: Login with valid credentials new tab
    Given I am a user
    When I enter my email and password on the login screen
    And I click on the login button
    Then I expect to be redirected to the home page
    When I open a new tab to the Hudl home page
    Then I expect to be redirected to the home page

  Scenario: View Reset Password page
    Given I am a user
    When I navigate to perform a password reset
    Then I expect to see the reset password screen

  Scenario: Login with invalid credentials
    Given I am a user
    When I enter my email and incorrect password "garbage..."
    And I click on the login button
    Then I expect an error should display on the page indicating that my login is incorrect

  Scenario Outline: Login with invalid credentials edge cases
    Given I am a user
    When I enter my <email> and incorrect password <password>
    And I click on the login button
    Then I expect an error should display on the page indicating that my login is incorrect
    Examples:
      | email      | password    |
      | asdasda    | null        |
      | null       | asdasdad    |
      # SQL Injection attack - This could be more specific if given the actual table names for login
      | ' OR 1=1-- |  ' OR 1=1-- |
      | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa |