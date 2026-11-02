# QA Automation Practice Project — UI + API + Allure

A beginner-friendly project using **Python + Playwright + Pytest + Requests + Allure**.

## What this project tests
- UI: opens the TodoMVC demo, adds a todo, and verifies it appears.
- API: sends a GET request to DummyJSON and validates the status code and response structure.
- Reporting: Pytest produces Allure result files; Allure CLI displays the report.

> This is a learning/portfolio project. The public demo website and public API require an internet connection and may change.

## 1. Prerequisites
- Python 3.10+ (Python 3.14 may work depending on package compatibility)
- VS Code
- Internet access
- Java installed if you want to run the Allure CLI
- Allure command-line tool installed for `allure serve`

Check:
```bash
python --version
```

## 2. Open the project
Extract the ZIP. In VS Code, open the `qa_automation_interview_project` folder.
Open Terminal → New Terminal.

## 3. Create and activate a virtual environment

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt:
```bat
.venv\Scripts\activate.bat
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 4. Install dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install chromium
```

## 5. Run the tests
Run everything:
```bash
pytest -v
```

Run only UI:
```bash
pytest -v tests/ui
```

Run only API:
```bash
pytest -v tests/api
```

## 6. Generate the Allure report
First run tests and create Allure result files:
```bash
pytest -v --alluredir=allure-results
```

Then open the report:
```bash
allure serve allure-results
```

`allure serve` requires the Allure CLI. If you have not installed the CLI, you can still run tests and inspect the terminal output. The `allure-results` folder contains raw report data, not the final HTML report.

## Project structure
```text
qa_automation_interview_project/
├── tests/
│   ├── ui/
│   │   └── test_todo_ui.py
│   └── api/
│       └── test_products_api.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

## Walkthrough: UI test
1. Pytest discovers files named `test_*.py`.
2. The `page` fixture is provided by `pytest-playwright`.
3. `page.goto(...)` opens the TodoMVC demo.
4. `get_by_placeholder(...)` locates the new-todo input.
5. `fill(...)` enters a todo title.
6. `press("Enter")` submits it.
7. `expect(...).to_be_visible()` verifies the todo appears.

## Walkthrough: API test
1. `requests.get(...)` sends an HTTP GET request.
2. `timeout=10` prevents the request from waiting indefinitely.
3. `assert response.status_code == 200` validates the HTTP status.
4. `response.json()` converts the JSON response to Python data.
5. The remaining assertions validate the response structure and product data.

## Common errors
- **`pytest` not recognized:** run `python -m pytest -v`.
- **Browser executable missing:** run `python -m playwright install chromium`.
- **Import error:** activate the virtual environment and run `pip install -r requirements.txt`.
- **API timeout/network error:** check internet access and rerun; public endpoints can be temporarily unavailable.
- **`allure` not recognized:** install the Allure CLI and ensure it is on PATH. Tests can still run without the CLI, but the report cannot be opened with `allure serve`.

## Interview explanation (truthful)
"I built a beginner-level practice project using Python, Playwright, Pytest, Requests, and Allure. The UI test adds a todo and verifies it is displayed. The API test checks a GET response's status code and JSON structure. Pytest executes the tests, and the Allure adapter generates result files that can be viewed with the Allure CLI. I am using this project to practise automation fundamentals and framework structure."
