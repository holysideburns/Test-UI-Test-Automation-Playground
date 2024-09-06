
# Test - UI Test Automation Playground
This is a training project using Playwright with Python and Pytest that focuses on practicing test automation techniques on www.uitestingplayground.com.

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Edit `.env` and fill in any test credentials (Sample App requires the password `pwd`)
5. Run tests: `pytest` or `pytest -m <marker>` with one or more page markers in the following format:
   - `homepage`
   - `dynamicid`
   - `clientsidedelay`
   - Example: `pytest -m "homepage or dynamicid"`

## Authors
- [@holysideburns (Jimmy Pettersson)](https://github.com/holysideburns)

