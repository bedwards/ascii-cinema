#!/bin/bash

# ASCII Cinema Project Structure Setup Script
# One command per line - explicit version

echo "Creating ASCII Cinema project structure..."
echo ""

# Create main project directory
mkdir -p ascii-cinema
cd ascii-cinema

# Create directories - one per line
mkdir -p ascii_cinema
mkdir -p tests

# Create Python package files - one per line
touch ascii_cinema/__init__.py
touch ascii_cinema/__main__.py
touch ascii_cinema/converter.py
touch ascii_cinema/player.py
touch ascii_cinema/styles.py

# Create test files - one per line
touch tests/__init__.py
touch tests/test_ascii_cinema.py

# Create configuration files - one per line
touch pyproject.toml
touch requirements.txt
touch requirements-dev.txt

# Create documentation files - one per line
touch README.md
touch SETUP.md
touch PROJECT_SUMMARY.md
touch LICENSE

# Create development/build files - one per line
touch Makefile
touch .gitignore

# Set permissions for Python package files - one per line
chmod 644 ascii_cinema/__init__.py
chmod 755 ascii_cinema/__main__.py
chmod 644 ascii_cinema/converter.py
chmod 644 ascii_cinema/player.py
chmod 644 ascii_cinema/styles.py

# Set permissions for test files - one per line
chmod 644 tests/__init__.py
chmod 644 tests/test_ascii_cinema.py

# Set permissions for configuration files - one per line
chmod 644 pyproject.toml
chmod 644 requirements.txt
chmod 644 requirements-dev.txt

# Set permissions for documentation files - one per line
chmod 644 README.md
chmod 644 SETUP.md
chmod 644 PROJECT_SUMMARY.md
chmod 644 LICENSE

# Set permissions for development files - one per line
chmod 644 Makefile
chmod 644 .gitignore

# Set directory permissions - one per line
chmod 755 ascii_cinema
chmod 755 tests

echo ""
echo "✓ Project structure created successfully!"
echo ""
echo "Project location: $(pwd)"
echo ""
echo "Directory tree:"
echo "ascii-cinema/"
echo "├── ascii_cinema/"
echo "│   ├── __init__.py"
echo "│   ├── __main__.py"
echo "│   ├── converter.py"
echo "│   ├── player.py"
echo "│   └── styles.py"
echo "├── tests/"
echo "│   ├── __init__.py"
echo "│   └── test_ascii_cinema.py"
echo "├── pyproject.toml"
echo "├── requirements.txt"
echo "├── requirements-dev.txt"
echo "├── README.md"
echo "├── SETUP.md"
echo "├── PROJECT_SUMMARY.md"
echo "├── LICENSE"
echo "├── Makefile"
echo "└── .gitignore"
echo ""
echo "Next steps:"
echo "1. Copy the file contents from the artifacts into each file"
echo "2. python3 -m venv venv"
echo "3. source venv/bin/activate"
echo "4. pip install -e '.[dev,video]'"
echo "5. pytest --cov=ascii_cinema"
echo ""
