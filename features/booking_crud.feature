Feature: Booking API CRUD
  As a client of the Restful-Booker API
  I want to create, update, and delete bookings
  So that I can manage reservations through the API

  Scenario: Create a booking and get back a valid schema
    Given I am authenticated with the booking API
    When I create a booking
    Then the booking response should match a valid schema
    And the booking should match what I sent

  Scenario: Update an existing booking
    Given I am authenticated with the booking API
    And I have created a booking
    When I update the booking's total price to 300
    Then the booking's total price should be 300

  Scenario: Delete an existing booking
    Given I am authenticated with the booking API
    And I have created a booking
    When I delete the booking
    Then the booking should no longer exist
