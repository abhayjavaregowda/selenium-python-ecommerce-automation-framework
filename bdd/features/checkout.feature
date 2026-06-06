Feature: Checkout
  Logged-in users should be able to buy products from the ecommerce store.

  @smoke @bdd @checkout
  Scenario: Complete checkout for one product
    Given I am logged in as the "standard" user
    When I add the "backpack" product to my cart
    And I checkout with valid customer information
    Then I should see the checkout confirmation message
