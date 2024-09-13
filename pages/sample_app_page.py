from .base_page import BasePage
from playwright.sync_api import Locator

class SampleAppPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/sampleapp"
        self.title = self.page.locator("h3")
        self.user_name_input = self.page.locator('input[name="UserName"]')
        self.password_input = self.page.locator('input[name="Password"]')
        self.login_button = self.page.locator('#login')
        self.login_status = self.page.locator('#loginstatus')

    def navigate(self) -> None:
        super().navigate(self.path)

    def click_login_button(self) -> None:
        try:
            self.login_button.click()
        except Exception as e:
            print(f"Failed to click button: {e}")

    def input_user_name(self, user_name: str) -> None:
        try:
            self.user_name_input.fill(user_name)
        except Exception as e:
            print(f"Failed to input user name {user_name}: {e}")

    def input_password(self, password: str) -> None:
        try:
            self.password_input.fill(password)
        except Exception as e:
            print(f"Failed to input password {password}: {e}")