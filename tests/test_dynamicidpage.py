"""
Script Name: test_dynamicidpage.py
Description: This script tests the "Dynamic ID" subpage on http://www.uitestingplayground.com/.
Challenge: Interact with a button that uses a dynamic ID without using the ID.
"""

import pytest
from playwright.sync_api import expect
from pages.dynamicid_page import DynamicIdPage
from config.config import Config

@pytest.mark.dynamicid
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_dynamicidpage_title(page):
    dynamicid_page = DynamicIdPage(page)
    dynamicid_page.navigate()
    expect(dynamicid_page.get_title()).to_have_text("Dynamic ID")

@pytest.mark.dynamicid
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_dynamicid_button(page):
    dynamicid_page = DynamicIdPage(page)
    dynamicid_page.navigate()
    dynamicid_page.dynamicid_button.click()