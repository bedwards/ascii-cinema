"""
Unit tests for ASCII Cinema
"""
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

import numpy as np
import pytest
from PIL import Image

from ascii_cinema.converter import ASCIIConverter
from ascii_cinema.player import ASCIIPlayer
from ascii_cinema.styles import ASCIIStyle


class TestASCIIConverter:
    """Test suite for ASCIIConverter class."""

    def test_init_default_values(self):
        """Test converter initialization with default values."""
        converter = ASCIIConverter()
        assert converter.width == 100
        assert converter.style == ASCIIStyle.STANDARD
        assert not converter.invert

    def test_init_custom_values(self):
        """Test converter initialization with custom values."""
        converter = ASCIIConverter(width=50, style=ASCIIStyle.SIMPLE, invert=True)
        assert converter.width == 50
        assert converter.style == ASCIIStyle.SIMPLE
        assert converter.invert

    def test_get_chars_normal(self):
        """Test character retrieval without inversion."""
        converter = ASCIIConverter(style=ASCIIStyle.SIMPLE, invert=False)
        chars = converter._get_chars()
        assert chars == ASCIIStyle.SIMPLE.value

    def test_get_chars_inverted(self):
        """Test character retrieval with inversion."""
        converter = ASCIIConverter(style=ASCIIStyle.SIMPLE, invert=True)
        chars = converter._get_chars()
        assert chars == ASCIIStyle.SIMPLE.value[::-1]

    def test_convert_image_grayscale(self):
        """Test converting a grayscale image to ASCII."""
        # Create a simple test image
        img = Image.new("L", (10, 10), color=128)
        converter = ASCIIConverter(width=10, style=ASCIIStyle.SIMPLE)
        result = converter._convert_image(img, use_color=False)

        # Check result is a string
        assert isinstance(result, str)
        # Check it has multiple lines
        assert "\n" in result
        # Check it only contains ASCII characters
        assert all(c in (ASCIIStyle.SIMPLE.value + "\n") for c in result)

    def test_convert_image_rgb(self):
        """Test converting an RGB image to ASCII."""
        img = Image.new("RGB", (10, 10), color=(255, 0, 0))
        converter = ASCIIConverter(width=10, style=ASCIIStyle.SIMPLE)
        result = converter._convert_image(img, use_color=False)

        assert isinstance(result, str)
        assert "\n" in result

    def test_convert_image_with_color(self):
        """Test converting an image to colored ASCII."""
        img = Image.new("RGB", (5, 5), color=(255, 0, 0))
        converter = ASCIIConverter(width=5, style=ASCIIStyle.SIMPLE)
        result = converter._convert_image(img, use_color=True)

        assert isinstance(result, str)
        # Check for ANSI color codes
        assert "\033[" in result

    def test_image_to_ascii_with_file(self):
        """Test converting an image file to ASCII."""
        converter = ASCIIConverter(width=20, style=ASCIIStyle.SIMPLE)

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            img = Image.new("RGB", (50, 50), color=(100, 150, 200))
            img.save(tmp.name)
            tmp_path = Path(tmp.name)

            try:
                result = converter.image_to_ascii(tmp_path, use_color=False)
                assert isinstance(result, str)
                assert len(result) > 0
            finally:
                tmp_path.unlink()

    def test_video_frame_to_ascii(self):
        """Test converting a video frame (numpy array) to ASCII."""
        # Create a test frame (BGR format like OpenCV)
        frame = np.random.randint(0, 255, (50, 50, 3), dtype=np.uint8)
        converter = ASCIIConverter(width=20, style=ASCIIStyle.SIMPLE)
        result = converter.video_frame_to_ascii(frame, use_color=False)

        assert isinstance(result, str)
        assert len(result) > 0

    def test_resize_for_terminal_wide_image(self):
        """Test terminal resize calculation for wide image."""
        img = Image.new("RGB", (200, 100))
        converter = ASCIIConverter(width=100)
        width, height = converter.resize_for_terminal(img, 120, 40)

        assert width <= 118  # terminal_width - 2
        assert height <= 38  # terminal_height - 2
        assert width > 0
        assert height > 0

    def test_resize_for_terminal_tall_image(self):
        """Test terminal resize calculation for tall image."""
        img = Image.new("RGB", (100, 200))
        converter = ASCIIConverter(width=100)
        width, height = converter.resize_for_terminal(img, 120, 40)

        assert width <= 118
        assert height <= 38
        assert width > 0
        assert height > 0

    def test_different_styles(self):
        """Test that different styles produce different output."""
        img = Image.new("L", (10, 10), color=128)
        
        simple = ASCIIConverter(width=10, style=ASCIIStyle.SIMPLE)
        blocks = ASCIIConverter(width=10, style=ASCIIStyle.BLOCKS)
        
        simple_result = simple._convert_image(img, use_color=False)
        blocks_result = blocks._convert_image(img, use_color=False)

        # Results should be different as they use different character sets
        assert simple_result != blocks_result


class TestASCIIPlayer:
    """Test suite for ASCIIPlayer class."""

    def test_init(self):
        """Test player initialization."""
        converter = ASCIIConverter()
        console = Mock()
        player = ASCIIPlayer(converter, console)

        assert player.converter == converter
        assert player.console == console

    def test_play_gif(self):
        """Test playing a GIF file."""
        converter = ASCIIConverter(width=20, style=ASCIIStyle.SIMPLE)
        console = Mock()
        player = ASCIIPlayer(converter, console)

        # Create a simple test GIF
        with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as tmp:
            img1 = Image.new("RGB", (10, 10), color=(255, 0, 0))
            img2 = Image.new("RGB", (10, 10), color=(0, 255, 0))
            
            img1.save(
                tmp.name,
                save_all=True,
                append_images=[img2],
                duration=100,
                loop=0,
            )
            tmp_path = Path(tmp.name)

            try:
                with patch("ascii_cinema.player.Live") as mock_live:
                    with patch("time.sleep"):
                        # Stop after first iteration
                        mock_live.return_value.__enter__ = Mock(
                            side_effect=KeyboardInterrupt
                        )
                        
                        with pytest.raises(KeyboardInterrupt):
                            player._play_gif(tmp_path, use_color=False, loop=False)

            finally:
                tmp_path.unlink()

    def test_play_gif_with_color(self):
        """Test playing a GIF with color."""
        converter = ASCIIConverter(width=10, style=ASCIIStyle.SIMPLE)
        console = Mock()
        player = ASCIIPlayer(converter, console)

        with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as tmp:
            img = Image.new("RGB", (10, 10), color=(255, 0, 0))
            img.save(tmp.name)
            tmp_path = Path(tmp.name)

            try:
                with patch("ascii_cinema.player.Live") as mock_live:
                    with patch("time.sleep"):
                        mock_live.return_value.__enter__ = Mock(
                            side_effect=KeyboardInterrupt
                        )
                        
                        with pytest.raises(KeyboardInterrupt):
                            player._play_gif(tmp_path, use_color=True, loop=False)

            finally:
                tmp_path.unlink()

    def test_play_gif_custom_fps(self):
        """Test playing a GIF with custom FPS."""
        converter = ASCIIConverter(width=10)
        console = Mock()
        player = ASCIIPlayer(converter, console)

        with tempfile.NamedTemporaryFile(suffix=".gif", delete=False) as tmp:
            img = Image.new("RGB", (10, 10), color=(255, 0, 0))
            img.save(tmp.name)
            tmp_path = Path(tmp.name)

            try:
                with patch("ascii_cinema.player.Live"):
                    with patch("time.sleep") as mock_sleep:
                        mock_sleep.side_effect = KeyboardInterrupt
                        
                        with pytest.raises(KeyboardInterrupt):
                            player._play_gif(tmp_path, target_fps=30.0, loop=False)

            finally:
                tmp_path.unlink()

    def test_play_video_opencv_not_installed(self):
        """Test that proper error is raised when OpenCV is not installed."""
        converter = ASCIIConverter()
        console = Mock()
        player = ASCIIPlayer(converter, console)

        with patch.dict("sys.modules", {"cv2": None}):
            with pytest.raises(ImportError, match="opencv-python is required"):
                player._play_video_file(
                    Path("test.mp4"), use_color=False, loop=False
                )

    def test_webcam_opencv_not_installed(self):
        """Test that proper error is raised for webcam when OpenCV not installed."""
        converter = ASCIIConverter()
        console = Mock()
        player = ASCIIPlayer(converter, console)

        with patch.dict("sys.modules", {"cv2": None}):
            with pytest.raises(ImportError, match="opencv-python is required"):
                player.play_webcam(use_color=False)


class TestASCIIStyle:
    """Test suite for ASCIIStyle enum."""

    def test_all_styles_have_values(self):
        """Test that all styles have character values."""
        for style in ASCIIStyle:
            assert isinstance(style.value, str)
            assert len(style.value) > 0

    def test_style_str_representation(self):
        """Test string representation of styles."""
        assert str(ASCIIStyle.SIMPLE) == "simple"
        assert str(ASCIIStyle.STANDARD) == "standard"
        assert str(ASCIIStyle.BLOCKS) == "blocks"

    def test_styles_are_different(self):
        """Test that different styles have different character sets."""
        styles_values = [style.value for style in ASCIIStyle]
        assert len(styles_values) == len(set(styles_values))

    def test_simple_style_progression(self):
        """Test that simple style goes from light to dark."""
        chars = ASCIIStyle.SIMPLE.value
        # First char should be space (lightest)
        assert chars[0] == " "
        # Last char should be densest
        assert chars[-1] in ["@", "$", "#"]


class TestIntegration:
    """Integration tests for the complete workflow."""

    def test_image_to_ascii_full_workflow(self):
        """Test complete workflow from image to ASCII."""
        # Create test image
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            img = Image.new("RGB", (100, 100))
            # Add some variation
            for i in range(100):
                for j in range(100):
                    img.putpixel((i, j), (i * 2, j * 2, 128))
            img.save(tmp.name)
            tmp_path = Path(tmp.name)

            try:
                converter = ASCIIConverter(width=50, style=ASCIIStyle.STANDARD)
                result = converter.image_to_ascii(tmp_path, use_color=False)

                # Verify output
                assert isinstance(result, str)
                assert len(result) > 0
                lines = result.split("\n")
                assert len(lines) > 0
                # Each line should have approximately the target width
                assert all(len(line) >= 45 for line in lines if line)

            finally:
                tmp_path.unlink()

    def test_colored_ascii_output(self):
        """Test that colored ASCII contains ANSI codes."""
        img = Image.new("RGB", (20, 20), color=(255, 100, 50))
        converter = ASCIIConverter(width=20, style=ASCIIStyle.SIMPLE)
        result = converter._convert_image(img, use_color=True)

        # Should contain ANSI color escape sequences
        assert "\033[38;2;" in result
        assert "\033[0m" in result
