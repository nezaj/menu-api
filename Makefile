MAKEFLAGS = --no-print-directory --always-make --silent
MAKE = make $(MAKEFLAGS)

VENV_NAME = menu-api
VENV_PATH = ~/.virtualenvs/$(VENV_NAME)
VENV_ACTIVATE = . $(VENV_PATH)/bin/activate

.PHONY: clean check virtualenv pep8 pylint test

clean:
	find . -name "*.pyc" -print -delete
	find . \( -name "*.min.js" -o -name "*.min.css" \) -print -delete
	rm -rfv $(VENV_PATH)

check:
	$(MAKE) virtualenv
	$(MAKE) pylint pep8 test

virtualenv:
	test -d $(VENV_PATH) || virtualenv $(VENV_PATH)
	$(VENV_ACTIVATE) && pip install -r requirements.txt

pep8:
	@echo "Running pep8..."
	$(VENV_ACTIVATE) && pep8 src test *.py

pylint:
	@echo "Running pylint..."
	$(VENV_ACTIVATE) && pylint src test *.py

test:
	@echo "Running py.test..."
	$(VENV_ACTIVATE) && APP_ENV=test py.test test --tb=short
