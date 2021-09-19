Feature: TrelloTest
  To Test the Trello Application

  Scenario: To Test the Trello Application Functionality
    Given launch chrome browser
    When open Trello URL
    Then Login into Trello
    Then Create a new board
    Then Create four Lists as Not Started, In Progress, QA, Done
    Then Create four Cards.Card 1, Card 2, Card 3, Card 4 under the list Not Started
    Then Move Card 2 to In Progress
    Then Move Card 3 to QA
    Then Move Card 2 under QA
    Then Open Card 1 and Assign it to the current logged in user and then leave a comment on Card 1 saying “I am done”
    And close the chrome browser