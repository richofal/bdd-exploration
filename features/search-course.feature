Feature: Student Course Search
  As a Student
  I want to be able to search for courses on the "Course Overview" page
  In order to quickly find a specific course

  Background:
    Given The Student is on the "Hebat" login page
    When The Student enters a valid username into the "Username" field
    And The Student enters a valid password into the "Password" field
    And The Student clicks the "Log in" button
    Then The Student should be redirected to the Hebat system's "Home" page

  Scenario: Successful Search for an Existing Course
    When The Student enters "Pembangunan Perangkat Lunak" into the "Search" field
    Then The Student should see the course "2025Ganjil - SII318 - Pembangunan Perangkat Lunak - S1 - Sistem Informasi - 2021 - I1" in the results