import configparser
from atlassian_lab.issue_data.get_issue import get_pbi_basic_data
from atlassian_lab.connect_atlassian import connect_to_jira_api
import pytest

@pytest.mark.itest
def test_it_should_get_issue_info() -> None:
    config = configparser.ConfigParser()
    config.read('conf/atl.conf')
    user = config['atl_api']['user']
    api_token = config['atl_api']['api_token']
    server = config['atl_api']['server']
    issue_key = config['atl_api']['issue_key']
    jira = connect_to_jira_api(api_token, server, user)
    pbi: dict = get_pbi_basic_data(jira, issue_key)
    assert True
    #assert False
