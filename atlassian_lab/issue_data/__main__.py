import configparser

import atlassian_lab.connect_atlassian
from atlassian_lab.issue_data import get_issue

# Config file format is like an .ini file
# [atlassian_api_client]
# user=name@example.com
# ...
def main() -> None:
    config = configparser.ConfigParser()
    config.read('conf/atl.conf')
    user = config['atl_api']['user']
    api_token = config['atl_api']['api_token']
    server = config['atl_api']['server']
    jira = atlassian_lab.connect_atlassian.connect_to_jira_api(api_token, server, user)
    get_issue.get_pbi_basic_data(jira, config['atl_api']['issue_key'])


if __name__ == '__main__':
    main()
