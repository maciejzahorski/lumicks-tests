"""
The father of all Page Object classes - all of them should inherit from
the one below.
"""

from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver


class BasePage:
    """
    As above, the father from all Page Object classes.

    DO NOT create any its instances directly - use it as Java abstract class.
    """

    def __init__(self, driver: RemoteDriver):
        """
        :param driver: a refence to the current WebDriver object
        """
        self.driver = driver
