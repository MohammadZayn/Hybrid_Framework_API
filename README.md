# Hybrid Framework API

## Overview

This repository contains a hybrid testing framework for API testing, designed to streamline and enhance the process of verifying API endpoints. The framework leverages various Python modules and tools to provide a robust and flexible testing environment.

## Features

- **Latest Python Version Compatibility**: Ensure compatibility with the latest Python versions.
- **HTTP Requests Handling**: Utilize the `requests` module to handle HTTP requests seamlessly.
- **Testing Framework**: Built on `pytest` to provide a simple and scalable test suite.
- **Comprehensive Reporting**: Integrated with Allure for detailed reports, PyTest HTML for HTML-based reports, and Faker for generating fake data.
- **Test Data Management**: Manage test data with CSV, Excel (using Openpyxl), and JSON files.
- **Parallel Test Execution**: Run tests in parallel using `pytest-xdist`.
- **Advanced API Testing**: Validate JSON schemas to ensure API responses conform to expected structures.

## Project Structure

```plaintext
Hybrid_Framework_API/
├── test_cases/
│   ├── crud_actions/
│   │   ├── test_create.py
│   │   ├── test_read.py
│   │   ├── test_update.py
│   │   ├── test_delete.py
├── utils/
│   ├── request_util.py
│   ├── data_util.py
│   ├── data1_util.py
├── conftest.py
├── requirements.txt
└── README.md
```
## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/Hybrid_Framework.git
2. Navigate to the project directory:
   ```bash
   cd Heruko_Tc
3. How to Install Packages
   ```bash
   pip install requests pytest pytest-html faker allure-pytest jsonschema
4. How to run your Testcase Parallel
   ```bash
   pip install pytest-xdist

5. How to add the .gitignore File?
   ```bash
   Copy the content from this to .gitignore file https://www.toptal.com/developers/gitignore/api/pycharm+all

6. How to run the Basic Test with Allure report
   ```bash
   1. pytest 'location of the file' --alluredir=allure_result -s
   2. allure serve allure_result

## Best Practices for Automated Testing

### 1. Follow the Page Object Model (POM)

The Page Object Model (POM) is a design pattern that helps in creating an object repository for web UI elements. It separates the test logic from the UI logic, making the code more maintainable and reusable.

#### Benefits:
- **Separation of Concerns:** Keeps test code clean and easy to understand by separating UI interactions from the test logic.
- **Reusability:** Common operations on UI elements are encapsulated in methods within the page objects, allowing you to reuse them across different tests.
- **Maintainability:** Changes to UI elements need only be updated in one place, the page object, which simplifies maintenance when the UI changes.

#### Implementation Tips:
- Create a separate class for each page of the application.
- Define locators for UI elements and wrap them in methods that perform actions on those elements.
- Avoid putting test assertions within the page objects; these should remain in the test scripts.

```python
# Example of a Page Object in Python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element_by_id('username')
        self.password_input = driver.find_element_by_id('password')
        self.login_button = driver.find_element_by_id('login')

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()
```
### 2. Use Data-Driven Testing
Data-driven testing involves running a test script with multiple sets of data inputs to ensure comprehensive test coverage. This approach allows you to validate how the application behaves with different inputs, edge cases, and data scenarios.

#### Benefits:
- **Increased Test Coverage:** Allows testing of multiple scenarios and edge cases without duplicating test code.
- **Efficiency:** Reduces the number of test scripts needed, as the same script can run with different data sets.
- **Ease of Maintenance:** Test data can be managed separately from test scripts, making it easier to update or expand test scenarios.

#### Implementation Tips:
- Store test data in external files such as CSV, JSON, or Excel.
- Use a framework that supports parameterized testing to feed the test data into your scripts.
- Ensure that your tests validate expected results for each data set.
```python
Copy code
# Example of Data-Driven Test in Python using pytest
import pytest

@pytest.mark.parametrize("username, password", [
    ("user1", "password1"),
    ("user2", "password2"),
    ("user3", "password3"),
])
def test_login(username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert "Welcome" in driver.page_source
```

### 3. Implement Cross-Browser Testing
Cross-browser testing ensures that your application works correctly across different web browsers and versions. It's crucial for providing a consistent user experience and catching browser-specific issues.

#### Benefits:
**Compatibility:** Ensures that your application is functional across multiple browsers, reducing the risk of browser-specific bugs.
**User Experience:** Helps maintain a consistent experience for users, regardless of their preferred browser.
**Quality Assurance:** Early detection of browser-specific issues helps in delivering a more robust application.

#### Implementation Tips:
- Use cloud-based testing platforms like Selenium Grid, BrowserStack, or Sauce Labs to run tests across multiple browsers.
- Automate tests for popular browsers like Chrome, Firefox, Safari, and Edge.
- Prioritize testing on browsers and versions most commonly used by your audience.
```python
Copy code
# Example of Cross-Browser Testing in Python with Selenium
from selenium import webdriver

browsers = ['chrome', 'firefox', 'safari']

for browser in browsers:
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()

    driver.get("http://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
```
## Future Enhancements

### Integrate with CI/CD Tools like Jenkins

**Installation in Jenkins:**
1. Install Jenkins: Follow the [official guide](https://www.jenkins.io/doc/book/installing/) to set up Jenkins.
2. Install Python: Ensure that Python and required dependencies (e.g., Selenium) are installed on the Jenkins server.
3. Create a new Jenkins job: 
   - Choose "Freestyle project" or "Pipeline."
   - Configure the job to pull the code from the repository.
   - Add a build step to execute the test script using the command:
     ```bash
     python -m pip install -r requirements.txt
     python -m pytest
     ```
   - Configure email notifications for test results.
4. Set up triggers: Schedule jobs or trigger them via webhooks on code commits.

**Benefits:**
- Automates test execution on every code change.
- Generates detailed reports that can be viewed directly within Jenkins.
- Supports continuous integration for a smooth development workflow.

### Add Mobile Testing Support Using Appium

**Installation and Setup:**
1. Install Appium: Follow the [Appium documentation](http://appium.io/docs/en/about-appium/intro/) to set up Appium.
2. Configure Python with Appium: 
   - Install Appium-Python-Client:
     ```bash
     pip install Appium-Python-Client
     ```
   - Set up desired capabilities for Android/iOS in your test script:
     ```python
     desired_caps = {
         'platformName': 'Android',
         'deviceName': 'emulator-5554',
         'app': '/path/to/app.apk'
     }
     ```
3. Write and run test cases for mobile applications.

**Benefits:**
- Ensures cross-platform compatibility for the Heruko Healthcare application.
- Provides end-to-end testing on real devices and emulators.

### Implement Visual Regression Testing

**Installation and Setup:**
1. Choose a tool: For Python, consider tools like `SeleniumBase` or `Pikachu`.
2. Install the required package:
   ```bash
   pip install seleniumbase

## Contributing
Contributions are welcome! Please create a pull request with a detailed description of the changes.

### Contact
For any inquiries or opportunities, feel free to reach out via www.linkedin.com/in/mohammadzayn or email at mohammadshaik776@gmail.com.
