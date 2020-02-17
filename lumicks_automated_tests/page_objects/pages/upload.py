from lumicks_automated_tests.lookups.locator import Locator
from lumicks_automated_tests.page_objects.pages import base


class UploadPage(base.BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.input_drag_drop = Locator(driver=driver, selector="div.ant-upload-drag-container")
        self.non_existing_element = Locator(driver=driver, selector="div.non-existing.thing")
