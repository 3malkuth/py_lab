import configparser
import pytest
import requests
import json


# @pytest.mark.skip
# @pytest.mark.itest
@pytest.mark.skip("Integration Test")
def test_it_should_get_committers() -> None:
    config = configparser.ConfigParser()
    config.read('./conf/gh.conf')
    str_user: str = config['gh_api']['user']
    str_repo: str = 'py_lab'
    str_api_token: str = config['gh_api']['api_token']
    str_url_api_commits: str = \
        "https://api.github.com/repos/{}/{}/commits?branch=master&since=2023-01-01&until=2023-05-03"\
            .format(str_user, str_repo)
    print(str_url_api_commits)
    req_gh_session = requests.Session()
    req_gh_session.auth = (str_user, str_api_token)
    response: list = json.loads(req_gh_session.get(str_url_api_commits).text)  # A list where each item is a dictionary
    print("__________________________")
    resp_dict: dict = response[0]
    print(resp_dict.keys())  # prints keys in dictionary
    print(resp_dict.get('sha'))
    print("__________________________")
    assert str_repo == 'py_lab'

# pytest ./github_lab/tests/committers_test.py::test_it_should_get_committers -rA
# assert True