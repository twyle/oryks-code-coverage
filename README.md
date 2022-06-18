# oryks-code-coverage

> This GitHub Action shows Code Coverage for a given project.


![Custom badge](https://img.shields.io/endpoint?style=flat-square&url=https%3A%2F%2Foryks-code-coverage-dev.herokuapp.com%2Fapi%2Fbadge)
[![security: bandit][bandit-image]][bandit-url]
[![Imports: isort][isort-image]][isort-url]
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

This GitHub Action shows code Coverage for a given python project using Pytest Coverage. To use this action, your project must have tests written using pytest and stored in a test folder. You can read about how it was developed over at [How To Create a GitHub Action that Shows Code Coverage using Pytest](https://medium.com/@lyle-okoth/creating-a-pytest-github-action-that-shows-code-coverage-b0d11655b748)

![](oryks-coverage-run.png)

## Inputs

## `codedirectory`

**Required** The directory containing the source code. Default `"."`.

## `testdirectory`

**Required** The directory containing the tests. Default `"tests\"`.

## `pycovconfigfile`

**Optional** The pycov configuration file Default `".coveragerc"`.

## `pytestconfigfile`

**Optional** The pytest configuration file. Default `"setup.cfg"`.
## `github_token`

**Required** The GitHub Token. Default `"${{ github.token }}"`.

## `github_token`

**Required** The GitHub Token. Default `"."`.

## `oryks_token`

**Required** The Code Coverage. Default `"."`

## Outputs

## `testcoverage`

The Test coverage

## Example usage
```
- name: oryks code coverage action
  id: selftest
  uses: twyle/oryks-code-coverage@v0.17.1
  with:
    codedirectory: src/
    testdirectory: tests/
    github_token: ${{ github.token }}
    oryks_token: ${{ secrets.ORYKS_TOKEN }}

- name: action output
  run: |
    echo "${{ steps.selftest.outputs.testcoverage }}
```

## v0.15.0 (2022-06-13)

### Feat

- using a python3.95 image.

## v0.14.2 (2022-06-13)

### Fix

- added the numpy dependancy.

## v0.14.1 (2022-06-13)

### Fix

- added the numpy dependancy.

## v0.14.0 (2022-06-13)

### Feat

- rendering the markdown.

### Fix

- using v0.13.0

## v0.13.0 (2022-06-12)

### Feat

- creating the issue from the code.

### Fix

- using v0.12.0

## v0.12.0 (2022-06-12)

### Feat

- substituting.

### Fix

- using v0.11.0

## v0.11.0 (2022-06-12)

### Feat

- rendering markdown.

### Fix

- using v0.10.

## v0.10.0 (2022-06-12)

### Feat

- using markdown.
- rendering markdown.

## v0.9.0 (2022-06-12)

### Feat

- rendering markdown.

### Fix

- using env vars.

## v0.8.0 (2022-06-12)

### Fix

- using env vars.

### Feat

- showing test output.

## v0.7.0 (2022-06-12)

### Feat

- showing test output.

### Fix

- using v0.6.0

## v0.6.0 (2022-06-12)

### Feat

- using the values from github.

### Fix

- using v0.5.0

## v0.5.0 (2022-06-12)

### Feat

- suding requests

### Fix

- added the ccfi requirement.

## v0.4.2 (2022-06-12)

### Fix

- added the ccfi requirement.

## v0.4.1 (2022-06-12)

### Fix

- added the ccfi requirement.
- updated the version.

## v0.4.0 (2022-06-12)

### Fix

- fixed the module import.
- updated the repo token.

### Feat

- creating an issue.

## v0.3.0 (2022-06-12)

### Feat

- creating an issue.
- updated the project description.
- testing out the workflow.

## v0.2.0 (2022-05-29)

### Feat

- created the pycov action.
- added code checkout.
- added code checkout.
- added code checkout.

## v0.1.0 (2022-05-27)

### Feat

- added code checkout.

## v0.0.1 (2022-05-27)

### Feat

- testing the action on GitHub.
- testing the action on GitHub.

[bandit-image]: https://img.shields.io/badge/security-bandit-yellow.svg
[bandit-url]: https://github.com/PyCQA/bandit

[isort-image]: https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336

[isort-url]: https://pycqa.github.io/isort/
