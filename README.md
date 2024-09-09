
# Playwright Test Automation - UI Test Automation Playground
This is my training project using Playwright with Python and Pytest that focuses on practicing test automation techniques on www.uitestingplayground.com.

## Project structure
```
project-root/
├── pages/                       # Page Object Model (POM) files to be used by tests
   ├── base_page.py              # Parent POM
   ├── home_page.py              # POM for `/home`
   ├── dynamicid_page.py         # POM for `/dynamicid`
   ├── classattribute_page.py    # POM for `/classattr`
   ├── hiddenlayers_page.py      # POM for `/hiddenlayers`
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   ├── 
   └── 
├── tests/                       # Files containing tests to be run by `pytest`
   ├── test_homepage.py          # Tests site home page, marker `homepage`
   ├── test_dynamicid.py         # Tests `Dynamic ID`, marker `dynamicid`
   ├── test_classattribute.py    # Tests `Class Attribute`, marker `classattribute`
   ├── test_hiddenlayers.py      # Tests `Hidden Layers`, marker `hiddenlayers`
   ├── 
   ├── 
   ├── 
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

