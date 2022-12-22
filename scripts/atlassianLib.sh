#!/bin/bash
# $1 path to py_lab code repo e.g. ~/path/py_lab
# $2 path to file with access info e.g. ~/path/filename.conf
export PYTHONPATH=$1
cd ..
echo "CHECK! Are you in the pipenv shell?"
# pipenv shell

# MODULES
#python atlassian_lab/atlassian_api_client $1
python atlassian_lab/epic_duration $2
