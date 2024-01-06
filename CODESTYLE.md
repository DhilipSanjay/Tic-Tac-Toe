# Tic-Tac-Toe Project Code Style and Local Setup Guide

## Code Style

This project adheres to a strict code style to maintain readability and consistency. We use several tools to enforce this style:

1. **Flake8**: A tool that combines PyFlakes, pycodestyle, and Ned Batchelder's McCabe script. It checks for style guide enforcement, programming errors like module imports and variable names, and complexity.

2. **Pylint**: A Python static code analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.

3. **Black**: A Python code formatter that re-formats your code to make it more readable and 'pythonic'. It adheres to PEP 8, the official Python style guide.

The code style checks are automated using GitHub Actions. Any push or pull request will trigger the checks.

## Local Setup

### IDE Setup

We recommend using Visual Studio Code (VS Code) as your IDE for this project. Here's how to set it up:

1. Download and install [VS Code](https://code.visualstudio.com/download).
2. Install Python, flake8, pylint and black extensions for VS Code from the marketplace.
3. Open the project folder in VS Code.

### Pre-commit Setup

Pre-commit is a tool that checks your code for any errors or discrepancies before you commit your code. Here's how to set it up:

1. Install pre-commit. If you have pip installed, you can do this by running `pip install pre-commit`.
2. In the project root directory, there is a file named `.pre-commit-config.yaml`.
3. Run `pre-commit install` to set up the git hook scripts.

Now, every time you commit your code, the pre-commit hook will run and check your code for any style or formatting issues. If any issues are found, the commit will be aborted, and you will be shown what issues were found.
