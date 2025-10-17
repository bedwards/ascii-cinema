"""
Core conversion logic for ASCII Cinema
"""
from pathlib import Path
from typing import Tuple

import numpy as np
from PIL import Image

from ascii_cinema.styles import ASCIIStyle


class ASCIIConverter:
    """Converts images to ASCII art."""

    def __init__(
        self, width: int = 100, style: ASCIIStyle = ASCIIStyle.STANDARD, invert: bool = False
    ):
        """
        Initialize the converter.

        Args:
            width: Target width in characters
            style: ASCII character style to use
            invert: Whether to invert brightness mapping
        """
        self.width = width
        self.style = style
        self.invert = invert
        self.chars = self._get_chars()

    def _get_chars(self) -> str:
        """Get the character set for the selected style."""
        chars = self.style.value
        return chars[::-1] if self.invert else chars

    def image_to_ascii(self, image_path: Path, use_color: bool = False) -> str:
        """
        Convert an image to ASCII art.

        Args:
            image_path: Path to the image file
            use_color: Whether to use ANSI color codes

        Returns:
            ASCII art string
        """
        img = Image.open(image_path)
        return self._convert_image(img, use_color)

    def _convert_image(self, img: Image.Image, use_color: bool = False) -> str:
        """
        Convert a PIL Image to ASCII art.

        Args:
            img: PIL Image object
            use_color: Whether to use ANSI color codes

        Returns:
            ASCII art string
        """
        # Calculate height maintaining aspect ratio
        aspect_ratio = img.height / img.width
        height = int(self.width * aspect_ratio * 0.55)  # 0.55 to account for char height

        # Resize image
        img = img.resize((self.width, height))

        # Convert to RGB if needed
        if img.mode != "RGB":
            img = img.convert("RGB")

        # Convert to numpy array for faster processing
        pixels = np.array(img)

        # Convert to grayscale for brightness calculation
        gray = np.dot(pixels[..., :3], [0.299, 0.587, 0.114])

        # Normalize to character range
        normalized = (gray / 255 * (len(self.chars) - 1)).astype(int)

        lines = []
        for row_idx in range(height):
            line_chars = []
            for col_idx in range(self.width):
                char = self.chars[normalized[row_idx, col_idx]]

                if use_color:
                    r, g, b = pixels[row_idx, col_idx][:3]
                    # Use ANSI 24-bit color
                    line_chars.append(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
                else:
                    line_chars.append(char)

            lines.append("".join(line_chars))

        return "\n".join(lines)

    def video_frame_to_ascii(self, frame: np.ndarray, use_color: bool = False) -> str:
        """
        Convert a video frame (numpy array) to ASCII art.

        Args:
            frame: Video frame as numpy array (BGR format)
            use_color: Whether to use ANSI color codes

        Returns:
            ASCII art string
        """
        # Convert BGR to RGB
        frame_rgb = frame[:, :, ::-1]
        img = Image.fromarray(frame_rgb)
        return self._convert_image(img, use_color)

    def resize_for_terminal(
        self, img: Image.Image, terminal_width: int, terminal_height: int
    ) -> Tuple[int, int]:
        """
        Calculate optimal dimensions for terminal display.

        Args:
            img: PIL Image object
            terminal_width: Terminal width in characters
            terminal_height: Terminal height in lines

        Returns:
            Tuple of (width, height) in characters
        """
        img_aspect = img.width / img.height
        term_aspect = terminal_width / (terminal_height * 0.55)

        if img_aspect > term_aspect:
            # Image is wider, fit to width
            width = min(self.width, terminal_width - 2)
            height = int(width / img_aspect * 0.55)
        else:
            # Image is taller, fit to height
            height = min(int(self.width / img_aspect * 0.55), terminal_height - 2)
            width = int(height * img_aspect / 0.55)

        return width, height
