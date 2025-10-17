"""
ASCII art styles and character sets
"""
from enum import Enum


class ASCIIStyle(str, Enum):
    """Available ASCII art styles with different character sets."""

    SIMPLE = " .:-=+*#%@"
    STANDARD = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    DETAILED = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    BLOCKS = " ░▒▓█"
    BINARY = " █"
    MINIMAL = " .:-=#"

    def __str__(self) -> str:
        """Return the enum name for CLI display."""
        return self.name.lower()
