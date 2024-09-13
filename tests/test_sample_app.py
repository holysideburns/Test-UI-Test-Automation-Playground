"""
Script Name: test_sample_app_page.py
Description: This script tests the "Sample App" page at http://www.uitestingplayground.com/sampleapp.
Challenge: Fill in user credentials and log in.
"""

import pytest
from playwright.sync_api import expect
from pages.sample_app_page import SampleAppPage
from config.config import Config

@pytest.fixture
def sample_app_page(page) -> SampleAppPage:
    sample_app_page = SampleAppPage(page)
    sample_app_page.navigate()
    return sample_app_page

@pytest.mark.sampleapp
def test_sample_app_page_title(sample_app_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'Sample App' page,
        When the page is loaded,
        Then the page title should be 'Sample App'.
    """
    expect(sample_app_page.title).to_have_text("Sample App")

@pytest.mark.sampleapp
def test_successful_login(sample_app_page) -> None:
    """
    Test Scenario: Test Successful Login
        Given the user navigates to the 'Sample App' page,
        When the user fills in VALID user name and password,
        And the user clicks the log in button,
        Then the user should be logged in.
    """
    sample_app_page.input_user_name(Config.TEST_USERNAME)
    sample_app_page.input_password(Config.TEST_PASSWORD)
    sample_app_page.click_login_button()
    expect(sample_app_page.login_status).to_have_text(f"Welcome, {Config.TEST_USERNAME}!")

@pytest.mark.sampleapp
def test_unsuccessful_login(sample_app_page) -> None:
    """
    Test Scenario: Test Unsuccessful Login
        Given the user navigates to the 'Sample App' page,
        When the user fills in INVALID user name and password,
        And the user clicks the log in button,
        Then the user should NOT be logged in.
    """
    sample_app_page.input_user_name(Config.TEST_USERNAME)
    sample_app_page.input_password("invalid_password")
    sample_app_page.click_login_button()
    expect(sample_app_page.login_status).to_have_text(f"Invalid username/password")