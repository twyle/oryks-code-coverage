# -*- coding: utf-8 -*-
"""Module doctsring."""
import json
import os

import requests

token = os.environ['INPUT_GITHUB_TOKEN']


def create_issue():
    """
    Step 1.

    Create contents for the issue you want to post
    """
    headers = {"Authorization": f"token {token}"}
    data = {"title": "Found a bug"}

    """
    Step 2:
    Generate your target repository's URL using Github API
    """  # pylint: disable=W0105
    username = 'twyle'
    Repositoryname = 'flask-social-auth'
    url = f"https://api.github.com/repos/{username}/{Repositoryname}/issues"

    """
    Step 3:
    Post your issue message using requests and json
    """  # pylint: disable=W0105
    requests.post(url, data=json.dumps(data), headers=headers)
