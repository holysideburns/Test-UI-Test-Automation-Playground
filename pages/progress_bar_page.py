import time
from .base_page import BasePage
from playwright.sync_api import Locator

class ProgressBarPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/progressbar"
        self.title = self.page.locator("h3")
        self.start_button = self.page.locator("#startButton")
        self.stop_button = self.page.locator("#stopButton")
        self.progress_bar = self.page.locator('#progressBar')
        self.result_text = self.page.locator("#result")

    def navigate(self) -> None:
        super().navigate(self.path)

    def wait_for_progress(self, target_percentage: str, timeout: int = 30000) -> None:
        target_percentage = int(target_percentage.rstrip("%"))
        start_time = time.time()
        while time.time() - start_time < timeout / 1000:
            value = int(self.progress_bar.get_attribute('aria-valuenow'))
            if value >= target_percentage:
                return
            time.sleep(0.5)
        raise AssertionError(f"Progress bar value did not reach {target_percentage} within {timeout} ms")

    def get_result(self) -> int:
        result_text = self.result_text.text_content()
        result_value = result_text.split(",")[0].split(":")[1].strip()
        return int(result_value)