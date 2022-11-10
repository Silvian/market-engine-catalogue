# Creates the default virtual environment to run.

.PHONY: env
env:
	pyenv uninstall -f market-engine-catalogue
	pyenv virtualenv 3.10.6 market-engine-catalogue

# Generates the requirements.txt file without installing the dependencies.

.PHONY: reqs
reqs:
	pip install --upgrade pip pip-tools
	pip-compile --no-emit-index-url
	pip-compile --no-emit-index-url requirements-dev.in

# Installs dependencies needed to run the project.

.PHONY: deps
deps: reqs
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt requirements-dev.txt

# Upgrades and installs all project dependencies.

.PHONY: upgrade
upgrade:
	pip install --upgrade pip pip-tools
	pip-compile --upgrade --no-emit-index-url
	pip-compile --upgrade --no-emit-index-url -f requirements-dev.in
	pip-sync requirements.txt requirements-dev.txt

# Formats all the code according to Black

.PHONY: format
format:
	isort .
	black .

# Cleans up containers, volumes, networks, etc.

.PHONY: clean
clean:
	docker-compose down --rmi all --volumes --remove-orphans

# Builds the Docker containers.

.PHONY: build
build:
	docker-compose build --parallel

# Tests the project using Docker Compose.

.PHONY: test
test: build
	docker-compose run --rm app pytest -p no:cacheprovider


# Runs the project using Docker Compose.

.PHONY: run
run:
	docker-compose up
