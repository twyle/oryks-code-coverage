# -*- coding: utf-8 -*-
"""This module contains functions that upload test data to our servers.."""
import json
import os

import requests

from .create_issue import create_df

# HOST_IP = '194.233.169.9'
# HOST_IP = '192.168.100.4'
run_number = os.environ['GITHUB_RUN_NUMBER']
HOST_IP = 'https://oryks-code-coverage-dev.herokuapp.com'
token = os.environ['INPUT_ORYKS_TOKEN']


def upload_data(test_output, project='lyleokoth/flask-social-auth', username='lyleokoth'):
    """Upload the test data to our servers."""
    test_df = create_df(test_output)
    # print(test_df)

    url = f'{HOST_IP}/api/data'
    # url = f'http://{HOST_IP}:5000/api/data'
    headers = {"Authorization": f"Bearer {token}"}

    data = {
        'user': {
            'project': project,
            'username': username,
            'run_number': run_number
        },
        'data': test_df.to_json()
    }

    res = requests.post(url=url, json=json.dumps(data), headers=headers)

    if res.status_code in [201, 200]:
        # print(res.json())
        return True

    # print(res.status_code)
    # print(res.json())
    return False
