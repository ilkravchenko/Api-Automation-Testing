
# Api Automation Testing


## Run Locally

Clone the project

```bash
  git clone https://github.com/ilkravchenko/Api-Automation-Testing.git
```

Go to the project directory

```bash
  cd Api-Automation-Testing
```

Install dependencies

```bash
  pip install -r requirements.txt
```


## Running Tests

**Before you will run the tests, you need to change input test data:**
```bash
  test_registration_data - 'YOUR_TOKEN', 'YOUR_LOGIN', 'YOUR_EMAIL', 'YOUR_PASSWORD'
  test_update_data - 'YOUR_TOKEN', 'YOUR_USER_TOKEN', 'YOUR_LOGIN', 'YOUR_NEW_EMAIL', 'YOUR_NEW_LOGIN'
```

After that manipulation you can run the tests

To run tests, run the following command

```bash
  pytest
```
or

```bash
  pytest .\tests\test_update_user.py
  pytest .\tests\test_registration.py
```
or

```bash
  pytest.\tests\test_update_user.py::test_update_user
  pytest .\tests\test_registration.py::test_registration
```


