Feature: Open Calendar
  In order to view academic deadlines and schedules
  As a Student
  I must be able to open the Calendar from the user menu

Scenario: Successful Navigation to Calendar Page from Homepage
  Given The Student is logged into the Hebat platform
  When The Student clicks their name in the "User Menu"
  And The Student clicks the "Calendar" option from the dropdown menu
  Then The Student should be redirected to the "Calendar" page
  And The Student should see the header containing the text "Calendar"