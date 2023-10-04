import pytest
from unittest.mock import MagicMock, Mock
from atlassian_lab.team_velocity.team_velocity_calc import get_velocity_data
import requests

# Define test parameters
SERVER: str = 'https://example.com/'
BOARD_ID: str = '123'
API_TOKEN: str = '2893rz423ngb34bbc4thn834'
USER: str = 'user@example.com'


# Define a mock function to replace requests.get
def mock_requests_get(url, auth, headers):
    mock_response = MagicMock()
    print(url)
    if url.endswith('/notfound'):
        print('hello')
        mock_response.json.return_value = None
        mock_response.status_code = 404
    elif url.endswith('/servererror'):
        mock_response.json.return_value = None
        mock_response.status_code = 500
    else:
        mock_response.json.return_value = {'velocity': 42}
        mock_response.status_code = 200  # Replace with expected JSON response
    return mock_response


# Test case 1: Simulate a successful request
@pytest.mark.utest
def test_it_should_get_velocity_data_and_status_200_OK(mocker):
    # ARRANGE
    # Mock requests.get to return a successful response
    mocker.patch('requests.get', side_effect=mock_requests_get)

    # ACT
    # Call the function that handles HTTP errors
    result = get_velocity_data(SERVER + '/success', API_TOKEN, USER)

    # ASSERT
    assert result['resp_json'] == {"velocity": 42}
    assert result['status_code'] == 200


# Test case 2: Simulate a 404 Not Found error
@pytest.mark.utest
def test_handle_http_errors_404_error(mocker):
    # Mock requests.get to return a 404 error response
    # mocker.patch('requests.get',
    #             side_effect=Mock(side_effect=requests.exceptions.HTTPError(response=Mock(status_code=404))))
    mocker.patch('requests.get', side_effect=mock_requests_get)

    # Call the function that handles HTTP errors
    result = get_velocity_data(SERVER + '/notfound', API_TOKEN, USER)

    # ASSERT
    assert result['resp_json'] is None
    assert result['status_code'] == 404


# Test case 3: Simulate a 500 Internal Server Error
@pytest.mark.utest
def test_handle_http_errors_500_error(mocker):
    # Mock requests.get to return a 500 error response
    # mocker.patch('requests.get',
    #             side_effect=Mock(side_effect=requests.exceptions.HTTPError(response=Mock(status_code=500))))
    mocker.patch('requests.get', side_effect=mock_requests_get)

    # Call the function that handles HTTP errors
    result = get_velocity_data(SERVER + '/servererror', API_TOKEN, USER)

    # ASSERT
    assert result['resp_json'] is None
    assert result['status_code'] == 500
