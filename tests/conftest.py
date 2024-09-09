import sys, os
import pytest
from config.config import Config

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def pytest_configure(config) -> None:
    """Validate configuration before tests run"""
    Config.validate()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args) -> None:
    return {
        **browser_context_args,
        "headless": True,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }