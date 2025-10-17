"""
Video and animation playback for ASCII Cinema
"""
import time
from pathlib import Path
from typing import Optional

from PIL import Image
from rich.console import Console
from rich.live import Live

from ascii_cinema.converter import ASCIIConverter


class ASCIIPlayer:
    """Plays ASCII art animations."""

    def __init__(self, converter: ASCIIConverter, console: Console):
        """
        Initialize the player.

        Args:
            converter: ASCIIConverter instance
            console: Rich Console instance
        """
        self.converter = converter
        self.console = console

    def play_video(
        self,
        video_path: Path,
        use_color: bool = False,
        target_fps: Optional[float] = None,
        loop: bool = True,
    ) -> None:
        """
        Play a video or GIF as ASCII animation.

        Args:
            video_path: Path to video/GIF file
            use_color: Whether to use colored output
            target_fps: Target frames per second (None = source fps)
            loop: Whether to loop the animation
        """
        # Check if it's a GIF
        if video_path.suffix.lower() in [".gif"]:
            self._play_gif(video_path, use_color, target_fps, loop)
        else:
            self._play_video_file(video_path, use_color, target_fps, loop)

    def _play_gif(
        self,
        gif_path: Path,
        use_color: bool = False,
        target_fps: Optional[float] = None,
        loop: bool = True,
    ) -> None:
        """Play a GIF file as ASCII animation."""
        img = Image.open(gif_path)
        
        # Get frame duration in milliseconds
        try:
            duration = img.info.get("duration", 100)  # Default 100ms
            source_fps = 1000.0 / duration
        except (KeyError, ZeroDivisionError):
            source_fps = 10.0

        fps = target_fps if target_fps else source_fps
        frame_delay = 1.0 / fps

        frames = []
        try:
            while True:
                # Convert current frame
                frame_copy = img.copy().convert("RGB")
                ascii_frame = self.converter._convert_image(frame_copy, use_color)
                frames.append(ascii_frame)
                
                img.seek(img.tell() + 1)
        except EOFError:
            pass  # End of GIF

        if not frames:
            raise ValueError("No frames found in GIF")

        # Play the animation
        with Live(frames[0], console=self.console, refresh_per_second=fps) as live:
            while True:
                for frame in frames:
                    live.update(frame)
                    time.sleep(frame_delay)
                
                if not loop:
                    break

    def _play_video_file(
        self,
        video_path: Path,
        use_color: bool = False,
        target_fps: Optional[float] = None,
        loop: bool = True,
    ) -> None:
        """Play a video file as ASCII animation (requires opencv-python)."""
        try:
            import cv2
        except ImportError:
            raise ImportError(
                "opencv-python is required for video playback. "
                "Install it with: pip install opencv-python"
            )

        cap = cv2.VideoCapture(str(video_path))
        
        if not cap.isOpened():
            raise ValueError(f"Could not open video file: {video_path}")

        # Get video properties
        source_fps = cap.get(cv2.CAP_PROP_FPS)
        fps = target_fps if target_fps else source_fps
        frame_delay = 1.0 / fps

        try:
            # Pre-load frames for smooth playback
            frames = []
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                ascii_frame = self.converter.video_frame_to_ascii(frame, use_color)
                frames.append(ascii_frame)

            if not frames:
                raise ValueError("No frames found in video")

            # Play the animation
            with Live(frames[0], console=self.console, refresh_per_second=fps) as live:
                while True:
                    for frame in frames:
                        live.update(frame)
                        time.sleep(frame_delay)
                    
                    if not loop:
                        break

        finally:
            cap.release()

    def play_webcam(self, use_color: bool = False, fps: float = 15.0) -> None:
        """
        Stream ASCII art from webcam.

        Args:
            use_color: Whether to use colored output
            fps: Target frames per second
        """
        try:
            import cv2
        except ImportError:
            raise ImportError(
                "opencv-python is required for webcam support. "
                "Install it with: pip install opencv-python"
            )

        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            raise ValueError("Could not open webcam")

        frame_delay = 1.0 / fps

        try:
            # Get first frame for initialization
            ret, frame = cap.read()
            if not ret:
                raise ValueError("Could not read from webcam")

            ascii_frame = self.converter.video_frame_to_ascii(frame, use_color)

            with Live(ascii_frame, console=self.console, refresh_per_second=fps) as live:
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    ascii_frame = self.converter.video_frame_to_ascii(frame, use_color)
                    live.update(ascii_frame)
                    time.sleep(frame_delay)

        finally:
            cap.release()
