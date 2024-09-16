from .base_page import BasePage
from playwright.sync_api import Locator

class MouseOverPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/mouseover"
        self.title = self.page.locator("h3")
        self.click_count = self.page.locator("#clickCount")
        self.link = self.page.locator("a[title='Click me']")

    def navigate(self) -> None:
        super().navigate(self.path)

    def click_link(self) -> None:
        try:
            self.link.hover(timeout=500)
        except Exception as e:
            print(f"Failed to hover over original link: {e}")
        new_link = self.page.locator("a[title='Active Link']")
        try:
            new_link.click()
        except Exception as e:
            print(f"Failed to click new link: {e}")