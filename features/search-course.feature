Feature: Student Course Search
  As a Student
  I want to be able to search for courses on the "Course Overview" page
  In order to quickly find a specific course

  Scenario: Successful Search for an Existing Course
    Given The Student is logged in and on the "Course Overview" page
    When The Student enters "Pembangunan Perangkat Lunak" into the "Search" field
    Then The Student should see the course "2025Ganjil - SII318 - Pembangunan Perangkat Lunak - S1 - Sistem Informasi - 2021 - I1" in the results
