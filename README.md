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

This project now includes a full code-cleaning workflow for all Python code.

### 1. Install dev tools

```bash
python -m pip install -r requirements-dev.txt
```

### 2. Run formatter

```bash
python -m ruff format .
python -m isort .
```

### 3. Run lint checks

```bash
python -m ruff check .
```

### 4. Auto-fix lint issues

```bash
python -m ruff check . --fix
```

### 5. Optional: run checks before each commit

```bash
python -m pre_commit install
pre-commit run --all-files
```

### VS Code Tasks

Open Command Palette and run `Tasks: Run Task`, then choose one of:

- `Install Dev Tools`
- `Format Code`
- `Lint Code`
- `Lint and Auto-fix`
- `Quality: format + lint`
- `Enable Pre-commit`