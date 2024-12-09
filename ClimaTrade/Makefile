# Define variables
APP_NAME = app.py
VENV_DIR = venv
REQUIREMENTS = requirements.txt

# Run the Dash app
.PHONY: run
run:
	$(VENV_DIR)/bin/python $(APP_NAME)

# Install or update dependencies
.PHONY: install
install:
	python3 -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)
	@echo "Dependencies installed/updated."

# Clean up the project
.PHONY: clean
clean:
	rm -rf $(VENV_DIR) __pycache__ */__pycache__
	find . -type f -name "*.pyc" -delete
	@echo "Project cleaned. Virtual environment and cache files removed."
