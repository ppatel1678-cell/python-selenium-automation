
Feature: Adding products to Target cart


  Scenario: User can add a product into target cart
    Given Open Target page
    When Click on product of choice
    When Click on add to cart button
    When Click on cart icon
    Then Verify product is in cart
