# Selenium Python Ecommerce Automation Framework

Professional Selenium WebDriver automation framework using Python, PyTest, pytest-bdd, Page Object Model, JSON test data, screenshots, HTML reports, and GitHub Actions CI.

Application under test: https://www.saucedemo.com/

## Why this project is useful

This project is designed for a fresher or junior QA automation role where interviewers expect clean Selenium scripts, framework understanding, test case design, reporting, debugging, and CI/CD awareness.

It covers:

- Page Object Model framework design
- Selenium WebDriver with Python
- PyTest test runner
- pytest-bdd Gherkin scenarios
- Data-driven testing with JSON test data
- Smoke, sanity, and regression test suites
- Explicit waits
- Screenshot capture on failure
- HTML test reports
- Chrome and Firefox execution
- GitHub Actions CI pipeline

## Framework structure

```text
selenium-python-ecommerce-automation-framework/
|
|-- pages/
|   |-- base_page.py
|   |-- login_page.py
|   |-- products_page.py
|   |-- cart_page.py
|   `-- checkout_page.py
|
|-- tests/
|   |-- test_login.py
|   |-- test_products.py
|   |-- test_cart.py
|   `-- test_checkout.py
|
|-- bdd/
|   |-- features/
|   |   |-- login.feature
|   |   `-- checkout.feature
|   `-- steps/
|       |-- test_login_steps.py
|       `-- test_checkout_steps.py
|
|-- test_data/
|   `-- users.json
|
|-- utils/
|   |-- config_reader.py
|   |-- data_reader.py
|   `-- screenshot_helper.py
|
|-- reports/
|-- screenshots/
|-- .github/workflows/selenium-tests.yml
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
|-- README.md
`-- .gitignore
```

## Setup

Use Python 3.10 or newer.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run tests

Run the complete suite:

```bash
pytest
```

Run smoke tests:

```bash
pytest -m smoke
```

Run sanity tests:

```bash
pytest -m sanity
```

Run regression tests:

```bash
pytest -m regression
```

Run only traditional PyTest tests:

```bash
pytest tests
```

Run only BDD scenarios:

```bash
pytest bdd/steps -m bdd
```

Run tests on Chrome:

```bash
pytest --browser chrome
```

Run tests on Firefox:

```bash
pytest --browser firefox
```

Run headless tests:

```bash
pytest --browser chrome --headless
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

Override the base URL:

```bash
pytest --base-url=https://www.saucedemo.com/
```

## What is automated

- Valid login test
- Negative login test for locked and invalid users
- Product listing validation
- Add to cart test
- Checkout flow test
- BDD login scenario
- BDD checkout scenario

## Requirement analysis and regression planning

The main business requirement is that a valid SauceDemo user should be able to log in, view products, add an item to the cart, and complete checkout. The negative requirement is that blocked or invalid users should not enter the application.

From these requirements, the framework creates smoke tests for the most critical happy paths, sanity tests for quick build validation, and regression tests for broader functional coverage. This is the same mindset used in Agile in-sprint automation: automate stable high-value scenarios early, run smoke tests frequently, and keep regression tests ready for release validation.

## File and folder explanation

`pages/` contains Page Object Model classes. Each page class stores locators and actions for one page, so test files stay readable.

`base_page.py` contains reusable Selenium actions such as click, enter text, get text, and explicit waits.

`login_page.py` automates username, password, login, and login error message behavior.

`products_page.py` automates product listing, add to cart, and cart navigation.

`cart_page.py` validates cart products and moves the user to checkout.

`checkout_page.py` fills checkout information, finishes checkout, and validates order confirmation.

`tests/` contains PyTest test cases for login, products, cart, and checkout.

`bdd/features/` contains Gherkin feature files written in business-readable Given/When/Then format.

`bdd/steps/` connects Gherkin steps to Selenium Python code using pytest-bdd.

`test_data/users.json` stores usernames, passwords, product names, and checkout data separately from test scripts.

`utils/config_reader.py` stores reusable project paths and the base URL.

`utils/data_reader.py` reads JSON test data.

`utils/screenshot_helper.py` saves screenshots when tests fail.

`conftest.py` defines the browser driver fixture, command-line options, and screenshot-on-failure hook.

`pytest.ini` defines test paths, markers, default report generation, and PyTest settings.

`.github/workflows/selenium-tests.yml` runs the tests automatically in GitHub Actions on Chrome and Firefox.

`reports/` stores generated HTML test reports.

`screenshots/` stores failure screenshots.

## How Selenium, PyTest, POM, BDD, data, reports, and CI are used

Selenium WebDriver controls Chrome or Firefox and performs real browser actions like typing, clicking, reading text, and navigating pages.

PyTest is the main test runner. It provides fixtures, markers, parametrization, assertions, and command-line execution.

Page Object Model separates test logic from page locators. Tests call methods like `login()` and `add_product_to_cart()` instead of directly using Selenium locators everywhere.

BDD is implemented with pytest-bdd. Feature files describe behavior in Gherkin language, while step files map each step to Selenium automation code.

JSON test data keeps credentials, products, and checkout data outside the test scripts. This makes the framework easier to maintain and extend.

Explicit waits in `BasePage` reduce flaky failures by waiting for elements to become visible or clickable before actions happen.

Screenshots are captured automatically in `conftest.py` when a test fails. This helps debug automation failures.

HTML reports are generated by pytest-html and saved in the `reports/` folder.

GitHub Actions installs dependencies and runs the same tests in CI on Chrome and Firefox in headless mode.

## How to explain this project in an interview

You can say:

I built a Selenium Python automation framework for the SauceDemo ecommerce application. I used Page Object Model to separate page locators and actions from test cases, which makes the framework reusable and maintainable. PyTest is used as the test runner with markers for smoke, sanity, and regression suites. I added pytest-bdd feature files to demonstrate BDD-style testing using Given/When/Then scenarios. Test data such as users, products, and checkout information is stored in JSON, so tests are data-driven and easy to update. The framework supports Chrome and Firefox execution through command-line options, uses explicit waits to reduce flaky failures, captures screenshots on test failure, generates HTML reports, and includes a GitHub Actions workflow for CI execution.

## 60-second interview explanation

This is a Selenium Python automation framework for the SauceDemo ecommerce website. I automated important user journeys such as valid login, negative login, product validation, add to cart, and checkout. The framework follows Page Object Model, so every page has a separate class for locators and reusable actions, while test files only focus on validation. I used PyTest for test execution, markers for smoke, sanity, and regression suites, and JSON files for data-driven testing. I also added pytest-bdd feature files for login and checkout scenarios to show BDD understanding. The framework supports Chrome and Firefox through command-line options, uses explicit waits, captures screenshots on failure, creates HTML reports, and runs in GitHub Actions CI in headless mode.

## Common interview questions and answers

### 1. Why did you use Page Object Model?

Page Object Model keeps locators and page actions in separate page classes. This reduces duplicate code and makes maintenance easier when UI locators change.

### 2. What is the role of `conftest.py`?

`conftest.py` stores shared PyTest configuration. In this project it creates the WebDriver fixture, handles browser selection, supports headless mode, and captures screenshots when tests fail.

### 3. What is the difference between smoke, sanity, and regression testing?

Smoke testing checks the most critical flows after a build. Sanity testing quickly verifies that a focused area is stable. Regression testing checks broader functionality to make sure existing features still work after changes.

### 4. How is data-driven testing implemented?

Test data is stored in `test_data/users.json`. Tests read credentials, product names, and checkout information through utility functions instead of hardcoding data in every test.

### 5. Why are explicit waits used?

Explicit waits wait for specific conditions, such as an element being visible or clickable. This is more reliable than fixed sleeps and helps reduce flaky test failures.

### 6. How do you debug a failed automation test?

I check the PyTest error message, review the HTML report, inspect the screenshot captured on failure, reproduce the test locally, and verify whether the failure is caused by test data, locator changes, timing, or an actual application defect.

### 7. How does cross-browser testing work here?

The framework accepts a `--browser` command-line option. Based on the selected browser, the fixture creates either a Chrome or Firefox WebDriver session.

### 8. What is BDD and how is it used here?

BDD describes application behavior in business-readable language using Given/When/Then steps. In this project, pytest-bdd maps those feature steps to Python Selenium step definitions.

### 9. What is the purpose of GitHub Actions?

GitHub Actions runs the automation tests automatically whenever code is pushed or a pull request is created. It helps identify failures early in the development process.

### 10. How would you extend this framework?

I would add more test data combinations, more page objects, API setup support, Allure reports, parallel execution with pytest-xdist, environment-specific configuration, and integration with a test management tool.

## Resume bullet points

- Built a Selenium WebDriver automation framework in Python for an ecommerce demo application using Page Object Model and reusable page actions.
- Automated login, negative login, product listing, add to cart, and checkout flows using PyTest.
- Implemented smoke, sanity, and regression test suites with PyTest markers for flexible execution.
- Added data-driven testing using JSON test data for users, products, and checkout information.
- Integrated pytest-bdd feature files and step definitions for BDD-style test scenarios.
- Added explicit waits, screenshot capture on failure, and HTML report generation for better debugging and reporting.
- Implemented Chrome and Firefox cross-browser execution using WebDriver Manager.
- Created a GitHub Actions CI workflow to run automation tests automatically in headless mode.

## Suggested test case design

| Test case | Type | Expected result |
| --- | --- | --- |
| Valid user login | Smoke, regression | Products page is displayed |
| Locked out user login | Regression, negative | Login error message is displayed |
| Product listing | Sanity, regression | Products are visible after login |
| Add product to cart | Smoke, regression | Cart badge and cart item are updated |
| Complete checkout | Smoke, regression | Order confirmation message is displayed |

## Notes

The first test run may take longer because WebDriver Manager downloads the browser driver. In CI, tests run in headless mode because there is no visible browser window.
