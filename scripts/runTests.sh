#!/bin/bash

echo "Ensure you are in a pipenv shell!"
# pipenv shell
echo "Running pytest..."
pytest

# run unit tests
# pytest -v -m utest

# run tests that use integrations
# pytest -v -m itest