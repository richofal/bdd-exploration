Feature: Open Pembangunan Perangkat Lunak Assignment
  In order to review assignment details...
  As a Student...
  I want to open and view the details of a specific PPL assignment...

  Background:
    Given The Student is on the "Hebat" login page
    When The Student enters a valid username into the "Username" field
    And The Student enters a valid password into the "Password" field
    And The Student clicks the "Log in" button
    Then The Student should be redirected to the Hebat system's "Home" page

  Scenario: Successfully Viewing Pembangunan Perangkat Lunak Assignment Details
    Given The Student is on the "Pembangunan Perangkat Lunak (PPL) course" page
    When The Student clicks on a specific "Assignment Title" link