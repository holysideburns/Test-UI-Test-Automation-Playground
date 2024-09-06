"""
Script Name: test_homepage.py
Description: This script tests the "home" page on http://www.uitestingplayground.com/.
Challenge: None, but added  a couple of tests anyway.
"""

import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from config.config import Config

@pytest.mark.skip(reason="Skipping this test for now.")
def test_homepage_title(page):
    home_page = HomePage(page)
    home_page.navigate()
    expect(home_page.get_title()).to_have_text("UI Test AutomationPlayground")

@pytest.mark.skip(reason="Skipping this test for now.")
def test_alternate_path(page):
    home_page = HomePage(page)
    home_page.navigate_alternate_path()
    expect(page).to_have_url(Config.BASE_URL + "/home")