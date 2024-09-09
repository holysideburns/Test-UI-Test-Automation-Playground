from .base_page import BasePage
from playwright.sync_api import Locator

class HiddenLayersPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "hiddenlayers"
        self.title = self.page.locator("h3")
        self.green_button = self.page.locator("#greenButton")

    def navigate(self) -> None:
        super().navigate(self.path)

    def get_title(self) -> Locator:
        return self.title
    
    def get_green_button(self) -> Locator:
        return self.green_button
    
    def click_green_button(self) -> None:
        self.green_button.click()