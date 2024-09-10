"""
Script Name: test_dynamic_id_page.py
Description: This script tests the "Dynamic ID" page on http://www.uitestingplayground.com/dynamicid.
Challenge: Interact with a button that uses a dynamic ID without using the ID.
"""

import pytest
from playwright.sync_api import expect
from pages.dynamic_id_page import DynamicIdPage

@pytest.fixture
def dynamicid_page(page) -> DynamicIdPage:
    dynamicid_page = DynamicIdPage(page)
    dynamicid_page.navigate()
    return dynamicid_page

@pytest.mark.dynamicid
def test_dynamic_id_page_title(dynamicid_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Dynamic ID' page,
        When the page is loaded,
        Then the page title should be 'Dynamic ID'.
    """
    expect(dynamicid_page.title).to_have_text("Dynamic ID")

@pytest.mark.dynamicid
def test_dynamic_id_button(dynamicid_page) -> None:
    """
    Test Scenario: Test Clicking Button Without Using ID
        Given the user is on the 'Dynamic ID' page,
        When the page is loaded,
        Then the button should be clickable using a locator that is not ID.
    """
    dynamicid_page.dynamicid_button.click()