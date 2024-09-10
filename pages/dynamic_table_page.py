from .base_page import BasePage
from playwright.sync_api import Locator

class DynamicTable(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.path = "/dynamictable"
        self.title = self.page.locator("h3")
        self.chrome_cpu_text = self.page.locator(".bg-warning")

    def navigate(self) -> None:
        super().navigate(self.path)
    
    def get_process_value(self, process: str, metric: str) -> str:
        row = self.page.locator(f'div[role="row"]:has(span[role="cell"]:text-is("{process}"))')
        cells = row.locator('span[role="cell"]').all()
        headers = self.page.locator('div[role="row"] > span[role="columnheader"]').all()
        target_column_index = next(i for i, header in enumerate(headers) if header.inner_text() == metric)
        return cells[target_column_index].inner_text()


        