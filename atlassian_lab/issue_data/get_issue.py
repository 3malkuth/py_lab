from atlassian import Jira


def connect_to_jira_api(api_token, server, user):
    jira = Jira(
        url=server,
        username=user,
        password=api_token,
        cloud=True)
    return jira


def get_pbi_data(jira, issue_key):
    issue = jira.issue(issue_key)  # full description
    field = 'issuetype'
    summary = jira.issue_field_value(issue_key, field)
    print('ticket: ', issue_key, summary)
