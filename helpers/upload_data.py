# -*- coding: utf-8 -*-
"""This module contains functions that upload test data to our servers.."""
import json
import os

import requests

from .create_issue import create_df

# HOST_IP = '194.233.169.9'
# HOST_IP = '192.168.100.4'
HOST_IP = 'https://oryks-code-coverage-dev.herokuapp.com'
token = os.environ['INPUT_ORYKS_TOKEN']


def upload_data(test_output, project='lyle/flask-social-auth', username='lyle'):
    """Upload the test data to our servers."""
    test_df = create_df(test_output)
    # print(test_df)

    url = f'{HOST_IP}/api/data'
    # url = f'http://{HOST_IP}:5000/api/data'
    headers = {"Authorization": f"Bearer {token}"}

    data = {
        'user': {
            'project': project,
            'username': username
        },
        'data': test_df.to_json()
    }

    res = requests.post(url=url, json=json.dumps(data), headers=headers)

    if res.status_code == 201:
        # print(res.json())
        return True

    return False
