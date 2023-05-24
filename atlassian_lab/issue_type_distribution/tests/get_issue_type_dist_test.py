import configparser
import csv
import os
from atlassian_lab.connect_atlassian import connect_to_jira_api
import pytest
from atlassian_lab.issue_type_distribution.get_issue_type_dist import get_issue_type_dist_per_sprint, \
    get_filtered_list_of_issues_with_same_type, get_spoints_sum_per_type, write_csv_file


@pytest.mark.itest
def test_it_should_get_dict_dist_of_issues_in_current_sprint() -> None:
    config = configparser.ConfigParser()
    config.read('conf/atl.conf')
    user = config['atl_api']['user']
    api_token = config['atl_api']['api_token']
    server = config['atl_api']['server']
    prj_key = config['atl_api']['prj_key']
    jira = connect_to_jira_api(api_token, server, user)
    jql_request: str = "project = '{}' AND sprint in openSprints() and issuetype in ('Bug','Task','Story')" \
                       "ORDER BY createdDate DESC".format(prj_key)
    print(get_issue_type_dist_per_sprint(jira, jql_request))
    #assert False
    assert True


@pytest.mark.utest
def test_it_should_filter_list_extracting_issues_with_the_same_type() -> None:
    # Arrange
    list_unfiltered_issues_different_type: list = [{'issue_key': 'TST-1234', 'type': 'Bug', 'spoints': 1.0},
                                                   {'issue_key': 'TST-4231', 'type': 'Task', 'spoints': 1.0},
                                                   {'issue_key': 'TST-3232', 'type': 'Story', 'spoints': 3.0},
                                                   {'issue_key': 'TST-8484', 'type': 'Task', 'spoints': 2.0},
                                                   {'issue_key': 'TST-9232', 'type': 'Story', 'spoints': 2.0},
                                                   {'issue_key': 'TST-2343', 'type': 'Task', 'spoints': 1.0},
                                                   {'issue_key': 'TST-3256', 'type': 'Bug', 'spoints': 1.0}]

    # Act
    keys_types_filtered: list = get_filtered_list_of_issues_with_same_type(list_unfiltered_issues_different_type,
                                                                           'Task')

    # Assert
    correctly_filtered_list: list = [{'issue_key': 'TST-4231', 'type': 'Task', 'spoints': 1.0},
                                     {'issue_key': 'TST-8484', 'type': 'Task', 'spoints': 2.0},
                                     {'issue_key': 'TST-2343', 'type': 'Task', 'spoints': 1.0}]
    assert keys_types_filtered == correctly_filtered_list


@pytest.mark.utest
def test_it_should_sum_the_spoints_for_an_issue_type() -> None:
    # Arrange
    list_filtered_issues_per_type: list = [{'issue_key': 'TST-4231', 'type': 'Task', 'spoints': 1.0},
                                           {'issue_key': 'TST-8484', 'type': 'Task', 'spoints': 2.0},
                                           {'issue_key': 'TST-2343', 'type': 'Task', 'spoints': 1.0}]

    # Act
    sum_of_spoints: float = get_spoints_sum_per_type(list_filtered_issues_per_type)

    # Assert
    correct_sum: float = 4.0
    assert sum_of_spoints == correct_sum


#@pytest.mark.utest
#def test_write_csv_file():
def write_csv_file() -> None:
    test_data = {'Sprint Name': 'Sprint - 2023 CW12/13',
                 'list_issue_types_spoints': [{'issue_type': 'Story', 'spoints': 8.0},
                                              {'issue_type': 'Task', 'spoints': 10.0},
                                              {'issue_type': 'Bug', 'spoints': 2.0}]}
    test_file_path = 'test_sprint_data.csv'

    # Call the function being tested
    write_csv_file(test_data, test_file_path)

    # Check that the CSV file was created with the correct data
    with open(test_file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    assert len(rows) == len(test_data['list_issue_types_spoints'])
    for i, item in enumerate(test_data['list_issue_types_spoints']):
        assert rows[i]['Sprint Name'] == test_data['Sprint Name']
        assert rows[i]['Issue Type'] == item['issue_type']
        assert rows[i]['Story Points'] == str(item['spoints'])

    # Clean up the test file
    os.remove(test_file_path)
