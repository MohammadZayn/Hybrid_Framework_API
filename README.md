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
   
## Best Practices
- Follow the Page Object Model (POM) to separate test logic from UI logic.
- Use data-driven testing for better coverage.
- Implement cross-browser testing to ensure compatibility.

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
     python -m filename.py -s tests
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
For any inquiries or opportunities, feel free to reach out via MohammadShaik or email at mohammadshaik776@gmail.com.
