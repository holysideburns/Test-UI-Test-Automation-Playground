from .base_page import BasePage
from playwright.sync_api import Locator

class TextInputPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/textinput"
        self.title = self.page.locator("h3")
        self.button = self.page.locator("#updatingButton")
        self.textbox = self.page.locator("#newButtonName")

    def navigate(self) -> None:
        super().navigate(self.path)
    
    def click_button(self) -> None:
        try:
            self.button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")

    def enter_text(self, input: str) -> None:
        try:
            self.textbox.fill(input)
        except Exception as e:
            print(f"Failed to fill textbox: {e}")