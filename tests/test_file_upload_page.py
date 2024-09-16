"""
Script Name: test_file_upload_page.py
Description: This script tests the "File Upload" page at http://www.uitestingplayground.com/upload.
Challenge: Test drag & drop and Browse Files file upload functions.
"""
import os
import pytest
from playwright.sync_api import expect
from pages.file_upload_page import FileUploadPage

@pytest.fixture
def file_upload_page(page) -> FileUploadPage:
    file_upload_page = FileUploadPage(page)
    file_upload_page.navigate()
    return file_upload_page

@pytest.mark.fileupload
def test_file_upload_page_title(file_upload_page) -> None:
    """
    Test Scenario: Test Page Title
        Given the user navigates to the 'File Upload' page,
        When the page is loaded,
        Then the page title should be 'File Upload'.
    """
    expect(file_upload_page.title).to_have_text("File Upload")

@pytest.mark.skip(reason="WIP")
@pytest.mark.fileupload
def test_drag_n_drop_file_upload(file_upload_page) -> None:
    """
    Test Scenario: Test Drag & Drop File Upload
        Given the user navigates to the 'File Upload' page,
    """

@pytest.mark.fileupload
def test_browse_files_file_upload(file_upload_page) -> None:
    """
    Test Scenario: Test Browse Files File Upload
        Given the user navigates to the 'File Upload' page,
    """
    file_name = "test_file.pdf"
    file_path = os.path.abspath(file_name)
    file_upload_page.file_input.set_input_files(file_path)
    expect(file_upload_page.file_info).to_have_text(file_name)
   