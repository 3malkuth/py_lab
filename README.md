# py_lab
## NB!!!
* Please note that module specific documentation have their own readme files!!!

## Cloud Environments
* TODO: Move to aws

## Check Type Safety
* By default type safety is now setup in python 3.6+
  * However at some stage they may change this or switch it off...
  * So you don't have to explicitly import typing
* In the main py_lab folder run
```
mypy . # this will use the ignores etc. from mypy.ini
```
* OR if you cd into a module / package and run the following
  * You will also get more error signals as no use of mypy.ini
```
mypy .

```
* OR if you want to manually check a module / package
  * NB! The following will use the ignores in mypy.ini
  * Assuming you run it from the main py_lab folder
```
mypy FOLDER_NAME # folder name e.g. atlassian_lab
mypy -p PACKAGE_NAME # usually a collection of modules
mypy -m MODULE_NAME # usually a single file
```

## Run tests
* First enter the pip environment
```
# Run all tests
pytest -v

# run unit tests
pytest -v -m utest

# run integration tests
pytest -v -m itest

# run tests excluding integration tests
pytest -v -m "not itest"

# run specific tests
pytest ./path/script.py::test_name -sv
```

## Setup Dev Environment
### Notes
* This is only for ubuntu linux
* Make sure python3 is installed

### Setup config files
* Please note the conf folder is excluded from git for obvious reasons
* Copy the "conf_template" folder in "docs" to...
  * "conf" in py_lab folder
* Fill in the details for the config files

### Install pip3 & pipenv
```
sudo apt update
sudo apt install python3-pip
pip3 install --upgrade pip
pip3 install pipenv
```

### Path
* Path
  * You may need to add pip3 etc to the PATH
  * May be found in ~/.local/bin
  * Add the following to .bashrc
```
export PATH="~/.local/bin:$PATH"
export PYTHONPATH="/path/to/py_lab" # epic_duration won't work without it
# check...
echo $PATH
echo $PYTHONPATH
```
* Python Path
  * NB! You may need to set the python path...
  * Many of the modules here are dependent on other modules outside of their module hierarchy
    * Therefore, you will need to...
```
export PYTHONPATH=~/path/to/py_lab
```

### Setup the pip virtual environment
* **Go to the pylab folder**
  * cd...
* Open Pipfile and check if the python version is correct
  * You may want to check and upgrade if necessary other libraries etc.
* Setup Python dependencies
```
pipenv install
pipenv install --dev
```
## Use the Dev Environment
### Access the virtual dev environment
* If you don't see: (py_lab) command prompt:$_____
* Then start this project's virtualenv with:
```
pipenv shell
```
* Or run a single command inside the virtualenv using:
```
pipenv run
```

### Add module to dev environment
* You don't need to have entered the dev environment
```
pipenv install name_of_module
pipenv install --dev name_of_module
```

### Managing Packages
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
