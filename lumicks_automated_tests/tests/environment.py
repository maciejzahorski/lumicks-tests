"""
Behave's environment file - defines Behave's hooks
"""

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from lumicks_automated_tests import LOG


def before_feature(context, feature):
    context.feature_name = feature.name


def before_scenario(context, scenario):
    context.scenario_name = scenario.name
    context.driver = webdriver.Chrome()

    try:
        context.driver.maximize_window()
    except WebDriverException:
        LOG.warning("Couldn't maximize browser's window")


def after_scenario(context, _):
    context.driver.quit()
