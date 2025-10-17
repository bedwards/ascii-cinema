# ASCII Cinema - Raw Setup Commands
# Copy and paste these commands one at a time in your terminal

# Create and enter project directory
mkdir -p ascii-cinema
cd ascii-cinema

# Create package directory
mkdir -p ascii_cinema

# Create tests directory
mkdir -p tests

# Create Python package files
touch ascii_cinema/__init__.py
touch ascii_cinema/__main__.py
touch ascii_cinema/converter.py
touch ascii_cinema/player.py
touch ascii_cinema/styles.py

# Create test files
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

# Set permissions - Python package files
chmod 644 ascii_cinema/__init__.py
chmod 755 ascii_cinema/__main__.py
chmod 644 ascii_cinema/converter.py
chmod 644 ascii_cinema/player.py
chmod 644 ascii_cinema/styles.py

# Set permissions - Test files
chmod 644 tests/__init__.py
chmod 644 tests/test_ascii_cinema.py

# Set permissions - Configuration files
chmod 644 pyproject.toml
chmod 644 requirements.txt
chmod 644 requirements-dev.txt

# Set permissions - Documentation files
chmod 644 README.md
chmod 644 SETUP.md
chmod 644 PROJECT_SUMMARY.md
chmod 644 LICENSE

# Set permissions - Development files
chmod 644 Makefile
chmod 644 .gitignore

# Set permissions - Directories
chmod 755 ascii_cinema
chmod 755 tests
