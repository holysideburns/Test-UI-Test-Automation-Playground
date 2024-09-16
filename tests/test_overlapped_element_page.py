"""
Script Name: test_overlapped_element_page.py
Description: This script tests the "Overlapped Element" page at http://www.uitestingplayground.com/overlapped.
Challenge: Make sure that a partially overlapped input element can be used.
"""

import pytest
from playwright.sync_api import expect
from pages.overlapped_element_page import OverlappedElementPage

@pytest.fixture
def overlapped_element_page(page) -> OverlappedElementPage:
    overlapped_element_page = OverlappedElementPage(page)
    overlapped_element_page.navigate()
    return overlapped_element_page

@pytest.mark.overlapped
def test_overlapped_element_page_title(overlapped_element_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Overlapped Element' page,
        When the page is loaded,
        Then the page title should be 'Overlapped Element'.
    """
    expect(overlapped_element_page.title).to_have_text("Overlapped Element")

@pytest.mark.overlapped
def test_overlapped_input_field(overlapped_element_page) -> None:
    """
    Test Scenario: Test Dynamic Link Click
        Given the user navigates to the 'Overlapped Element' page,
        When the user tries to enter text into the "Name" input field,
        Then the "Name" input field should contain that text.
    """
    test_string = "Jeff"
    overlapped_element_page.page.evaluate("""
        document.querySelector('div[style*="overflow-y: scroll"]').scrollBy(0, 200);
    """)
    try:
        overlapped_element_page.name_input.type(test_string)
    except Exception as e:
        print(f"Failed to input name: {e}")  
    expect(overlapped_element_page.name_input).to_have_value(test_string)