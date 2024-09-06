import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from config.config import Config

def test_homepage_title(page):
    home_page = HomePage(page)
    home_page.navigate()
    expect(home_page.get_title()).to_have_text("UI Test AutomationPlayground")

def test_base_url(page):
    home_page = HomePage(page)
    home_page.navigate()
    expect(page).to_have_url(Config.BASE_URL + "/")