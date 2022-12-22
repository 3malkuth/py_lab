import sys

import configparser
import get_issue

# Config file format is like an .ini file
# [atlassian_api_client]
# user=name@example.com
# ...
def main():
    config = configparser.ConfigParser()
    config.read('conf/atl.conf')
    user = config['atlassian_api_client']['user']
    api_token = config['atlassian_api_client']['api_token']
    server = config['atlassian_api_client']['server']
    jira = get_issue.connect_to_jira_api(api_token, server, user)
    get_issue.get_pbi_data(jira, config['atlassian_api_client']['issue'])


if __name__ == '__main__':
    main()
