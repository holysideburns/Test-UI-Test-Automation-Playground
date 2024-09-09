"""
Script Name: test_dynamic_id_page.py
Description: This script tests the "Dynamic ID" page on http://www.uitestingplayground.com/dynamicid.
Challenge: Interact with a button that uses a dynamic ID without using the ID.
"""

import pytest
from playwright.sync_api import expect
from pages.dynamic_id_page import DynamicIdPage

@pytest.mark.dynamicid
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_dynamicid_page_title(page) -> None:
    dynamicid_page = DynamicIdPage(page)
    dynamicid_page.navigate()
    expect(dynamicid_page.get_title()).to_have_text("Dynamic ID")

@pytest.mark.dynamicid
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_dynamicid_button(page) -> None:
    dynamicid_page = DynamicIdPage(page)
    dynamicid_page.navigate()
    dynamicid_page.dynamicid_button.click()