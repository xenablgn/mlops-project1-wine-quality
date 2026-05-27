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

- `pyproject.toml`: central lint/format settings (`ruff`, `black` defaults).
- `.pre-commit-config.yaml`: pre-commit hooks (`ruff --fix`, `ruff-format`).
- `.github/workflows/ci.yml`: CI checks for lint and format validation.

### 1. Install dev tools

```bash
python -m pip install -r requirements-dev.txt
```

### 2. Run formatter locally

```bash
ruff format .
```

### 3. Run lint checks locally

```bash
ruff check .
```

### 4. Auto-fix lint issues

```bash
ruff check . --fix
```

### 5. Enable pre-commit hooks

```bash
python -m pre_commit install
pre-commit run --all-files
```

### 6. CI validation

Your CI pipeline runs the following checks on every push and pull request:

```bash
ruff check .
ruff format --check .
```

### VS Code Tasks

Open Command Palette and run `Tasks: Run Task`, then choose one of:

- `Install Dev Tools`
- `Format Code`
- `Lint Code`
- `Lint and Auto-fix`
- `Quality: format + lint`
- `Enable Pre-commit`