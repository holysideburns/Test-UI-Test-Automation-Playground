"""
Script Name: test_text_input_page.py
Description: This script tests the "Text Input" page at http://www.uitestingplayground.com/textinput.
Challenge: Ensure that the text box can be interacted with without using an event based input.
"""

import pytest
from playwright.sync_api import expect
from pages.text_input_page import TextInputPage


@pytest.fixture
def text_input_page(page) -> TextInputPage:
    text_input_page = TextInputPage(page)
    text_input_page.navigate()
    return text_input_page

@pytest.mark.textinput
def test_text_input_page_title(text_input_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Text Input' page,
        When the page is loaded,
        Then the page title should be 'Text Input'.
    """
    expect(text_input_page.title).to_have_text("Text Input")

@pytest.mark.textinput
def test_text_input(text_input_page) -> None:
    """
    Test Scenario: Test Text Input
        Given the user is on the 'Text Input' page,
        When they enter 'Test Value' into the textbox,
        And click the update button,
        Then the button's text should be updated to 'Test Value'.
    """
    input_value = "Test Value"
    expect(text_input_page.button).not_to_have_text(input_value)
    text_input_page.enter_text(input_value)
    text_input_page.click_button()
    expect(text_input_page.button).to_have_text(input_value)