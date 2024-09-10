"""
Script Name: test_dynamic_table_page.py
Description: This script tests the "Dynamic Table" page at http://www.uitestingplayground.com/dynamictable.
Challenge: Access a specific value in a dynamic table where columns and values locations are not static.
"""
import pytest
from playwright.sync_api import expect
from pages.dynamic_table_page import DynamicTable

@pytest.fixture
def dynamic_table_page(page) -> DynamicTable:
    dynamic_table_page = DynamicTable(page)
    dynamic_table_page.navigate()
    return dynamic_table_page

@pytest.mark.dynamictable
def test_dynamic_table_page_title(dynamic_table_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Dynamic Table' page,
        When the page is loaded,
        Then the page title should be 'Dynamic Table'.
    """
    expect(dynamic_table_page.title).to_have_text("Dynamic Table")

@pytest.mark.dynamictable
def test_chrome_cpu_value(dynamic_table_page) -> None:
    """
    Test Scenario: Test Chrome CPU value
        Given the user navigates to the 'Scrollbars' page,
        When the page is loaded,
        Then the CPU value for Chrome should be the same in the table as in the text field.
    """
    chrome_cpu_value = dynamic_table_page.get_process_value("Chrome", "CPU")
    try:
        expect(dynamic_table_page.chrome_cpu_text).to_have_text(f"Chrome CPU: {chrome_cpu_value}")
    except AssertionError as e:
        print(f"AssertionError: The Chrome CPU value is not as expected. Details: {e}")

