"""
Script Name: test_dynamic_id_page.py
Description: This script tests the "Dynamic ID" page on http://www.uitestingplayground.com/dynamicid.
Challenge: Interact with a button that uses a dynamic ID without using the ID.
"""

import pytest
from playwright.sync_api import expect
from pages.dynamic_id_page import DynamicIdPage

""" Test Scenario: Verify that the page title is 'Dynamic ID'. """
@pytest.mark.dynamicid

def test_dynamic_id_page_title(page) -> None:
    dynamicid_page = DynamicIdPage(page)
    dynamicid_page.navigate()
    expect(dynamicid_page.title).to_have_text("Dynamic ID")

""" Test Scenario: Verify that the button can be clicked without using its ID. """
@pytest.mark.dynamicid

def test_dynamic_id_button(page) -> None:
    dynamicid_page = DynamicIdPage(page)
    dynamicid_page.navigate()
    dynamicid_page.dynamicid_button.click()