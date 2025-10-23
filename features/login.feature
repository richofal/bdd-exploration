Feature: Student Login

  In order to access courses and academic information
  As a Student
  I must be able to log into the Hebat platform

  Scenario: Successful Login with Valid Credentials
    
    Given The Student is on the "Hebat" login page
    When The Student enters a valid username into the "Username" field
    And The Student enters a valid password into the "Password" field
    And The Student clicks the "Log in" button
    Then The Student should be redirected to the Hebat system's "Home" page
    And The Student should see their courses information on the page