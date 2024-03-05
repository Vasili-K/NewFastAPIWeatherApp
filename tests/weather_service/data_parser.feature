Feature: Parse Weather Data

  Scenario: Parse data - Successful
    Given Receive weather data for parsing
    When Service parse the received data
    Then Result is successful and equal to expected response

  Scenario Outline: Parse data - Successful
    Given Receive weather data for parsing
    When Field <field> remove from weather data
    Then I should see a KeyError error message

    Examples:
      | field   |
      | weather |
      | main    |
      | wind    |
