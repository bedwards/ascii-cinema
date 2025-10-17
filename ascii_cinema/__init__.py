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
