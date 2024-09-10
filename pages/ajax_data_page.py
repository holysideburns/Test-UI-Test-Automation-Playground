from .base_page import BasePage
from playwright.sync_api import Locator

class AjaxDataPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/ajax"
        self.title = self.page.locator("h3")
        self.ajax_button = self.page.locator("#ajaxButton")
        self.ajax_message = self.page.get_by_text("Data loaded with AJAX get")

    def navigate(self) -> None:
        super().navigate(self.path)

    def get_title(self) -> Locator:
        return self.title
    
    def click_ajax_button(self) -> None:
        self.ajax_button.click()

    def get_ajax_message(self) -> Locator:
        return self.ajax_message