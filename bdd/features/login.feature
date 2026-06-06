Feature: Login
  Users should be able to access the application only with valid credentials.

  @smoke @bdd @login
  Scenario: Successful login with a valid user
    Given I am on the SauceDemo login page
    When I login with the "standard" user
    Then I should see the products page

  @regression @bdd @login @negative
  Scenario: Locked out user cannot login
    Given I am on the SauceDemo login page
    When I login with the "locked_out" user
    Then I should see the login error for the "locked_out" user
