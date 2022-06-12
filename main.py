# -*- coding: utf-8 -*-
"""This module creates and executes the GitHub Action Code that shows code coverage."""
import json
import os
import subprocess
from os.path import exists
from pprint import pprint

import requests

from helpers.create_issue import create_issue


def main():
    """Generate coverage report for a given project."""
    code_directory = os.getenv('INPUT_CODEDIRECTORY')
    test_directory = os.getenv('INPUT_TESTDIRECTORY')
    pycov_config_file = os.getenv('INPUT_PYCOVCONFIGFILE')
    pytest_config_file = os.getenv('INPUT_PYTESTCONFIGFILE')

    if code_directory and test_directory:
        print(f'The code directory is {code_directory} and test directory is {test_directory}')
        p = subprocess.run(["python", "-m", "pytest", f"--cov={code_directory}",
                            test_directory], capture_output=True, text=True, check=True)
        subprocess.run(["python", "-m", "pytest", "--cov-report=xml",
                        f"--cov={code_directory}", test_directory], capture_output=True, text=True, check=True)
        if pycov_config_file:
            p = subprocess.run(["python", "-m", "pytest", f"--cov-config={pycov_config_file}",
                                f"--cov={code_directory}", test_directory], capture_output=True, text=True, check=True)
            subprocess.run(["python", "-m", "pytest", "--cov-report=xml", f"--cov-config={pycov_config_file}",
                            f"--cov={code_directory}", test_directory], capture_output=True, text=True, check=True)
        elif pytest_config_file:
            p = subprocess.run(["python", "-m", "pytest", f"--cov-config={pytest_config_file}",
                                f"--cov={code_directory}", test_directory], capture_output=True, text=True, check=True)
            subprocess.run(["python", "-m", "pytest", "--cov-report=xml", f"--cov-config={pytest_config_file}",
                            f"--cov={code_directory}", test_directory], capture_output=True, text=True, check=True)
    else:
        code_directory = '.'
        test_directory = 'tests/'
        # print(f'The code directory is {code_directory} and test directory is {test_directory}')
        p = subprocess.run(["python", "-m", "pytest", f"--cov={code_directory}",
                            test_directory], capture_output=True, text=True, check=True)
        subprocess.run(["python", "-m", "pytest", "--cov-report=xml",
                        f"--cov={code_directory}", test_directory], capture_output=True, text=True, check=True)

    test_output = p.stdout

    # print(test_output)

    create_issue(test_output)

    print(f"::set-output name=TESTCOVERAGE::{test_output}")


if __name__ == "__main__":
    main()
