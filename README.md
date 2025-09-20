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

### [Reusable Workflows](/.github/workflows/reusable-build.yml)
Modular workflow components:
- Parameterized build workflows
- Input/output handling
- Secret management
- Cross-repository reuse

### [Call Reusable Workflow](/.github/workflows/call-reusable-workflow.yml)
Demonstrates reusable workflow usage:
- Multiple environment builds
- Matrix strategies with reusable workflows
- Output consumption
- Conditional workflow calls

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

### [Code Quality Checks](/.github/workflows/code-quality.yml)
Comprehensive quality analysis:
- Linting and formatting checks
- Security vulnerability scanning
- Code complexity analysis
- Documentation quality assessment
- Automated quality reporting

### [Security Scanning](/.github/workflows/security-scan.yml)
Multi-layered security analysis:
- Dependency vulnerability scanning
- Code security analysis (SAST)
- Container security scanning
- Automated security reporting
- Remediation recommendations

### [Deploy to Pages](/.github/workflows/deploy-to-pages.yml)
GitHub Pages deployment:
- Static site generation
- Automated documentation deployment
- Multi-environment support
- Custom domain configuration

## 📊 Complete Workflow Index

| Category | Workflow | Purpose | Key Features |
|----------|----------|---------|--------------|
| **Basic** | [Basic CI](/.github/workflows/basic-ci.yml) | Simple CI demonstration | Basic triggers, environment variables |
| **Basic** | [Build and Test](/.github/workflows/build-and-test.yml) | Multi-job workflow | Artifacts, dependencies, matrices |
| **Basic** | [Scheduled Workflow](/.github/workflows/scheduled-workflow.yml) | Cron automation | Scheduled runs, manual triggers |
| **Language** | [Node.js CI](/.github/workflows/nodejs-ci.yml) | Node.js testing | Multi-version, cross-platform, caching |
| **Language** | [Python CI](/.github/workflows/python-ci.yml) | Python development | Multiple versions, linting, testing |
| **Language** | [Docker Workflow](/.github/workflows/docker-workflow.yml) | Container builds | Multi-platform, security scanning |
| **Advanced** | [Matrix Builds](/.github/workflows/matrix-builds.yml) | Complex matrices | Dynamic generation, includes/excludes |
| **Advanced** | [Conditional Workflows](/.github/workflows/conditional-workflow.yml) | Conditional logic | Branch conditions, file changes |
| **Advanced** | [Reusable Build](/.github/workflows/reusable-build.yml) | Reusable components | Parameters, outputs, secrets |
| **Advanced** | [Call Reusable](/.github/workflows/call-reusable-workflow.yml) | Using reusable workflows | Multiple calls, matrices, outputs |
| **Utility** | [Auto Labeler](/.github/workflows/auto-labeler.yml) | Automatic labeling | PR analysis, content detection |
| **Utility** | [Release Automation](/.github/workflows/release-automation.yml) | Release management | Versioning, changelogs, artifacts |
| **Utility** | [Code Quality](/.github/workflows/code-quality.yml) | Quality analysis | Linting, complexity, documentation |
| **Utility** | [Security Scanning](/.github/workflows/security-scan.yml) | Security analysis | Dependency, code, container scanning |
| **Utility** | [Deploy to Pages](/.github/workflows/deploy-to-pages.yml) | Static site deployment | GitHub Pages, documentation |

## 📁 Sample Applications


The repository includes sample applications that you can use to test the workflows:

### [Node.js Sample App](/sample-apps/nodejs/)
- Simple Express-like application with functions to test
- Unit tests demonstrating testing patterns  
- Package.json with common npm scripts
- Demonstrates JavaScript/TypeScript workflow patterns

### [Python Sample App](/sample-apps/python/)
- Python application with basic functions
- Comprehensive unit tests using unittest
- Requirements.txt with development dependencies
- Demonstrates Python testing and linting workflows

These sample applications are used by the workflows to demonstrate real testing and building scenarios. You can run them locally:

```bash
# Node.js example
cd sample-apps/nodejs
node test.js

# Python example  
cd sample-apps/python
python3 test_app.py
```

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

Please read our [Contributing Guidelines](CONTRIBUTING.md) for detailed information on how to contribute effectively.

### Guidelines for Contributions
- Include clear documentation and comments
- Follow the existing naming conventions
- Test your workflows before submitting
- Add your example to this README and the workflow index
- Ensure security best practices are followed

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Action Marketplace](https://github.com/marketplace?type=actions)
- [GitHub Actions Community](https://github.com/actions)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Happy automating! 🚀*