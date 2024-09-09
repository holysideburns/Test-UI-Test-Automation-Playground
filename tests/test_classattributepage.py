"""
Script Name: test_classattributepage.py
Description: This script tests the "Class Attribute" page at http://www.uitestingplayground.com/classattr.
Challenge: Craft a reliable XPath selector that works on an element with more than one class reference.
"""

import pytest
from playwright.sync_api import expect
from pages.classattribute_page import ClassAttributePage

@pytest.mark.classattribute
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_classattribute_page_title(page) -> None:
    classattribute_page = ClassAttributePage(page)
    classattribute_page.navigate()
    expect(classattribute_page.get_title()).to_have_text("Class Attribute")

@pytest.mark.classattribute
#@pytest.mark.skip(reason="Skipping this test for now.")
def test_blue_button(page) -> None:
    classattribute_page = ClassAttributePage(page)
    classattribute_page.navigate()
    classattribute_page.click_blue_button()
    expect(classattribute_page.get_title()).to_be_visible()
    