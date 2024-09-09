from .base_page import BasePage
from playwright.sync_api import Locator

class LoadDelaysPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "loaddelay"
        self.title = self.page.locator("h3")
        self.delayed_button = self.page.get_by_role("button", name="Button Appearing After Delay")

    def navigate(self) -> None:
        super().navigate(self.path)

    def get_title(self) -> Locator:
        return self.title
    
    def click_delayed_button(self) -> None:
        self.delayed_button.click()