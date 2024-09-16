
# Playwright Test Automation - UI Test Automation Playground
This is my training project using Playwright with Python and Pytest that focuses on practicing test automation techniques on www.uitestingplayground.com.

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Run tests using `pytest` or `pytest -m <marker>` with one or more test markers, like this:
      - `pytest -m "homepage"`
      - `pytest -m "not homepage"`
      - `pytest -m "classattribute or dynamicid"`

### Running Tests In Parallel
I've included the optional module `pytest-xdist` in the requirements, which enables you to run tests in parallel.
Use the option `-n X`, where X is the number of processes to use.

### Test Report Generation
I've also included the optional module `pytest-reporter-html1` in the requirements, which enables the generation of an HTML report after a test run.
Use the option `--template=html1/index.html --report=report.html` to generate `report.html` in the project root.

## Project structure
```
project-root/
├── pages/                             # Page Object Model (POM) classes to be used by tests
   ├── base_page.py                    # Parent POM
   ├── home_page.py                    # POM for `/home`
   ├── dynamic_id_page.py              # POM for `/dynamicid`
   ├── class_attribute_page.py         # POM for `/classattr`
   ├── hidden_layers_page.py           # POM for `/hiddenlayers`
   ├── load_delays_page.py             # POM for `/loaddelay`
   ├── ajax_data_page.py               # POM for `/ajax`
   ├── client_side_delay_page.py       # POM for `/clientdelay`
   ├── click_page.py                   # POM for `/click`
   ├── text_input_page.py              # POM for `/textinput`
   ├── scrollbars_page.py              # POM for `/scrollbars`
   ├── dynamic_table_page.py           # POM for `/dynamictable`
   ├── verify_text_page.py             # POM for `/verifytext`
   ├── progress_bar_page.py            # POM for `/progressbar`
   ├── visibility_page.py              # POM for `/visibility`
   ├── sample_app_page.py              # POM for `/sampleapp`
   ├── mouse_over_page.py              # POM for `/mouseover`
   ├── nbsp_page.py                    # POM for `/nbsp`
   ├── overlapped_element_page.py      # POM for `/overlapped`
   ├── shadow_dom_page.py              # POM for `/shadowdom`
   ├── alerts_page.py                  # POM for `/alerts`
   └── file_upload_page.py             # POM for `/upload`
├── tests/                             # Files containing tests to be run by `pytest`
   ├── test_home_page.py               # Tests site home page, marker `homepage`
   ├── test_dynamic_id_page.py         # Tests `Dynamic ID`, marker `dynamicid`
   ├── test_class_attribute_page.py    # Tests `Class Attribute`, marker `classattribute`
   ├── test_hidden_layers_page.py      # Tests `Hidden Layers`, marker `hiddenlayers`
   ├── test_load_delays_page.py        # Tests `Load Delays`, marker `loaddelays`
   ├── test_ajax_data_page.py          # Tests `AJAX Data`, marker `ajaxdata`
   ├── test_client_side_delay_page.py  # Tests `Client Side Delay`, marker `clientsidedelay`
   ├── test_click_page.py              # Tests `Click`, marker `click`
   ├── test_text_input_page.py         # Tests `Text Input`, marker `textinput`
   ├── test_scrollbars_page.py         # Tests `Scrollbars`, marker `scrollbars`
   ├── test_dynamic_table_page.py      # Tests `Dynamic Table`, marker `dynamictable`
   ├── test_verify_text_page.py        # Tests `Verify Text`, marker `verifytext`
   ├── test_progress_bar_page.py       # Tests `Progress Bar`, marker `progressbar`
   ├── test_visibility_page.py         # Tests `Visibility`, marker `visibility`
   ├── test_sample_app_page.py         # Tests `Sample App`, marker `sampleapp`
   ├── test_mouse_over_page.py         # Tests `Mouse Over`, marker `mouseover` 
   ├── test_nbsp_page.py               # Tests `Non-Breaking Space`, marker `nbsp`
   ├── test_overlapped_page.py         # Tests `Overlapped Element`, marker `overlapped`
   ├── test_shadow_dom_page.py         # Tests `Shadow DOM`, marker `shadowdom`
   ├── test_alerts_page.py             # Tests `Alerts`, marker `alerts`
   └── test_file_upload_page.py        # Tests `File Upload`, marker `fileupload`
└── config/                   
   └── config.py              # General configuration file, mainly loads from .env file
├── .env (.env.example)       # Environment file, mainly for credentials and base URL
├── pytest.ini                # Configuration file for `pytest`
├── README.md                 # You're looking at it
└── requirements.txt          # Required Python modules to run the project
```

## Author
- [@holysideburns (Jimmy Pettersson)](https://github.com/holysideburns)

