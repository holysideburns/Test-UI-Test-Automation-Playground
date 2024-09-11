"""
Script Name: test_visbility_page.py
Description: This script tests the "Visibility" page at http://www.uitestingplayground.com/visibility.
Challenge: Use different ways to determine if buttons are visible or not.
"""

import pytest
from playwright.sync_api import expect
from pages.visibility_page import VisibilityPage

@pytest.fixture
def visibility_page(page) -> VisibilityPage:
    visibility_page = VisibilityPage(page)
    visibility_page.navigate()
    return visibility_page

@pytest.mark.visibility
def test_visibility_title(visibility_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Visibility' page,
        When the page is loaded,
        Then the page title should be 'Visibility'.
    """
    expect(visibility_page.title).to_have_text("Visibility")

@pytest.mark.visibility
def test_buttons_visibilities(visibility_page) -> None:
    """
    Test Scenario: Test Buttons Visibilities
        Given the user navigates to the 'Visibility' page,
        When the Hide button is clicked,
        Then no other button should be visible.
    """
    visibility_page.hide_button.click()
    
    assert (visibility_page.removed_button.count() == 0
            ), "Expected button to be removed."

    assert (visibility_page.zero_width_button.bounding_box()['width'] == 0
            ), "Expected button width to be zero."
    
    assert visibility_page.is_overlapping(
        visibility_page.overlapped_button.bounding_box(), 
        visibility_page.overlapping_layer.bounding_box()
        ), "Expected button to be overlapped."

    assert (visibility_page.get_opacity(visibility_page.transparent_button) == "0"
            ), "Expected button to be transparent."

    try:
        expect(visibility_page.invisible_button).to_have_css("visibility", "hidden")
    except AssertionError:
        raise AssertionError("Expected button to be hidden.")

    try:
        expect(visibility_page.not_displayed_button).to_have_css("display", "none")
    except AssertionError:
        raise AssertionError("Expected button to not be displayed.")
    
    try:
        expect(visibility_page.offscreen_button).not_to_be_in_viewport()
    except AssertionError:
        raise AssertionError("Expected button to be offscreen.")
