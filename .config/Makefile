# Install and cache poetry
.PHONY: install-poetry
install-poetry:
	curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies with poetry
.PHONY: install-dependencies
install-dependencies:
	poetry install
	env POETRY_VIRTUALENVS_IN_PROJECT=true

# Lint with flake8
.PHONY: lint-flake8
lint-flake8:
	poetry run flake8 --ignore=E123,E126,E203,E402,E501,F401 --exclude=.venv .

# Lint with ruff
.PHONY: lint-ruff
lint-ruff:
	poetry run ruff check

# Static type checks with mypy
.PHONY: static-type-checks
static-type-checks:
	poetry run mypy datetime-tools/ --exclude '/site-packages/'

# Wily build and rank
.PHONY: wily-build-and-rank
wily-build-and-rank:
	poetry run wily build datetime-tools
	poetry run wily rank datetime-tools

# Run unit tests and make coverage report
.PHONY: run-tests-and-coverage
run-tests-and-coverage:
	poetry run pytest --cov=./ --cov-report xml:cov.xml

# Qualify code target
.PHONY: qualify-code
qualify-code: install-poetry install-dependencies lint-flake8 lint-ruff \
	static-type-checks wily-build-and-rank run-tests-and-coverage
