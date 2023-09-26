import csv
from datetime import date, timedelta
from unittest.mock import MagicMock

import pytest
from jira import JIRA

from atlassian_lab.team_velocity.team_velocity_calc import write_to_csv, get_sprint_data

DELIVERED_VELOCITY = 'Delivered Velocity'
SPRINT_2 = 'Sprint 2'
COMMITTED_VELOCITY = 'Committed Velocity'
SPRINT_1 = 'Sprint 1'
TEAM_A = 'Team A'
TEAM_B = 'Team B'
TEAM_C = 'Team C'
@pytest.fixture
def mock_jira():
    jira = MagicMock(spec=JIRA)
    jira.sprints.return_value = [
        create_mock_sprint(TEAM_A, 10, 8, date.today()),
        create_mock_sprint(TEAM_B, 15, 12, date.today() - timedelta(days=3)),
        create_mock_sprint(TEAM_C, 20, 18, date.today() - timedelta(days=5))
    ]
    return jira


def create_mock_sprint(board_name, committed_points, completed_points, end_date):
    sprint = MagicMock()
    sprint.raw = {
        'originBoardName': board_name,
        'committedPoints': {'value': committed_points},
        'completedPoints': {'value': completed_points}
    }
    sprint.endDate.date.return_value = end_date
    return sprint


# @pytest.mark.utest
# def test_get_sprint_data(mock_jira):
def get_sprint_data(mock_jira):
    # Call the function with mock Jira server
    # sprint_data = get_sprint_data('http://mock-jira-server', 'username', 'password')
    sprint_data = get_sprint_data(mock_jira)

    # Verify the output
    assert len(sprint_data) == 2
    assert sprint_data[0]['Team'] == TEAM_A
    assert sprint_data[0]['Sprint'] == SPRINT_1
    assert sprint_data[0][COMMITTED_VELOCITY] == '10'
    assert sprint_data[0][DELIVERED_VELOCITY] == '8'
    assert sprint_data[1]['Team'] == TEAM_B
    assert sprint_data[1]['Sprint'] == 'Sprint 2'
    assert sprint_data[1][COMMITTED_VELOCITY] == '15'
    assert sprint_data[1][DELIVERED_VELOCITY] == '12'


# @pytest.mark.utest
def test_write_to_csv(tmpdir):
    # Test data
    data = [
        {'Team': 'Team A', 'Sprint': SPRINT_1, COMMITTED_VELOCITY: '10', DELIVERED_VELOCITY: '8'},
        {'Team': 'Team B', 'Sprint': SPRINT_2, COMMITTED_VELOCITY: '15', DELIVERED_VELOCITY: '12'}
    ]

    # Call the function
    filename = tmpdir.join('sprint_data.csv')
    write_to_csv(data, str(filename))

    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    # Verify the output
    assert len(rows) == 2
    assert rows[0]['Team'] == TEAM_A
    assert rows[0]['Sprint'] == SPRINT_1
    assert rows[0][COMMITTED_VELOCITY] == '10'
    assert rows[0][DELIVERED_VELOCITY] == '8'
    assert rows[1]['Team'] == TEAM_B
    assert rows[1]['Sprint'] == SPRINT_2
    assert rows[1][COMMITTED_VELOCITY] == '15'
    assert rows[1][DELIVERED_VELOCITY] == '12'
