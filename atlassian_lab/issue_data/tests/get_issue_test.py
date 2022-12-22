import configparser
from atlassian_lab.issue_data.get_issue import connect_to_jira_api, get_pbi_data
import pytest

@pytest.mark.itest
def test_it_should_get_issue_info():
    config = configparser.ConfigParser()
    config.read('conf/atl.conf')
    user = config['atlassian_api_client']['user']
    api_token = config['atlassian_api_client']['api_token']
    server = config['atlassian_api_client']['server']
    jira = connect_to_jira_api(api_token, server, user)
    get_pbi_data(jira, config['atlassian_api_client']['issue'])
    assert 1 == 1