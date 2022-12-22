import sys
import configparser
# The following will only work if you set the PYTHONPATH variable
# > export PYTHONPATH=~/path/to/py_lab
from atlassian_lab.issue_data import get_issue


def main():
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    user = config['atlassian_api_client']['user']
    api_token = config['atlassian_api_client']['api_token']
    server = config['atlassian_api_client']['server']
    jira = atlassian_api_client.connect_to_jira_api(api_token, server, user)
    jql_request = 'issuetype = epic'
    issues = jira.jql(jql_request)
    print(issues)


if __name__ == '__main__':
    main()
