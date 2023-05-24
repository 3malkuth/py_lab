import csv
from typing import List, Dict
from jira import JIRA


#def get_sprint_data(jira_url: str, username: str, password: str, jira: any) -> List[Dict[str, str]]:
def get_sprint_data(jira: any) -> List[Dict[str, str]]:
    # Connect to Jira
    # jira = JIRA(server=jira_url, basic_auth=(username, password))

    # Get the last 7 completed sprints
    completed_sprints = jira.search_issues(
        f"project = YOUR_PROJECT AND type = Sprint AND sprint in closedSprints() ORDER BY Sprint DESC",
        maxResults=7)

    sprint_data = []

    for sprint in completed_sprints:
        sprint_info = {
            'Team': sprint.fields.customfield_10008,  # Replace customfield_10008 with your team custom field ID
            'Sprint': sprint.fields.customfield_10007,  # Replace customfield_10007 with your sprint custom field ID
            'Committed Velocity': str(sprint.fields.customfield_10010),
            # Replace customfield_10010 with your committed velocity custom field ID
            'Delivered Velocity': str(sprint.fields.customfield_10011)
            # Replace customfield_10011 with your delivered velocity custom field ID
        }

        sprint_data.append(sprint_info)

    return sprint_data


def write_to_csv(data: List[Dict[str, str]], filename: str):
    headers = ['Team', 'Sprint', 'Committed Velocity', 'Delivered Velocity']

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
