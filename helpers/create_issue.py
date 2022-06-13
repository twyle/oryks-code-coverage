# -*- coding: utf-8 -*-
"""Module doctsring."""
import json
import os

import pandas as pd
import requests

token = os.environ['INPUT_GITHUB_TOKEN']
repository = os.environ['GITHUB_REPOSITORY']
username = repository.split('/')[0]
repository_name = repository.split('/')[-1]


def create_df(test_output):
    """Create df from test output."""
    all_lines = []
    for line in test_output.split('\n')[3:-2]:
        non_empty_tokens = []
        for word_token in line.split(' '):
            if word_token:
                non_empty_tokens.append(word_token)
        if len(non_empty_tokens) > 1:
            all_lines.append(non_empty_tokens)
    df = pd.DataFrame(all_lines)
    return df


def create_markdown_string(df):
    """Create the markdown string."""
    markdown_string = df.to_markdown()
    return markdown_string


def create_issue(test_output):  # pylint: disable=W0613
    """
    Step 1.

    Create contents for the issue you want to post
    """
    df = create_df(test_output)
    issue_body = create_markdown_string(df)
    headers = {"Authorization": f"token {token}"}
    data = {
        "title": "Found a bug",
        "body": issue_body,
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
    res = requests.post(url, data=json.dumps(data), headers=headers)

    if res.status_code == 201:
        return True

    return False
