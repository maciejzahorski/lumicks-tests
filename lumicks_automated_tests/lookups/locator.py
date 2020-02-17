"""
Module responsible for getting WebElements. Contains:
  - `Locator` class - the wrapper for Selenium's WebElement class
  - `get_wait` function which return WebDriverWait object for fluent waits
    for operations which can be related to Selenium's WebDriver.
"""

from typing import Callable, List, Union

from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

WEB_ELEMENT_TYPE = Union[WebElement, List[WebElement]]


class Locator:
    """
    Wrapper for Selenium's WebElement class - offers shortcuts for getting
    the WebElements directly and with fluent waits. Allows to store a single
    WebElement or a list of them in a single object, with easy access to its
    finding methods.
    """

    def __init__(
            self,
            driver: RemoteDriver,
            selector: str,
            by: str = "css_selector",
            many: bool = False,
    ) -> None:
        """
        :param driver: a reference to the current WebDriver object
        :param selector: a selector which is used to locate an element
        :param by: a type of the selector
            Available types:
                - id
                - class_name
                - link_text
                - partial_link_text
                - tag_name
                - css_selector
                - xpath
            Default value: 'css_selector'
            Values given as this parameter can contain space instead of underscore.
                For example, both:
                    - 'css_selector'
                    - 'css selector'
                are valid values for 'by' parameter.
        :param many: should the Locator object refer to the single WebElement
            or to the list of WebElements
        """

        self.driver: RemoteDriver = driver
        self.selector: str = selector
        self.by: str = by
        self.many: bool = many

    def get(self) -> WEB_ELEMENT_TYPE:
        """
        Get a WebElement or a list of WebElements without any waiting.

        :raises selenium.common.exceptions.NoSuchElementException: if the element
            wasn't found
        """

        return getattr(
            self.driver,
            "find_element{}_by_{}".format("s" if self.many else "", self.by.replace(" ", "_")),
        )(self.selector)

    def get_when_present(self, wait_time: int = 15) -> WEB_ELEMENT_TYPE:
        """
        Returns a WebElement or a list of WebElements after its/their presence
        in the page code.

        :param wait_time: number of seconds to wait
        :raises: see - `_execute_wait_conditions` docs
        """

        func = getattr(
            expected_conditions,
            "presence_of_{}_located".format("all_elements" if self.many else "element"),
        )
        return self._execute_wait_conditions(wait_time, func, self.by, self.selector)

    def get_when_visible(self, wait_time: int = 15) -> WEB_ELEMENT_TYPE:
        """
        Returns a WebElement or a list of WebElements after its/their visibility
        in the browser (it means: element is present in the code and its size
        is greater than 0).

        :param wait_time: number of seconds to wait
        :raises: see - `_execute_wait_conditions` docs
        """

        func = getattr(
            expected_conditions,
            "visibility_of_{}_located".format("all_elements" if self.many else "element")
        )
        return self._execute_wait_conditions(wait_time, func, self.by, self.selector)

    def get_when_clickable(self, wait_time: int = 15) -> WEB_ELEMENT_TYPE:
        """
        Returns a WebElement when it's clickable.

        :param wait_time: number of seconds to wait
        :raises selenium.common.exceptions.TimeoutException: if the element isn't found
            as clickable after given time
        """

        func = expected_conditions.element_to_be_clickable
        return self._execute_wait_conditions(wait_time, func, self.by, self.selector)

    def wait_until_invisible(self, wait_time: int = 15) -> None:
        """
        Waits until the WebElement will stop to be visible on the page.

        :param wait_time: number of seconds to wait
        :raises selenium.common.exceptions.TimeoutException: if the element is still
            visible on the page after given time
        """

        (get_wait(self.driver, wait_time)
            .until_not(expected_conditions.visibility_of_element_located((
                self.by.replace("_", " "),
                self.selector,
            ))))

    def _execute_wait_conditions(
            self,
            wait_time: int,
            func: Callable,
            by: str,
            selector: str,
    ) -> WEB_ELEMENT_TYPE:
        """
        Wrapper for calling Selenium's `expected_conditions` functions with 'until'.

        :param wait_time: number of seconds to wait
        :param func: method to call (from `expected_conditions`)
        :param by: a type of the selector (see: docs in the __init__ method
            in this module)
        :param selector: a selector used to locate an element
        :return: a WebElement of a list of WebElements
        :raises selenium.common.exceptions.TimeoutException: if the condition
            isn't fulfilled in the given amount of the time
        """

        return get_wait(self.driver, wait_time).until(func((by.replace("_", " "), selector)))


def get_wait(driver: RemoteDriver, wait_time: int = 15) -> WebDriverWait:
    """
    Get the WebDriverWait object for current driver session.

    :param driver: the current WebDriver object
    :param wait_time: number of seconds to wait
    """

    # avoiding wait_time == 0
    wait_time = wait_time or 15
    return WebDriverWait(driver, wait_time)
