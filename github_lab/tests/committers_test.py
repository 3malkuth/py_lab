import configparser
import pytest
import requests
import json

# @pytest.mark.skip
@pytest.mark.itest
def test_it_should_get_committers():
    config: configparser = configparser.ConfigParser()
    config.read('./conf/gh.conf')
    str_user: str = config['gh_tri_api']['user']
    str_repo: str = 'py_lab'
    str_api_token: str = config['gh_tri_api']['api_token']
    str_url_api_commits: str = "https://api.github.com/repos/{}/{}/commits?branch=master&since=2021-12-01&until=2021-12-31".format(str_user, str_repo)
    print(str_url_api_commits)
    req_gh_session: requests = requests.Session()
    req_gh_session.auth = (str_user, str_api_token)
    response: list = json.loads(req_gh_session.get(str_url_api_commits).text)
    print(response[0])
    assert 1 == 1

# pytest ./github_lab/tests/committers_test.py::test_it_should_get_committers -rA