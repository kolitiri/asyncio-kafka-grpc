run:
	poetry run python main.py

delete-env: ##@delete-env Delete the virtual environment
	@echo $(shell poetry run which python) | xargs dirname | xargs dirname | xargs rm -rf
