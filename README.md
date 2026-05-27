# End to End Data Science Project

### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py

## Code Quality & Cleaning Policy

This project enforces a strict code quality and cleaning policy using automated tools and tasks. All Python code must be formatted and linted before merging or deployment.

### Code Cleaning Workflow

1. **Install Dev Tools**
	 - Install [go-task](https://taskfile.dev/#/installation) (required for task automation):
		 ```sh
		 brew install go-task/tap/go-task  # macOS
		 ```
	 - Install Python dev dependencies:
		 ```sh
		 pip install -r requirements-dev.txt
		 ```

2. **Format Code**
	 - Run the following command to auto-format all Python files using [ruff format](https://docs.astral.sh/ruff/formatter/) and [black](https://black.readthedocs.io/en/stable/):
		 ```sh
		 task format
		 ```

3. **Lint Code**
	 - Run the following command to check for lint errors using [ruff](https://docs.astral.sh/ruff/):
		 ```sh
		 task lint
		 ```

4. **Auto-fix Lint Issues**
	 - To automatically fix lint issues:
		 ```sh
		 task lint -- --fix
		 ```

5. **Pre-commit Hooks**
	 - Enable pre-commit hooks to enforce code quality on every commit:
		 ```sh
		 task enable-pre-commit
		 ```

6. **CI/CD Enforcement**
	 - All code is checked for formatting and linting in CI via `.github/workflows/ci.yml`.

### Configuration Sources

- `pyproject.toml`: Central lint/format settings (`ruff`, `black` defaults)
- `.pre-commit-config.yaml`: Pre-commit hooks (`ruff --fix`, `ruff-format`)
- `.github/workflows/ci.yml`: CI checks for lint and format validation
- `Taskfile.yml`: Local automation

### VS Code Tasks

Open Command Palette and run `Tasks: Run Task`, then choose one of:

- `Install Dev Tools`
- `Format Code`
- `Lint Code`
- `Lint and Auto-fix`
- `Quality: format + lint`
- `Enable Pre-commit`

## ⚡ Ruff (Linter + Formatter + Import Cleaner)
### What Ruff does:

- ✔ **Finds bugs in code (linting)**
- ✔ **Checks coding style issues**
- ✔ **Fixes import order automatically**
- ✔ **Formats code (basic formatting)**
- ✔ **Very fast compared to older tools**

## 🖤 Black (Code Formatter)
### What Black does:

- ✔ **Automatically formats Python code to a consistent style**
- ✔ **Enforces PEP 8 and opinionated formatting rules**
- ✔ **Removes code style debates by using a single format**
- ✔ **Works well with Ruff for fast, reliable formatting**

## 🛠️ Linting, Formatting, and Import Cleaning

- **Linting:** Detects code errors, bugs, and style violations (handled by Ruff)
- **Formatting:** Automatically reformats code for consistency (handled by Black and Ruff)
- **Import Cleaning:** Sorts and removes unused imports (handled by Ruff)

> **Best Practice:** Always run `task format` and `task lint` before committing or pushing code to ensure your codebase is clean and consistent.
