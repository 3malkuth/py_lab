# py_lab

## Run tests
* First enter the pip environment
```
# Run all tests
pytest -v

# run integration tests
pytest -v -m itest

# run tests excluding integration tests
pytest -v -m "not itest"

# run specific tests
pytest ./path/script.py::test_name -sv
```

## NB! You may need to set the Python Path
* Many of the modules here are dependent on other modules outside of their module hierarchy
    * Therefore, you will need to...
```
export PYTHONPATH=~/path/to/py_lab
```

## pip virtual environment
### Setup dev environment
* Setup Python dependencies
```
pipenv install
pipenv install --dev
```

### Enter the dev environment
* If you don't see: (py_lab) command prompt:$_____
* Then start this project's virtualenv with:
```
pipenv shell
```
* Or run a single command inside the virtualenv using:
```
pipenv run
```

## Add module to dev environment
* You don't need to have entered the dev environment
```
pipenv install name_of_module
pipenv install --dev name_of_module
```

## Managing Packages
* Add a new package to the environment
  * Edit Pipfile
```
[packages]
atlassian-python-api = "*"
```
* Update the current pipenv and lock
```
pipenv install # or update
pipenv lock
```
