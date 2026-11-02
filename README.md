# 🧪 Hybrid API & UI Test Automation Framework

A professional, decoupled test automation framework designed using Python to validate web interface workflows and verify REST API transaction integrity. This repository features full continuous integration capabilities to execute tests headless inside modern CI/CD pipelines.

## 🛠️ Tech Stack & Architecture
* **Core Language:** Python 3.10+
* **Execution Engine:** Pytest (Test discovery, parameterization, and runner layers)
* **UI Automation Engine:** Playwright (Fast, isolated, out-of-process browser control)
* **API Validation Layer:** Requests (HTTP transaction tracking and response parsing)
* **Continuous Integration:** GitHub Actions (Automated workflow runner)
* **Reporting Architecture:** Allure Framework (Interactive test execution metrics)

---

## ⚡ Continuous Integration & Automation (CI/CD)
This framework features an integrated **GitHub Actions pipeline** configured to automate validation runs. 
* **Pipeline Trigger:** Executes automatically on every `git push` or `pull request` targeting the `main` branch.
* **Headless Infrastructure:** Automatically provisions a Linux server workspace, instantiates target runtime dependencies, sets up the web driver binary layers, and executes the suite end-to-end.
* **Artifact Storage:** Saves all raw test artifacts automatically upon run completion for debugging evaluations.

---

## 📋 Target Test Coverage
* **Frontend Web UI (`/tests/ui`):** Interfaces with the TodoMVC web application engine to validate input interaction boundaries, form submission state management, and real-time DOM element visibility metrics.
* **Backend REST API (`/tests/api`):** Dispatches asynchronous network transactions against DummyJSON servers to isolate schema validation rules, evaluate HTTP communication headers, and confirm structural JSON key/value mapping distributions.

---

## 📁 Project Structure
```text
qa_automation_interview_project/
├── .github/
│   └── workflows/
│       └── pytest_ci.yml       # GitHub Actions pipeline workflow configuration
├── tests/
│   ├── ui/
│   │   └── test_todo_ui.py     # Frontend web functional UI validations
│   └── api/
│       └── test_products_api.py # Backend REST API integration test coverage
├── requirements.txt            # Explicit framework dependency matrix
├── pytest.ini                  # Central configuration rules for execution runs
├── .gitignore                  # Controls file exclusion logic (blocking logs, .venv)
└── README.md                   # Technical portfolio documentation showcase
```

---

## 🚀 Local Environment Installation & Setup

### 1. Initialize Development Environment
Clone this repository to your local workspace, open the project directory in VS Code, and spin up an isolated virtual environment:

**Windows PowerShell:**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
*(If execution policies restrict script run permissions on PowerShell, use Command Prompt: `.venv\Scripts\activate.bat`)*

**macOS / Linux terminal:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Framework Package Dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m playwright install chromium
```

---

## 🎯 Test Execution Management

**Execute the full test suite:**
```bash
pytest -v
```

**Isolate execution to Frontend UI tests only:**
```bash
pytest -v tests/ui
```

**Isolate execution to Backend API components only:**
```bash
pytest -v tests/api
```

---

## 📊 Allure Execution Metrics Reporting

To compile historical framework performance outputs and inspect individual steps inside a visual, human-readable report dashboard:

1. Execute the test runner suite while targeting an output metrics repository directory:
   ```bash
   pytest -v --alluredir=allure-results
   ```
2. Serve and render the static execution results inside your default system browser workspace:
   ```bash
   allure serve allure-results
   ```
*(Note: Visual server compilation requires the Allure CLI binaries to be configured on your system environment's PATH).*

---

## 🛠️ Core Troubleshooting
* **`pytest` command rejection:** Execute using explicitly bound Python module parameters: `python -m pytest -v`.
* **Missing browser binaries error:** Ensure driver instances are registered locally by executing `python -m playwright install chromium`.
* **Dependency mapping exceptions:** Confirm your terminal console has successfully activated your virtual environment context (`(.venv)` prefix visible), then re-run `pip install -r requirements.txt`.

---

## 💼 Professional Interview Overview
"I engineered a decoupled, hybrid test automation framework using Python, Pytest, Playwright, and Requests to build isolated regression boundaries for web application frontends and underlying REST API endpoints. The framework features an active Continuous Integration architecture driven by GitHub Actions to systematically run full regression verification matrices on new code updates. Test output cycles are bound directly to an Allure reporting architecture, generating interactive dashboards highlighting test step transitions, transaction data tracking, and test pass/fail breakdown metrics."
