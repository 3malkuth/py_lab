# import sys
import configparser

import atlassian_lab.connect_atlassian
# The following will only work if you set the PYTHONPATH variable
# > export PYTHONPATH=~/path/to/py_lab
from atlassian_lab.issue_data import get_issue


def main() -> None:
    config = configparser.ConfigParser()
    # config.read(sys.argv[1]) # import sys & set config file on the command line
    config.read('conf/atl.conf')
    user = config['atl_api']['user']
    api_token = config['atl_api']['api_token']
    server = config['atl_api']['server']
    jira = atlassian_lab.connect_atlassian.connect_to_jira_api(api_token, server, user)
    jql_request = 'issuetype = epic'
    # TODO Refine the epic search
    issues = jira.jql(jql_request)
    print(issues)


if __name__ == '__main__':
    main()
