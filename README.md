# GitHub Actions Examples

A comprehensive collection of GitHub Actions workflow examples demonstrating various CI/CD patterns, automation techniques, and best practices.

## 📚 Table of Contents

- [Overview](#overview)
- [Basic Examples](#basic-examples)
- [Language-Specific Examples](#language-specific-examples)
- [Advanced Examples](#advanced-examples)
- [Utility Workflows](#utility-workflows)
- [Getting Started](#getting-started)
- [Best Practices](#best-practices)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains practical GitHub Actions examples that you can use as templates or reference for your own projects. Each workflow is thoroughly documented and demonstrates specific use cases and patterns.

### What's Included

- **Basic CI/CD workflows** - Simple examples to get started
- **Language-specific examples** - Tailored workflows for different programming languages
- **Advanced patterns** - Complex scenarios with matrices, conditions, and reusable workflows
- **Automation utilities** - Workflows for common repository management tasks

## 🚀 Basic Examples

### [Basic CI](/.github/workflows/basic-ci.yml)
A simple continuous integration workflow that demonstrates:
- Basic workflow structure
- Triggering on push and pull requests
- Running simple commands
- Using environment variables

```yaml
name: Basic CI
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

### [Build and Test](/.github/workflows/build-and-test.yml)
A more comprehensive workflow showing:
- Multi-job workflows with dependencies
- Artifact upload/download
- Matrix builds for multiple test suites
- Job interdependencies

### [Scheduled Workflow](/.github/workflows/scheduled-workflow.yml)
Demonstrates scheduled workflows:
- Cron-based scheduling
- Manual triggering with `workflow_dispatch`
- Daily maintenance tasks
- Report generation

## 💻 Language-Specific Examples

### [Node.js CI](/.github/workflows/nodejs-ci.yml)
Node.js specific workflow featuring:
- Multiple Node.js versions (16.x, 18.x, 20.x)
- Cross-platform testing (Ubuntu, Windows, macOS)
- npm caching
- Package.json creation and dependency management

### [Python CI](/.github/workflows/python-ci.yml)
Python development workflow with:
- Multiple Python versions (3.8, 3.9, 3.10, 3.11)
- pip caching
- Code linting with flake8
- Testing with unittest and pytest
- Cross-platform support

### [Docker Workflow](/.github/workflows/docker-workflow.yml)
Docker containerization workflow:
- Multi-platform image builds (linux/amd64, linux/arm64)
- Docker Buildx setup
- Image metadata extraction
- Security scanning simulation
- Registry push simulation

## 🔧 Advanced Examples

### [Matrix Builds](/.github/workflows/matrix-builds.yml)
Advanced matrix build strategies:
- Multi-dimensional matrices
- Dynamic matrix generation
- Complex configurations with includes/excludes
- Conditional matrix execution

### [Conditional Workflows](/.github/workflows/conditional-workflow.yml)
Sophisticated conditional logic:
- Branch-based conditions
- File change detection
- Environment-based execution
- Manual trigger inputs
- Complex conditional expressions

## 🛠️ Utility Workflows

### [Auto Labeler](/.github/workflows/auto-labeler.yml)
Automatic labeling system:
- PR analysis based on file changes
- Issue content analysis
- Size-based labeling
- Keyword detection
- Automated team assignment

### [Release Automation](/.github/workflows/release-automation.yml)
Complete release automation:
- Version validation
- Changelog generation
- Build artifact creation
- GitHub release creation
- Notification systems

## 🏁 Getting Started

### 1. Choose a Workflow
Browse the examples above and find one that matches your needs.

### 2. Copy to Your Repository
Create a `.github/workflows/` directory in your repository and copy the desired workflow file.

### 3. Customize
Modify the workflow to match your specific requirements:
- Update trigger conditions
- Change build steps
- Add your specific testing commands
- Configure secrets and environment variables

### 4. Test
Create a pull request or push to trigger the workflow and verify it works as expected.

## 📋 Best Practices

### Security
- **Never commit secrets** - Use GitHub secrets for sensitive data
- **Use minimal permissions** - Specify only required permissions
- **Pin action versions** - Use specific versions like `actions/checkout@v4`
- **Validate inputs** - Always validate workflow inputs and parameters

### Performance
- **Use caching** - Cache dependencies and build artifacts
- **Parallel jobs** - Run independent jobs in parallel
- **Conditional execution** - Skip unnecessary steps with conditions
- **Artifact management** - Clean up old artifacts regularly

### Maintainability
- **Clear naming** - Use descriptive names for workflows and jobs
- **Documentation** - Comment complex logic and conditions
- **Modular design** - Break complex workflows into smaller, reusable pieces
- **Error handling** - Include proper error handling and notifications

### Example Security Configuration
```yaml
permissions:
  contents: read    # Read repository contents
  issues: write     # Write to issues (for auto-labeling)
  pull-requests: write  # Write to PRs
```

### Example Caching Pattern
```yaml
- name: Cache dependencies
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

## 📖 Common Patterns

### Environment-based Deployment
```yaml
environment: ${{ github.ref == 'refs/heads/main' && 'production' || 'staging' }}
```

### File Change Detection
```yaml
- name: Check for changes
  uses: dorny/paths-filter@v2
  id: changes
  with:
    filters: |
      frontend:
        - 'src/**'
      backend:
        - 'api/**'
```

### Dynamic Matrix Generation
```yaml
jobs:
  setup:
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: echo "matrix=$(cat .github/matrix.json)" >> $GITHUB_OUTPUT
```

## 🤝 Contributing

Contributions are welcome! If you have useful workflow examples or improvements:

1. Fork this repository
2. Create a feature branch
3. Add your workflow example with documentation
4. Submit a pull request

### Guidelines for Contributions
- Include clear documentation and comments
- Follow the existing naming conventions
- Test your workflows before submitting
- Add your example to this README

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Action Marketplace](https://github.com/marketplace?type=actions)
- [GitHub Actions Community](https://github.com/actions)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Happy automating! 🚀*