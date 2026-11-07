# TDD/BDD Final Project - Product Catalogue

This project implements a microservice-based product catalogue backend for an e-commerce application using Test Driven Development (TDD) and Behaviour Driven Development (BDD).

## Tech Stack
- **Flask** - Web framework
- **SQLAlchemy** - ORM
- **factory_boy** - Test data generation
- **Behave** - BDD testing
- **Selenium** - UI automation

## Project Structure
```
.
├── service/
│   ├── __init__.py       # Flask app initialization
│   ├── models.py         # Product model
│   ├── routes.py         # REST API routes
│   ├── common/
│   │   └── status.py     # HTTP status codes
│   └── static/
│       └── index.html    # Admin UI
├── tests/
│   ├── factories.py      # ProductFactory (factory_boy)
│   ├── test_models.py    # TDD model tests
│   └── test_routes.py    # TDD route tests
├── features/
│   ├── products.feature  # BDD scenarios (Gherkin)
│   ├── environment.py    # Behave environment setup
│   └── steps/
│       ├── load_steps.py # BDD data loading steps
│       └── web_steps.py  # BDD Selenium web steps
├── config.py
└── requirements.txt
```

## Running the Service
```bash
pip install -r requirements.txt
python -m flask run
```

## Running TDD Tests
```bash
python -m pytest tests/ -v
```

## Running BDD Tests
```bash
behave
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /products | List all products |
| GET | /products?name=X | Search by name |
| GET | /products?category=X | Search by category |
| GET | /products?available=true | Search by availability |
| GET | /products/{id} | Read a product |
| POST | /products | Create a product |
| PUT | /products/{id} | Update a product |
| DELETE | /products/{id} | Delete a product |


## Continuous Integration (GitHub Actions)

The GitHub Actions workflow at [`.github/workflows/workflow.yml`](.github/workflows/workflow.yml) runs on pushes, pull requests, and manual dispatch. It checks out the source, configures Python 3.11, installs project dependencies, runs a focused **flake8** lint check, and executes the unit tests with **pytest**.

## Tekton Tasks

The Tekton task definitions are in [`.tekton/tasks.yml`](.tekton/tasks.yml). The `cleanup` task clears the shared source workspace before a fresh run. The `nose` task name is retained to match the course submission requirement; because this repository's actual tests use pytest, that task installs and runs pytest against `tests/`.

## CI/CD Submission Evidence

See [`docs/CI-CD-SUBMISSION.md`](docs/CI-CD-SUBMISSION.md) for the submission checklist, evidence filenames, commands, and the distinction between GitHub Actions evidence and OpenShift console evidence.
