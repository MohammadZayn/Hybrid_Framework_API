# Python Automation Framework (API)

### Required Things
- Python Latest Version
- Requests Module - HTTPS request
- PyTest Module - Testing Framework
- Report Modules - Allure , PyTest, HTML ,Faker
- Test Data Modules - CSV, Excel(Openpyxl), JSON
- Parallel Execution - Xdist Module
- Advance API Testing - Jsonschema 

### Install the required libraries
- pip install requests pytest pytest-html faker allure-pytest jsonschema pytest-xdist

### To run the parallel testcases in a single click
- pip install pytest-xdist

### Add the git ignore file
- Copy the content from the below link and paste it to the .gitignore file
- https://www.toptal.com/developers/gitignore/api/pycharm+all

### To create an allure test report command
- pytest "location_of_the_file" --alluredir=allure_result
- allure serve allure_result

