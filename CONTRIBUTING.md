# Contributing to GitHub Actions Examples

Thank you for your interest in contributing to the GitHub Actions Examples repository! This guide will help you understand how to contribute effectively.

## 🎯 How to Contribute

### Types of Contributions We Welcome

1. **New Workflow Examples**
   - Language-specific CI/CD workflows
   - Advanced automation patterns
   - Integration examples with third-party services
   - Best practice demonstrations

2. **Documentation Improvements**
   - Better explanations of existing workflows
   - Additional use cases and scenarios
   - Troubleshooting guides
   - Best practices documentation

3. **Bug Fixes**
   - Fixing syntax errors in workflows
   - Correcting documentation
   - Resolving broken examples

4. **Sample Applications**
   - Adding sample projects for testing workflows
   - Creating realistic test scenarios
   - Supporting multiple programming languages

## 📋 Contribution Guidelines

### Before You Start

1. **Check existing issues** to see if someone is already working on similar changes
2. **Open an issue** to discuss your proposed changes if they're significant
3. **Fork the repository** and create a new branch for your changes

### Workflow Example Guidelines

When adding new workflow examples, please ensure they:

#### ✅ Do Include:
- **Clear, descriptive names** for workflows and jobs
- **Comprehensive comments** explaining each step
- **Real-world scenarios** that developers actually encounter
- **Error handling** and proper status checks
- **Security best practices** (no hardcoded secrets, minimal permissions)
- **Cross-platform support** when applicable
- **Caching strategies** for dependencies and build artifacts

#### ❌ Avoid:
- Hardcoded secrets or sensitive information
- Overly complex examples that are hard to understand
- Workflows that only work in very specific environments
- Examples without proper documentation
- Duplicate functionality without clear differentiation

### Code Style and Standards

#### YAML Formatting
```yaml
# Use 2-space indentation
name: Example Workflow

# Always include helpful comments
on:
  push:
    branches: [ main ]  # Use square brackets for arrays
  pull_request:
    branches: [ main ]

# Use descriptive job names
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    
    steps:
    - name: Clear step descriptions
      uses: actions/checkout@v4  # Pin to specific versions
      
    - name: Another step
      run: |
        echo "Use pipe for multi-line commands"
        echo "Include helpful output messages"
```

#### Documentation Standards
- Use clear, concise language
- Include practical examples
- Explain the "why" not just the "how"
- Add links to relevant documentation
- Use proper markdown formatting

## 🚀 Getting Started

### 1. Set Up Your Development Environment

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/github-actions-examples.git
cd github-actions-examples

# Create a new branch for your changes
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Add your workflow to the appropriate directory (`.github/workflows/`)
- Include comprehensive comments and documentation
- Test your workflow if possible
- Update the README.md to reference your new example

### 3. Test Your Workflow

Before submitting, please:

- **Validate YAML syntax** using a YAML linter
- **Test the workflow** in your own repository if possible
- **Check for security issues** (no secrets, appropriate permissions)
- **Verify documentation** is clear and accurate

```bash
# Test YAML syntax
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/your-workflow.yml'))"

# Or use yamllint if available
yamllint .github/workflows/your-workflow.yml
```

### 4. Submit Your Contribution

```bash
# Commit your changes with a descriptive message
git add .
git commit -m "Add workflow example for [specific use case]

- Describe what the workflow does
- Mention key features or techniques demonstrated
- Reference any issues this addresses"

# Push to your fork
git push origin feature/your-feature-name

# Create a pull request on GitHub
```

## 📝 Pull Request Process

### Before Submitting
- [ ] Workflow YAML is properly formatted and commented
- [ ] Documentation is updated (README.md, workflow comments)
- [ ] No hardcoded secrets or sensitive information
- [ ] Workflow follows security best practices
- [ ] Sample files are included if needed
- [ ] Changes are tested and working

### Pull Request Template

When submitting a pull request, please include:

```markdown
## Description
Brief description of what this PR adds or changes.

## Type of Change
- [ ] New workflow example
- [ ] Documentation improvement
- [ ] Bug fix
- [ ] Sample application

## Workflow Details (if applicable)
- **Workflow name:** 
- **Primary use case:** 
- **Languages/tools involved:** 
- **Key features demonstrated:** 

## Testing
- [ ] YAML syntax validated
- [ ] Workflow tested in personal repository
- [ ] Documentation reviewed for accuracy
- [ ] No security issues identified

## Checklist
- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Commented code, particularly complex areas
- [ ] Documentation updated
- [ ] No breaking changes introduced
```

## 🎨 Example Workflow Structure

Here's a template for creating new workflow examples:

```yaml
name: Descriptive Workflow Name

# Clear description of when this workflow runs
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

# Set minimal required permissions
permissions:
  contents: read

jobs:
  # Use descriptive job names
  example-job:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Setup environment
      # Include version and reasoning for choices
      uses: actions/setup-node@v4
      with:
        node-version: '18'  # Use LTS version
        cache: 'npm'        # Enable caching
        
    - name: Descriptive step name
      run: |
        # Include helpful comments
        echo "What this step does and why"
        
    - name: Another step with error handling
      run: |
        if ! command -v tool; then
          echo "Installing required tool..."
          # Installation commands
        fi
        
        # Main command with error checking
        tool --version || exit 1
```

## 🤝 Community Guidelines

### Be Respectful and Inclusive
- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Accept constructive criticism gracefully
- Focus on what's best for the community

### Communication
- Be clear and constructive in code reviews
- Ask questions if something is unclear
- Provide helpful feedback and suggestions
- Celebrate others' contributions

## 🆘 Getting Help

If you need help or have questions:

1. **Check the documentation** - README.md and existing examples
2. **Search existing issues** - your question might already be answered
3. **Open a new issue** - we're happy to help!
4. **Join discussions** - participate in existing conversations

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [Security Best Practices](https://docs.github.com/en/actions/security-guides)
- [Action Marketplace](https://github.com/marketplace?type=actions)

## 🏆 Recognition

Contributors will be recognized in:
- The repository's contributor list
- Release notes for significant contributions
- Special mentions for outstanding examples

Thank you for helping make GitHub Actions more accessible to everyone! 🚀