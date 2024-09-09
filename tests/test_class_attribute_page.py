"""
Script Name: test_class_attribute_page.py
Description: This script tests the "Class Attribute" page at http://www.uitestingplayground.com/classattr.
Challenge: Craft a reliable XPath selector that works on an element with more than one class reference.
"""

import pytest
from playwright.sync_api import expect
from pages.class_attribute_page import ClassAttributePage

@pytest.mark.classattribute
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_class_attribute_page_title(page) -> None:
    class_attribute_page = ClassAttributePage(page)
    class_attribute_page.navigate()
    expect(class_attribute_page.get_title()).to_have_text("Class Attribute")

@pytest.mark.classattribute
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_blue_button(page) -> None:
    class_attribute_page = ClassAttributePage(page)
    class_attribute_page.navigate()
    class_attribute_page.click_blue_button()
    expect(class_attribute_page.get_title()).to_be_visible()
    