
# Playwright Test Automation - UI Test Automation Playground
This is my training project using Playwright with Python and Pytest that focuses on practicing test automation techniques on www.uitestingplayground.com.

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
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   └── 
├── tests/                             # Files containing tests to be run by `pytest`
   ├── test_home_page.py               # Tests site home page, marker `homepage`
   ├── test_dynamic_id_page.py         # Tests `Dynamic ID`, marker `dynamicid`
   ├── test_class_attribute_page.py    # Tests `Class Attribute`, marker `classattribute`
   ├── test_hidden_layers_page.py      # Tests `Hidden Layers`, marker `hiddenlayers`
   ├── test_load_delays_page.py        # Tests `Load Delays`, marker `loaddelays`
   ├── test_ajax_data_page.py          # Tests `AJAX Data`, marker `ajaxdata`
   ├── test_client_side_delay_page.py  # Tests `Client Side Delay`, marker `clientsidedelay`
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   └── 
└── config/                   # Configuration files
   └── config.py              # General configuration file for the project
├── .env (.env.example)       # Environment file, mainly for credentials
├── pytest.ini                # Configuration file for `pytest`
├── README.md                 # You're looking at it
└── requirements.txt          # Required Python modules to run project
```

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Run tests using `pytest` or `pytest -m <marker>` with one or more test markers, like this:
      - `pytest -m "homepage"`
      - `pytest -m "not homepage"`
      - `pytest -m "classattribute or dynamicid"`

## Author
- [@holysideburns (Jimmy Pettersson)](https://github.com/holysideburns)

