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
## How to Install Packages
- pip install requests pytest pytest-html faker allure-pytest jsonschema

## How to run your Testcase Parallel
- pip install pytest-xdist

## How to add the .gitignore File?
- Copy the content from this to .gitignore file https://www.toptal.com/developers/gitignore/api/pycharm+all

## How to run the Basic Test with Allure report
1. pytest 'location of the file' --alluredir=allure_result -s
2. allure serve allure_resul
 