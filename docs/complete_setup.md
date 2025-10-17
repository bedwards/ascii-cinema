# ASCII Cinema - Complete Setup Commands

## Option 1: Run the Shell Script

Save the `setup_explicit.sh` script and run it:

```bash
# Make the script executable
chmod +x setup_explicit.sh

# Run the script
./setup_explicit.sh
```

## Option 2: Manual Setup (Command by Command)

Copy and paste these commands one at a time:

### 1. Create Project Structure

```bash
mkdir -p ascii-cinema
cd ascii-cinema
mkdir -p ascii_cinema
mkdir -p tests
```

### 2. Create All Files

```bash
# Package files
touch ascii_cinema/__init__.py
touch ascii_cinema/__main__.py
touch ascii_cinema/converter.py
touch ascii_cinema/player.py
touch ascii_cinema/styles.py

# Test files
touch tests/__init__.py
touch tests/test_ascii_cinema.py

# Config files
touch pyproject.toml
touch requirements.txt
touch requirements-dev.txt

# Documentation
touch README.md
touch SETUP.md
touch PROJECT_SUMMARY.md
touch LICENSE

# Dev files
touch Makefile
touch .gitignore
```

### 3. Set Permissions

```bash
# Python files
chmod 644 ascii_cinema/__init__.py
chmod 755 ascii_cinema/__main__.py
chmod 644 ascii_cinema/converter.py
chmod 644 ascii_cinema/player.py
chmod 644 ascii_cinema/styles.py

# Test files
chmod 644 tests/__init__.py
chmod 644 tests/test_ascii_cinema.py

# Config files
chmod 644 pyproject.toml
chmod 644 requirements.txt
chmod 644 requirements-dev.txt

# Docs
chmod 644 README.md
chmod 644 SETUP.md
chmod 644 PROJECT_SUMMARY.md
chmod 644 LICENSE

# Dev files
chmod 644 Makefile
chmod 644 .gitignore

# Directories
chmod 755 ascii_cinema
chmod 755 tests
```

### 4. Populate Files with Content

Now copy the content from each artifact into the corresponding file:

```bash
# Option A: Use a text editor
nano ascii_cinema/__init__.py
# (paste content, save, repeat for each file)

# Option B: Use cat with heredoc (example for one file)
cat > ascii_cinema/__init__.py << 'EOF'
"""
ASCII Cinema - Convert images and videos to ASCII art
"""

__version__ = "1.0.0"
__author__ = "ASCII Cinema Team"
__license__ = "MIT"

from ascii_cinema.converter import ASCIIConverter
from ascii_cinema.player import ASCIIPlayer
from ascii_cinema.styles import ASCIIStyle

__all__ = ["ASCIIConverter", "ASCIIPlayer", "ASCIIStyle"]
EOF
```

### 5. Setup Python Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install package in development mode
pip install -e ".[dev,video]"
```

### 6. Verify Installation

```bash
# Run tests
pytest --cov=ascii_cinema --cov-report=term-missing

# Check CLI works
ascii-cinema --help

# Create a test image
python3 -c "from PIL import Image; img=Image.new('RGB',(200,200)); [img.putpixel((i,j),(i,j,128)) for i in range(200) for j in range(200)]; img.save('test.png')"

# Convert it
ascii-cinema image test.png --width 80 --color
```

## Complete File List

After running the commands, you should have:

```
ascii-cinema/
├── ascii_cinema/
│   ├── __init__.py          (populated with content)
│   ├── __main__.py          (populated with content)
│   ├── converter.py         (populated with content)
│   ├── player.py            (populated with content)
│   └── styles.py            (populated with content)
├── tests/
│   ├── __init__.py          (empty or with test config)
│   └── test_ascii_cinema.py (populated with content)
├── pyproject.toml           (populated with content)
├── requirements.txt         (populated with content)
├── requirements-dev.txt     (populated with content)
├── README.md                (populated with content)
├── SETUP.md                 (populated with content)
├── PROJECT_SUMMARY.md       (populated with content)
├── LICENSE                  (populated with content)
├── Makefile                 (populated with content)
└── .gitignore              (populated with content)
```

## Quick Start After Setup

```bash
# Format code
make format

# Run linter
make lint

# Type check
make type-check

# Run tests
make test

# Do everything
make all
```

## Troubleshooting

If `ascii-cinema` command not found:
```bash
pip install -e .
```

If tests fail:
```bash
pip install -e ".[dev,video]"
```

If you need to start over:
```bash
cd ..
rm -rf ascii-cinema
# Then run the setup commands again
```
