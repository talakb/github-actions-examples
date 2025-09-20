# GitHub Actions Examples

This repository contains simple examples of GitHub Actions workflows to help you get started.

## Simple Example

The `simple-example.yml` workflow demonstrates the basics of GitHub Actions:

- **File**: `.github/workflows/simple-example.yml`
- **What it does**:
  - Checks out the repository using `actions/checkout@v4`
  - Echoes a simple message
  - Shows basic information about the checked out repository
- **When it runs**: On push and pull requests to main/master branches
- **Runs on**: Ubuntu latest

This example covers the fundamental GitHub Actions concepts:
- Workflow triggers (`on`)
- Jobs and runners (`jobs`, `runs-on`)
- Steps with actions and commands (`steps`, `uses`, `run`)

### Usage

The workflow will automatically run when you:
1. Push code to the main or master branch
2. Create a pull request targeting main or master branch

You can also manually trigger it from the Actions tab in your GitHub repository.