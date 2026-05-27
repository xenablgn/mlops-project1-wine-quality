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

## Code Quality (Format + Lint)

This project includes a Ruff-first code quality workflow for all Python code.

Configuration sources:

## brew install go-task/tap/go-task   # mac

- `pyproject.toml`: central lint/format settings (`ruff`, `black` defaults).
- `.pre-commit-config.yaml`: pre-commit hooks (`ruff --fix`, `ruff-format`).
- `.github/workflows/ci.yml`: CI checks for lint and format validation.
- `Taskfile.yml`: local automation

### 1. Install dev tools:
- brew install go-task/tap/go-task 

### VS Code Tasks

Open Command Palette and run `Tasks: Run Task`, then choose one of:

- `Install Dev Tools`
- `Format Code`
- `Lint Code`
- `Lint and Auto-fix`
- `Quality: format + lint`
- `Enable Pre-commit`