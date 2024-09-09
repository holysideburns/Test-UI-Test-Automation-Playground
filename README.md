
# Test - UI Test Automation Playground
This is a training project using Playwright with Python and Pytest that focuses on practicing test automation techniques on www.uitestingplayground.com.

## Project structure
```
project-root/
├── pages/              # Page Object Model files to be used by tests
   ├── base_page.py     # Parent Page Object Model
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
   ├── 
   └── 
├── tests/              # Files containint tests to be run by `pytest`
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
├── utils/
└── config/             # Configuration files
   └── config.py        # Configuration file
├── pytest.ini          # Configuration file for `pytest`
├── .env (.env.example) # Environment file, mainly for credentials
├── requirements.txt    # Required Python modules to run project
└──
```
## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Run tests: `pytest` or `pytest -m <marker>` with one or more page markers in the following format:
   - `homepage`
   - `dynamicid`
   - `clientsidedelay`
   - Example: `pytest -m "homepage or dynamicid"`

## Authors
- [@holysideburns (Jimmy Pettersson)](https://github.com/holysideburns)

