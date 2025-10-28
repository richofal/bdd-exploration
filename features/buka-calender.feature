Feature: Open Calendar
  In order to view academic deadlines and schedules
  As a Student
  I must be able to open the Calendar from the user menu

  Background:
    Given The Student is on the "Hebat" login page
    When The Student enters a valid username into the "Username" field
    And The Student enters a valid password into the "Password" field
    And The Student clicks the "Log in" button
    Then The Student should be redirected to the Hebat system's "Home" page

  Scenario: Successful Navigation to Calendar Page from Homepage
    When The Student clicks their name in the "User Menu"
    And The Student clicks the "Calendar" option from the dropdown menu
    Then The Student should be redirected to the "Calendar" page
    And The Student should see the header containing the text "Calendar"