import pytest
from unittest.mock import MagicMock
from atlassian_lab.team_velocity.team_velocity_calc import get_velocity_data


@pytest.fixture
def mock_requests_get(mocker):  # 'mocker' is injected by pytest-mock
    # Mock requests.get
    mock_response = MagicMock()
    mock_response.json.return_value = {"velocity": 42}  # Replace with expected JSON response
    mocker.patch('requests.get', return_value=mock_response)


def test_it_should_get_velocity_data(mock_requests_get):
    # Define test parameters
    server = 'https://example.com'
    board_id = '123'
    api_token: str = '2893rz423ngb34bbc4thn834'
    user = 'user@example.com'

    # Call the function to be tested
    result = get_velocity_data(api_token, board_id, server, user)

    # Assertions
    assert result == {"velocity": 42}  # Replace with your expected result
