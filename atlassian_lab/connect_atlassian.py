from atlassian import Jira


def connect_to_jira_api(api_token, server, user):
    jira = Jira(
        url=server,
        username=user,
        password=api_token,
        cloud=True)
    return jira
