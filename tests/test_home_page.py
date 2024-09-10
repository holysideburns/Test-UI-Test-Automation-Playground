"""
Script Name: test_home_page.py
Description: This script tests the "home" page on http://www.uitestingplayground.com/.
Challenge: None, but added  a couple of tests anyway.
"""

import pytest
from playwright.sync_api import expect
from config.config import Config
from pages.home_page import HomePage

@pytest.fixture
def home_page(page) -> HomePage:
    home_page = HomePage(page)
    home_page.navigate()
    return home_page

""" Test Scenario: Verify that he page title is 'UI Test AutomationPlayground'. """
@pytest.mark.homepage
def test_home_page_title(home_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the home page,
        When the page is loaded,
        Then the page title should be 'UI Test AutomationPlayground'.
    """
    expect(home_page.title).to_have_text("UI Test AutomationPlayground")

""" Test Scenario: Verify that the page is accessable at '/home'. """
@pytest.mark.homepage
def test_alternate_path(home_page) -> None:
    """
    Test Scenario: Test Alternate Path
        Given that the user navigates to /home,
        When the page is loaded,
        Then the URL should have /home at the end.
    """
    home_page.navigate_alternate_path()
    expect(home_page.page).to_have_url(Config.BASE_URL + "/home")
