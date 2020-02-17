# Unit-integrated tests for Locator class

Feature: Locator object

    Background:
        When I open 'http://localhost:3000/' page

    Scenario Outline: Using method from Locator returns the WebElement
        Then I am able to find an existing element with Locator '<method>' method

        Examples:
        | method             |
        | get                |
        | get_when_present   |
        | get_when_visible   |
        | get_when_clickable |

    Scenario Outline: Using method from Locator raises an exception if the element wasn't found
        Then the '<exception_type>' is raised when element was not found using '<method>' method

        Examples:
        | method             | exception_type         |
        | get                | NoSuchElementException |
        | get_when_present   | TimeoutException       |
        | get_when_visible   | TimeoutException       |
        | get_when_clickable | TimeoutException       |

    Scenario Outline: Using method 'wait_until_invisible' results the proper behave of the tests
        Then the tests '<result>' when the element is '<state>'

        Examples:
        | result      | state       |
        | pass        | not visible |
        | raise error | visible     |
