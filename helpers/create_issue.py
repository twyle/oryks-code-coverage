# -*- coding: utf-8 -*-
"""This module creates and executes the GitHub Action Code that shows code coverage."""
import os
from pprint import pprint

from github import Github


def create_issue():
    """Create an issue on GitHub."""
    owner = "twyle"
    repo = "flask-social-auth"

    token = os.getenv('INPUT_GITHUB_TOKEN')

    g = Github(token)

    repo = g.get_repo(f"{owner}/{repo}")

    i = repo.create_issue(
        title="Issue Title",
        body="Text of the body.",
        assignee=owner,
        labels=[
            repo.get_label("good first issue")
        ]
    )

    pprint(i)

    issues = repo.get_issues(state="open")
    pprint(issues.get_page(0))
