# -*- coding: utf-8 -*-
"""Module doctsring."""
import json
import os
from pprint import pprint

import requests

token = os.environ['INPUT_GITHUB_TOKEN']

x = """
   | Route       | Method      | Description      |
   | ----------- | ----------- |----------------- |
   | '/'         | GET         | Get the home page |
"""


def create_markdown():
    """Create the markdown for the issue."""
    query_url = "https://api.github.com/markdown"
    data = {
        "text": x,
        "mode": "markdown",
    }
    headers = {'Authorization': f'token {token}'}
    r = requests.post(query_url, headers=headers, data=json.dumps(data))
    pprint(r)
    pprint(r.text)


if __name__ == '__main__':
    create_markdown()
