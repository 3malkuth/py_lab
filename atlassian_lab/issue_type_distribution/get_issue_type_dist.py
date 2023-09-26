import csv

from atlassian_lab.constants import ISSUE_TYPES_LIST


def get_issue_type_dist_per_sprint(jira, jql_request: str) -> dict:
    jql_response: dict = jira.jql(jql_request)
    issues_list: list = jql_response.get('issues')
    sprint_name: str = get_sprint_name(issues_list)
    print("Current Sprint Name: " + str(sprint_name))
    issue_keys_types_spoints_list: list = list(map(get_key_type_spoints_dict, issues_list))
    issue_type_dist_per_sprint: list = list(map(lambda x: get_dict_type_spoints(issue_keys_types_spoints_list, x),
                                                ISSUE_TYPES_LIST))
    issue_type_dist_per_sprint_name: dict = {'Sprint Name': sprint_name,
                                             'list_issue_types_spoints': issue_type_dist_per_sprint}
    write_csv_file(issue_type_dist_per_sprint_name, 'test_sprint_data.csv')
    return issue_type_dist_per_sprint_name


def write_csv_file(data: dict[str, any], file_path: str) -> None:
    with open(file_path, mode='w', newline='') as csv_file:
        fieldnames: list = ['Sprint Name', 'Issue Type', 'Story Points']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for item in data['list_issue_types_spoints']:
            writer.writerow({
                'Sprint Name': data['Sprint Name'],
                'Issue Type': item['issue_type'],
                'Story Points': item['spoints']
            })


def get_sprint_name(issues_list: list) -> str:
    sprint: str = issues_list[0].get('fields').get('customfield_10007')[0].get('name')
    return sprint


def get_dict_type_spoints(issue_keys_types_spoints_list, type: str) -> dict:
    issue_keys_types_spoints_filtered: list = get_filtered_list_of_issues_with_same_type(issue_keys_types_spoints_list,
                                                                                         type)
    return {'issue_type': type,
            'spoints': get_spoints_sum_per_type(issue_keys_types_spoints_filtered)}


def get_spoints_sum_per_type(issue_keys_types_spoints_filtered: list) -> float:
    return sum(issue['spoints'] for issue in issue_keys_types_spoints_filtered)


def get_key_type_spoints_dict(issue: dict) -> dict:
    spoints_unfiltered = issue.get('fields').get('customfield_10005')

    spoints_updated: float = float(0.0) if spoints_unfiltered is None else spoints_unfiltered
    # print (spoints_updated)

    type_unfiltered: str = issue.get('fields').get('issuetype').get('name')
    print(type_unfiltered)
    # type_updated: str = 'Other' if type_unfiltered != 'Story' or type_unfiltered != 'Task' or type_unfiltered != 'Bug'\
    #    else type_unfiltered
    type_updated: str = type_unfiltered if type_unfiltered == 'Story' or type_unfiltered == 'Task' or type_unfiltered == 'Bug' \
        else 'Other'
    print(type_updated)

    return {'issue_key': issue.get('key'),
            'type': type_updated,
            'spoints': spoints_updated,
            }


def get_filtered_list_of_issues_with_same_type(keys_types_spoints: list, type: str) -> list:
    keys_types_spoints_filtered: list = list(filter(lambda x: (x.get('type') == type), keys_types_spoints))
    print(keys_types_spoints_filtered)
    return keys_types_spoints_filtered
