"""
Script Name: test_class_attribute_page.py
Description: This script tests the "Class Attribute" page at http://www.uitestingplayground.com/classattr.
Challenge: Craft a reliable XPath selector that works on an element with more than one class reference.
"""

import pytest
from playwright.sync_api import expect
from pages.class_attribute_page import ClassAttributePage

@pytest.fixture
def class_attribute_page(page) -> ClassAttributePage:
    class_attribute_page = ClassAttributePage(page)
    class_attribute_page.navigate()
    return class_attribute_page

@pytest.mark.classattribute
def test_class_attribute_page_title(class_attribute_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Class Attribute' page,
        When the page is loaded,
        Then the page title should be 'Class Attribute'.
    """
    expect(class_attribute_page.title).to_have_text("Class Attribute")

@pytest.mark.classattribute
def test_blue_button(class_attribute_page) -> None:
    """
    Test Scenario: Test Text Input
        Given the user is on the 'Text Input' page,
        When the page is loaded,
        Then the button should be clickable using the 'btn-primer' class.
    """
    class_attribute_page.click_blue_button()
    expect(class_attribute_page.title).to_be_visible()