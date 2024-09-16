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
def browser_context_args():
    return {
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {
        "headless": True  # Set to False to run in non-headless mode
    }