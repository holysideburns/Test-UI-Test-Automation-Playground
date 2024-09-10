"""
Script Name: test_text_input_page.py
Description: This script tests the "Text Input" page at http://www.uitestingplayground.com/textinput.
Challenge: Ensure that the text box can be interacted with without using an event based input.
"""

import pytest
from playwright.sync_api import expect
from pages.text_input_page import TextInput

@pytest.fixture
def text_input_page(page) -> TextInput:
    text_input_page = TextInput(page)
    text_input_page.navigate()
    return text_input_page

@pytest.mark.textinput
def test_text_input_page_title(text_input_page) -> None:
    expect(text_input_page.title).to_have_text("Text Input")

@pytest.mark.textinput
def test_text_input(text_input_page) -> None:
    """Test Scenario: Verify that text can be entered into the textbox 
    and that clicking the button sets the button name to the text."""
    input_value = "Test Value"
    expect(text_input_page.button).not_to_have_text(input_value)
    text_input_page.enter_text(input_value)
    text_input_page.click_button()
    expect(text_input_page.button).to_have_text(input_value)