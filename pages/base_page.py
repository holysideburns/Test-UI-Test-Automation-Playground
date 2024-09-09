from playwright.sync_api import Page
from config.config import Config

class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = Config.BASE_URL

    def navigate(self, path: str = "") -> None:
        full_url = f"{self.base_url}/{path.lstrip('/')}"
        self.page.goto(full_url)