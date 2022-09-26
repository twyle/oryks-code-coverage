# -*- coding: utf-8 -*-
"""This module creates and executes the GitHub Action Code that shows code coverage."""
import os
import subprocess
from os.path import exists

from helpers.create_issue import create_issue
from helpers.upload_data import upload_data


def main():
    """Generate coverage report for a given project."""
    code_directory = os.getenv('INPUT_CODEDIRECTORY')
    test_directory = os.getenv('INPUT_TESTDIRECTORY')
    pycov_config_file = os.getenv('INPUT_PYCOVCONFIGFILE')
    pytest_config_file = os.getenv('INPUT_PYTESTCONFIGFILE')

    if code_directory and test_directory:
        p = subprocess.run(["python", "-m", "pytest", f"--cov={code_directory}",
                            test_directory], capture_output=True, text=True, check=True)
        if pycov_config_file:
            p = subprocess.run(["python", "-m", "pytest", f"--cov-config={pycov_config_file}",
                                f"--cov={code_directory}", test_directory], capture_output=True, text=True, check=True)
        elif pytest_config_file:
            p = subprocess.run(["python", "-m", "pytest", f"--cov-config={pytest_config_file}",
                                f"--cov={code_directory}", test_directory], capture_output=True, text=True, check=True)
    else:
        code_directory = '.'
        test_directory = 'tests/'
        p = subprocess.run(["python", "-m", "pytest", f"--cov={code_directory}",
                            test_directory], capture_output=True, text=True, check=True)

    test_output = p.stdout

    if create_issue(test_output):
        print("::set-output name=TESTCOVERAGE::true")
        upload_data(test_output)
    else:
        print("::set-output name=TESTCOVERAGE::false")


if __name__ == "__main__":
    main()
