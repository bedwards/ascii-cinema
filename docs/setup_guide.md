# ASCII Cinema - Setup Guide

Complete setup instructions for getting ASCII Cinema running on your Mac.

## Prerequisites

- macOS 10.15 or later
- Python 3.11 or 3.12 (recommended: 3.12)
- pip package manager
- Terminal app

## Step-by-Step Installation

### 1. Check Python Version

```bash
python3 --version
```

You should see Python 3.11 or higher. If not, install Python:

```bash
# Using Homebrew
brew install python@3.12
```

### 2. Create Project Directory

```bash
mkdir -p ~/projects/ascii-cinema
cd ~/projects/ascii-cinema
```

### 3. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip
```

### 4. Set Up Project Structure

Create the following directory structure:

```
ascii-cinema/
├── ascii_cinema/
│   ├── __init__.py
│   ├── __main__.py
│   ├── converter.py
│   ├── player.py
│   └── styles.py
├── tests/
│   └── test_ascii_cinema.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── README.md
├── Makefile
├── .gitignore
└── LICENSE
```

Copy all the provided files into their respective locations.

### 5. Install Dependencies

```bash
# Install core dependencies
pip install -r requirements.txt

# Or install in development mode with all dependencies
pip install -e ".[dev,video]"
```

### 6. Verify Installation

```bash
# Check if the command is available
ascii-cinema --help

# Should show:
# Usage: ascii-cinema [OPTIONS] COMMAND [ARGS]...
```

## Running Tests

### Run All Tests

```bash
# Simple test run
pytest

# With verbose output
pytest -v

# With coverage report
pytest --cov=ascii_cinema --cov-report=term-missing
```

### Run Specific Tests

```bash
# Test only the converter
pytest tests/test_ascii_cinema.py::TestASCIIConverter -v

# Test with coverage for specific module
pytest tests/test_ascii_cinema.py::TestASCIIConverter --cov=ascii_cinema.converter
```

## Quick Start Examples

### 1. Test with a Simple Image

Create a test image:

```python
from PIL import Image

# Create a simple gradient test image
img = Image.new('RGB', (200, 200))
for i in range(200):
    for j in range(200):
        img.putpixel((i, j), (i, j, 128))
img.save('test_gradient.png')
```

Then convert it:

```bash
ascii-cinema image test_gradient.png --width 80
```

### 2. Try Different Styles

```bash
# Simple style
ascii-cinema image test_gradient.png --style simple

# Block style
ascii-cinema image test_gradient.png --style blocks

# With color
ascii-cinema image test_gradient.png --style standard --color
```

### 3. Download and Play a GIF

```bash
# Download a test GIF (or use your own)
curl -o test.gif "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif"

# Play it
ascii-cinema video test.gif --width 60 --color
```

## Development Workflow

### 1. Format Code

```bash
# Using make
make format

# Or directly
black ascii_cinema tests
```

### 2. Run Linter

```bash
# Using make
make lint

# Or directly
ruff check ascii_cinema tests
```

### 3. Type Checking

```bash
# Using make
make type-check

# Or directly
mypy ascii_cinema
```

### 4. Run All Checks

```bash
# Format, lint, type-check, and test
make all
```

## Troubleshooting

### ImportError: No module named 'ascii_cinema'

**Solution**: Install the package in editable mode:
```bash
pip install -e .
```

### opencv-python installation fails

**Solution**: Try installing with Homebrew first:
```bash
brew install opencv
pip install opencv-python
```

### Tests fail with "ModuleNotFoundError"

**Solution**: Make sure you're in the virtual environment:
```bash
source venv/bin/activate
pip install -e ".[dev,video]"
```

### ASCII art looks stretched

**Solution**: Try different terminal fonts (Menlo, Monaco) or adjust the width parameter.

### Colors not showing

**Solution**: 
1. Check if your terminal supports 24-bit color
2. Try iTerm2 or the latest macOS Terminal
3. Test with: `echo -e "\033[38;2;255;0;0mRed Text\033[0m"`

## Performance Tips

### For Smooth Video Playback

```bash
# Use simpler style
ascii-cinema video animation.gif --style simple --width 60

# Reduce FPS
ascii-cinema video animation.gif --fps 15

# No color for faster rendering
ascii-cinema video animation.gif --no-color
```

### For Large Images

```bash
# Limit width
ascii-cinema image large_photo.jpg --width 100

# Save to file instead of displaying
ascii-cinema image large_photo.jpg --output art.txt
```

## Uninstall

```bash
# Deactivate virtual environment
deactivate

# Remove the project directory
cd ..
rm -rf ascii-cinema

# Or just uninstall the package
pip uninstall ascii-cinema
```

## Next Steps

1. **Explore Different Images**: Try converting various types of images
2. **Create Animations**: Convert your favorite GIFs
3. **Customize**: Modify the character sets in `styles.py`
4. **Contribute**: Add new features or styles
5. **Share**: Show off your ASCII creations!

## Getting Help

- Check the [README.md](README.md) for usage examples
- Run `ascii-cinema --help` for command options
- Run `ascii-cinema COMMAND --help` for command-specific help

## Resources

- Python Documentation: https://docs.python.org/3/
- Typer Documentation: https://typer.tiangolo.com/
- Rich Documentation: https://rich.readthedocs.io/
- PIL/Pillow Documentation: https://pillow.readthedocs.io/

---

Happy ASCII art creating! 🎨
