Feature: Swag Labs checkout
  As a customer of Swag Labs
  I want to buy the cheapest available product
  So that I can complete an order at the lowest possible price

  Scenario: Standard user buys the cheapest item, sorted by price low to high
    Given I am logged in as "standard_user" with password "secret_sauce"
    When I sort the products by price low to high
    And I add the cheapest item to the cart
    And I proceed to checkout
    And I enter my shipping details as "John" "Doe" "10001"
    And I finish the order
    Then the page title should show "Checkout: Complete!"
    And the order confirmation should say "Thank you for your order!"
