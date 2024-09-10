from .base_page import BasePage
from playwright.sync_api import Locator

class TextInput(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "textinput"
        self.title = self.page.locator("h3")
        self.button = self.page.locator("#updatingButton")
        self.textbox = self.page.locator("#newButtonName")

    def navigate(self) -> None:
        super().navigate(self.path)

    def get_title(self) -> Locator:
        return self.title
    
    def get_button(self) -> Locator:
        return self.button

    def get_textbox(self) -> Locator:
        return self.textbox
    
    def click_button(self) -> None:
        self.button.click()

    def enter_text(self, input) -> None:
        self.textbox.fill(input)