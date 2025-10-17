# 🎬 ASCII Cinema

Convert images and videos into beautiful ASCII art animations right in your terminal!

![Tests](https://github.com/bedwards/ascii-cinema/actions/workflows/test.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![codecov](https://codecov.io/gh/bedwards/ascii-cinema/branch/main/graph/badge.svg)

## ✨ Features

- 🖼️ **Image to ASCII**: Convert any image to ASCII art
- 🎥 **Video/GIF Playback**: Watch videos and GIFs as ASCII animations
- 📹 **Webcam Support**: Real-time ASCII art from your webcam
- 🎨 **Multiple Styles**: Choose from various ASCII character sets
- 🌈 **Color Support**: Full 24-bit color ASCII output
- ⚡ **Fast**: Optimized with NumPy for smooth playback
- 🎯 **Easy CLI**: Simple and intuitive command-line interface

## 🚀 Installation

### Basic Installation

```bash
# Clone the repository
git clone https://github.com/ascii-cinema/ascii-cinema.git
cd ascii-cinema

# Install with pip
pip install -e .
```

### With Video Support

For video and webcam features, install with optional dependencies:

```bash
pip install -e ".[video]"
```

### Development Installation

```bash
pip install -e ".[dev,video]"
```

## 📖 Usage

### Convert an Image

```bash
# Basic usage
ascii-cinema image path/to/image.jpg

# With custom width
ascii-cinema image image.jpg --width 120

# With color output
ascii-cinema image image.jpg --color

# Save to file
ascii-cinema image image.jpg --output art.txt

# Different styles
ascii-cinema image image.jpg --style blocks
ascii-cinema image image.jpg --style simple
```

### Play a Video or GIF

```bash
# Play a GIF
ascii-cinema video animation.gif

# Play a video (requires opencv-python)
ascii-cinema video movie.mp4

# Custom settings
ascii-cinema video movie.mp4 --width 100 --fps 30 --no-loop --color
```

### Webcam ASCII Art

```bash
# Stream from webcam (requires opencv-python)
ascii-cinema webcam

# With custom settings
ascii-cinema webcam --width 100 --style simple --color
```

## 🎨 ASCII Styles

ASCII Cinema supports multiple character set styles:

- **simple**: ` .:-=+*#%@` - Clean and minimal
- **standard**: Extended character set for detailed images
- **detailed**: Full character range for maximum detail
- **blocks**: ` ░▒▓█` - Block characters for a pixelated look
- **binary**: ` █` - Pure black and white
- **minimal**: ` .:-=#` - Very simple 6-character set

Example:
```bash
ascii-cinema image photo.jpg --style blocks --width 80
```

## 🛠️ Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ascii_cinema --cov-report=html

# Run specific test file
pytest tests/test_converter.py
```

### Code Quality

```bash
# Format code
black ascii_cinema tests

# Lint code
ruff check ascii_cinema tests

# Type checking
mypy ascii_cinema
```

### Project Structure

```
ascii-cinema/
├── ascii_cinema/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # CLI entry point
│   ├── converter.py         # Image/video to ASCII conversion
│   ├── player.py            # Video playback engine
│   └── styles.py            # ASCII character sets
├── tests/
│   └── test_*.py            # Comprehensive test suite
├── pyproject.toml           # Project configuration
├── README.md                # This file
└── requirements.txt         # Dependencies
```

## 📊 Code Coverage

The project maintains high test coverage:

```bash
pytest --cov=ascii_cinema --cov-report=term-missing
```

Current coverage: **~95%**

## 🎯 Requirements

- Python 3.11 or higher
- Core dependencies:
  - typer >= 0.12.0
  - rich >= 13.7.0
  - Pillow >= 10.3.0
  - numpy >= 1.26.0

- Optional (for video/webcam):
  - opencv-python >= 4.9.0

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🌟 Examples

### Basic Image Conversion

```bash
# Convert a photo to ASCII art
ascii-cinema image vacation.jpg --width 120 --color
```

### Animated GIF

```bash
# Play a GIF with color
ascii-cinema video cat.gif --width 80 --color --loop
```

### Live Webcam

```bash
# See yourself in ASCII!
ascii-cinema webcam --style blocks --color
```

## 💡 Tips

1. **Terminal Size**: Larger terminal windows allow for bigger, more detailed ASCII art
2. **Font**: Monospace fonts work best. Try "Menlo" or "Monaco" on macOS
3. **Performance**: Use simpler styles (like `simple` or `minimal`) for smoother video playback
4. **Colors**: Use `--color` flag for images with lots of colors, but it may be slower
5. **Width**: Experiment with different widths (40-150) to find the best look

## 🐛 Troubleshooting

### Video playback not working?

Make sure you have opencv-python installed:
```bash
pip install opencv-python
```

### Colors not showing?

Ensure your terminal supports 24-bit color (most modern terminals do).

### Performance issues?

- Try a simpler style: `--style simple`
- Reduce width: `--width 60`
- Lower FPS: `--fps 15`

## 📚 API Usage

You can also use ASCII Cinema as a library:

```python
from ascii_cinema import ASCIIConverter, ASCIIStyle
from pathlib import Path

# Create converter
converter = ASCIIConverter(width=100, style=ASCIIStyle.STANDARD)

# Convert image
ascii_art = converter.image_to_ascii(Path("image.jpg"), use_color=False)
print(ascii_art)
```

## 🎉 Fun Ideas

- Create ASCII art wallpapers
- Make terminal screensavers
- Convert your favorite movie scenes
- Create ASCII art GIFs for GitHub
- Live stream your webcam as ASCII on video calls!

---

Made with ❤️ for the terminal enthusiasts
