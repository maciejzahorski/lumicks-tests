from behave import then, when
from selenium.common import exceptions
from selenium.webdriver.remote.webelement import WebElement

from lumicks_automated_tests.page_objects.pages import upload


@when("I open '{url}' page")
def step_impl(context, url):
    context.driver.get(url)
    context.page = upload.UploadPage(context.driver)


@then("I am able to find an existing element with Locator '{method}' method")
def step_impl(context, method):
    locator_obj = context.page.input_drag_drop
    element = None
    error_msg = "{} generated = '{}' method doesn't work"

    if method.lower() == "get":
        try:
            element = locator_obj.get()
        except exceptions.NoSuchElementException:
            raise AssertionError(error_msg.format("NoSuchElementException", method))
    elif method.lower() in ("get_when_present", "get_when_visible", "get_when_clickable"):
        try:
            element = getattr(locator_obj, method)()
        except exceptions.TimeoutException:
            raise AssertionError(error_msg.format("TimeoutException", method))

    assert type(element) == WebElement, \
        f"Element returned by {method} is not of expected type"


@then("the '{exception}' is raised when element was not found using '{method}' method")
def step_impl(context, exception, method):
    locator_obj = context.page.non_existing_element

    try:
        getattr(locator_obj, method)()
    except Exception as err:
        assert type(err) == getattr(exceptions, exception),\
            "Unexpected type of exception. Expected: {}, got: {}".format(exception, type(err))


@then("the tests '{result}' when the element is '{state}'")
def step_impl(context, result, state):
    if state == "visible":
        locator_obj = context.page.input_drag_drop
    else:
        locator_obj = context.page.non_existing_element

    try:
        locator_obj.wait_until_invisible()
    except Exception as err:
        if result == "pass":
            raise AssertionError(
                "Got unexpected TimeoutException - the element is visible but it shouldn't",
            )
        assert type(err) == exceptions.TimeoutException, \
            "Unexpected type of exception. Expected: TimeoutException, got: {}".format(type(err))
    else:
        if result == "raise error":
            raise AssertionError("The exception wasn't raised but it should")
