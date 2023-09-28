import configparser
import csv
import requests


def get_sprint_data() -> None:
    config = configparser.ConfigParser()
    # config.read(sys.argv[1]) # import sys & set config file on the command line
    config.read('conf/atl.conf')
    user: str = config['atl_api']['user']
    api_token: str = config['atl_api']['api_token']
    server: str = config['atl_api']['server']

    # Set the board ID and sprint range
    board_id: str = config['atl_api']['board_id']

    # Set the authentication credentials
    auth: tuple = (user, api_token)

    # Set the headers
    headers: dict = {
        "Accept": "application/json"
    }

    # Send a GET request to the API endpoint
    response = requests.get(server + "/rest/greenhopper/1.0/rapid/charts/velocity?rapidViewId=" + board_id,
                            auth=auth,
                            headers=headers)
    response_dict: dict = response.json()

    sprint_data = []

    # print(response_dict['velocityStatEntries']['11570']['estimated']['text'])

    for sprint in response_dict['sprints']:
        sprint_id = '{}'.format(sprint['id'])

        sprint_info = {
            'id': sprint_id,
            'name': sprint['name'],
            'estimated': response_dict['velocityStatEntries'][sprint_id]['estimated']['text'],
            'completed': response_dict['velocityStatEntries'][sprint_id]['completed']['text']
        }
        sprint_data.append(sprint_info)

    # Print the response content
    print(sprint_data)

    # Export the data to a CSV file
    tmpdir = ''
    filename = tmpdir.join('sprint_data.csv')
    write_to_csv(sprint_data, filename)


def write_to_csv(data: list[dict[str, str]], filename: str):
    headers = ['id', 'name', 'estimated', 'completed']

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
