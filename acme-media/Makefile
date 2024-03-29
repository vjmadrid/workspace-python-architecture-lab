#
# Makefile for Project Management
#  

.DEFAULT_GOAL := help

# *** GENERAL ***

upgrade: ## Upgrade Python modules : pip and setuptools
	pip install -U pip setuptools wheel



# *** DEPENDENCIES ***

deps-install-dev: ## Install dependencies 'dev-requirements.txt' file (No versions)
	pip install -Ur dev-requirements.txt
	make deps-generate-requirements

deps-generate-requirements: ## Generate 'requirements-version.txt' file (With versions)
	pip freeze | grep -v -- '^-e' > requirements.txt

deps-install: ## Install dependencies 'requirements.txt' file (With versions)
	pip install -Ur requirements.txt

deps-tree: ## Show dependency tree of packages
	pipdeptree

deps-reset: ## Reset all requirements
	pip freeze | xargs pip uninstall -y



# *** QA ****

lint: ## Lint and static-check code
	flake8 --version
	flake8 .
	pylint --version
	pylint acmemedia
	pylint tests

format-check: ## Format check code
	black . --check --color --diff

format: ## Format code
	black .



# *** TEST ***

test: clean ## Run all the tests with all the supported python interpreters 
	pytest -ra

test-lint: ## Lint and static-check code
	pytest --cache-clear --flake8

coverage: ## Run tests with coverage
	coverage erase
	coverage run --include=acmecommon/* -m pytest -ra
	coverage report -m



# *** DOCS ***

docs: ## Create the documentation
	@echo "Build completed"
	cd ./docs/sphinx && make html



# *** INSTALL / UNINSTALL ***

install: uninstall ## Distribute package install local
	python3 setup.py develop

uninstall: ## Distribute package uninstall local
	python3 setup.py develop --uninstall



# *** DISTRIBUTE ***

distribute-package-install: ## Distribute package install
	pip install -Ue .

distribute-install: ## Distribute package install by setup.py
	python3 setup.py install

distribute-local: ## Distribute package mode local (folder : sdist)
	python3 setup.py sdist



# *** CLEAN ***

clean-build: ## Remove elements for build
	find . -name '__pycache__' -type d | xargs rm -fr
	find . -name '.pytest_cache' -type d | xargs rm -fr
	find . -name '*.pytest_cache' -type d | xargs rm -fr
	find . -name '*.pyc' -type d | xargs rm -fr

clean-distribute: clean-build ## Remove *.egg-info files and *.egg, build and dist directories
	rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info ./*.egg
	find . -name '*.egg-info/' -type d | xargs rm -fr

clean : clean-distribute ## Remove *.pyc files and __pycache__ directory



# *** BUILD ***

build: ## Build
	make clean
	make deps-install-dev
	make lint
	make test
	make docs
	make install
	@echo "Build completed"



# *** RUN ***

run: ## Run
	@echo "N/A"



# *** UPLOAD ****
upload: ## Upload
	python3 setup.py 
	@echo "Upload completed"


# *** HELP ***

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [target]"; \
	printf "%-40s %s\n" "target" "help" ; \
	printf "%-40s %s\n" "----------------------------------" "----------------------------------" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-40s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
	@echo "Check the Makefile to know exactly what each target is doing"


.PHONY: init test