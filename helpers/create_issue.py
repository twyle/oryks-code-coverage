# -*- coding: utf-8 -*-
"""Module doctsring."""
import json
import os
from pprint import pprint

import requests

token = os.environ['INPUT_GITHUB_TOKEN']
repository = os.environ['GITHUB_REPOSITORY']
username = repository.split('/')[0]
repository_name = repository.split('/')[-1]


def create_markdown():
    """Create the markdown for the issue."""
    query_url = "https://api.github.com/markdown"
    data = {
        "text": "`code`, _italics_, **bold**",
        "mode": "markdown",
    }
    headers = {'Authorization': f'token {token}'}
    r = requests.post(query_url, headers=headers, data=json.dumps(data))
    pprint(r)
    pprint(r.text)


def create_issue(test_output):
    """
    Step 1.

    Create contents for the issue you want to post
    """
    headers = {"Authorization": f"token {token}"}
    data = {
        "title": "Found a bug",
        "body": test_output,
        "assignee": username,
        "labels": ['bug']
    }

    """
    Step 2:
    Generate your target repository's URL using Github API
    """  # pylint: disable=W0105
    url = f"https://api.github.com/repos/{username}/{repository_name}/issues"

    """
    Step 3:
    Post your issue message using requests and json
    """  # pylint: disable=W0105
    requests.post(url, data=json.dumps(data), headers=headers)

    create_markdown()
