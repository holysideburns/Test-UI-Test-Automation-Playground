"""
Script Name: test_progress_bar_page.py
Description: This script tests the "Progress Bar" page at http://www.uitestingplayground.com/progressbar.
Challenge: Make sure that the script waits for the progress bar to reach 75%, but not longer than necessary.
Comment: Tried getting built in page.wait_for_function() to work, but gave up and used manual value polling in the end.
"""

import pytest
from playwright.sync_api import expect
from pages.progress_bar_page import ProgressBarPage

@pytest.fixture
def progress_bar_page(page) -> ProgressBarPage:
    progress_bar_page = ProgressBarPage(page)
    progress_bar_page.navigate()
    return progress_bar_page

@pytest.mark.progressbar
def test_progress_bar_title(progress_bar_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Progress Bar' page,
        When the page is loaded,
        Then the page title should be 'Progress Bar'.
    """
    expect(progress_bar_page.title).to_have_text("Progress Bar")

@pytest.mark.progressbar
def test_progress_bar_value(progress_bar_page) -> None:
    """
    Test Scenario: Verify that the progress bar is readable
        Given the user navigates to the 'Progress Bar' page,
        When the user clicks the start button,
        And the user waits for the progress bar to reach 75%,
        And the user clicks the stop button,
        Then the result value should be less than 5.
    """
    progress_bar_page.start_button.click()
    progress_bar_page.wait_for_progress("75")
    progress_bar_page.stop_button.click()
    end_result = progress_bar_page.get_result()
    assert end_result < 5, f"The time it took to click the stop button is too long: {end_result}"
    