from .base_page import BasePage
from playwright.sync_api import Locator

class Scrollbars(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/scrollbars"
        self.title = self.page.locator("h3")
        self.button = self.page.locator("#hidingButton")

    def navigate(self) -> None:
        super().navigate(self.path)
    
    def scroll_to_button(self) -> None:
        try:
            self.button.scroll_into_view_if_needed()
        except Exception as e:
            print(f"Failed to scroll to button: {e}")

    def click_button(self) -> None:
        try:
            self.button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")