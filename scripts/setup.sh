#!/bin/bash

# ASCII Cinema Project Structure Setup Script
# This script creates all directories and files for the project

echo "Creating ASCII Cinema project structure..."

# Create main project directory
mkdir -p ascii-cinema

# Change to project directory
cd ascii-cinema

# Create package directory
mkdir -p ascii_cinema

# Create tests directory
mkdir -p tests

# Create __pycache__ directories (will be populated later)
mkdir -p ascii_cinema/__pycache__
mkdir -p tests/__pycache__

# Create all Python files in ascii_cinema package
touch ascii_cinema/__init__.py
touch ascii_cinema/__main__.py
touch ascii_cinema/converter.py
touch ascii_cinema/player.py
touch ascii_cinema/styles.py

# Create test file
touch tests/__init__.py
touch tests/test_ascii_cinema.py

# Create configuration files
touch pyproject.toml
touch requirements.txt
touch requirements-dev.txt

# Create documentation files
touch README.md
touch SETUP.md
touch PROJECT_SUMMARY.md
touch LICENSE

# Create development files
touch Makefile
touch .gitignore

# Create additional utility files
touch .coveragerc
touch pytest.ini

# Set executable permissions for Python package entry point
chmod +x ascii_cinema/__main__.py

# Set executable permissions for Makefile
chmod +x Makefile

# Set read/write permissions for all Python source files
chmod 644 ascii_cinema/__init__.py
chmod 644 ascii_cinema/converter.py
chmod 644 ascii_cinema/player.py
chmod 644 ascii_cinema/styles.py

# Set read/write permissions for test files
chmod 644 tests/__init__.py
chmod 644 tests/test_ascii_cinema.py

# Set read/write permissions for configuration files
chmod 644 pyproject.toml
chmod 644 requirements.txt
chmod 644 requirements-dev.txt
chmod 644 .coveragerc
chmod 644 pytest.ini

# Set read/write permissions for documentation
chmod 644 README.md
chmod 644 SETUP.md
chmod 644 PROJECT_SUMMARY.md
chmod 644 LICENSE

# Set read/write permissions for .gitignore
chmod 644 .gitignore

# Set directory permissions
chmod 755 ascii_cinema
chmod 755 tests

echo "✓ Directory structure created"
echo "✓ All files created"
echo "✓ Permissions set"
echo ""
echo "Project structure ready at: $(pwd)"
echo ""
echo "Next steps:"
echo "1. Copy the file contents into each file"
echo "2. Create a virtual environment: python3 -m venv venv"
echo "3. Activate it: source venv/bin/activate"
echo "4. Install: pip install -e '.[dev,video]'"
echo "5. Run tests: pytest --cov=ascii_cinema"
