Feature: Your cart is empty message shows

  Scenario: Cart is empty message shows
    Given Open Target page
    When Click on cart button
    Then Your cart is empty message displays

Feature: Logged out user can navigate to sign in page


  Scenario: Clicking on sign on page leads to sign in page
    Given Open Target page
    When Click on sign on button
    When Click sign in from side navigation
    Then Sign in message displays

