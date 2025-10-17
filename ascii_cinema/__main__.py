"""
ASCII Cinema - Convert images and videos to ASCII art
"""
import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from ascii_cinema.converter import ASCIIConverter
from ascii_cinema.player import ASCIIPlayer
from ascii_cinema.styles import ASCIIStyle

app = typer.Typer(
    name="ascii-cinema",
    help="Convert images and videos to beautiful ASCII art animations",
    add_completion=False,
)
console = Console()


@app.command()
def image(
    path: Path = typer.Argument(..., help="Path to the image file"),
    width: int = typer.Option(100, "--width", "-w", help="Width in characters"),
    style: ASCIIStyle = typer.Option(
        ASCIIStyle.DETAILED, "--style", "-s", help="ASCII character style"
    ),
    color: bool = typer.Option(False, "--color", "-c", help="Use colored output"),
    invert: bool = typer.Option(False, "--invert", "-i", help="Invert brightness"),
    output: Optional[Path] = typer.Option(
        None, "--output", "-o", help="Save to file instead of displaying"
    ),
) -> None:
    """Convert an image to ASCII art."""
    if not path.exists():
        console.print(f"[red]Error: File not found: {path}[/red]")
        raise typer.Exit(1)

    try:
        converter = ASCIIConverter(width=width, style=style, invert=invert)
        ascii_art = converter.image_to_ascii(path, use_color=color)

        if output:
            output.write_text(ascii_art)
            console.print(f"[green]✓[/green] Saved to {output}")
        else:
            console.print(ascii_art)

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def video(
    path: Path = typer.Argument(..., help="Path to the video/GIF file"),
    width: int = typer.Option(80, "--width", "-w", help="Width in characters"),
    style: ASCIIStyle = typer.Option(
        ASCIIStyle.STANDARD, "--style", "-s", help="ASCII character style"
    ),
    color: bool = typer.Option(True, "--color/--no-color", help="Use colored output"),
    invert: bool = typer.Option(False, "--invert", "-i", help="Invert brightness"),
    fps: Optional[float] = typer.Option(None, "--fps", "-f", help="Frames per second"),
    loop: bool = typer.Option(True, "--loop/--no-loop", help="Loop the animation"),
) -> None:
    """Play a video or GIF as ASCII art animation."""
    if not path.exists():
        console.print(f"[red]Error: File not found: {path}[/red]")
        raise typer.Exit(1)

    try:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Loading video...", total=None)
            
            converter = ASCIIConverter(width=width, style=style, invert=invert)
            player = ASCIIPlayer(converter, console)
            
            progress.update(task, description="Converting frames...")
            player.play_video(path, use_color=color, target_fps=fps, loop=loop)

    except KeyboardInterrupt:
        console.print("\n[yellow]Playback stopped[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


@app.command()
def webcam(
    width: int = typer.Option(80, "--width", "-w", help="Width in characters"),
    style: ASCIIStyle = typer.Option(
        ASCIIStyle.SIMPLE, "--style", "-s", help="ASCII character style"
    ),
    color: bool = typer.Option(True, "--color/--no-color", help="Use colored output"),
    invert: bool = typer.Option(False, "--invert", "-i", help="Invert brightness"),
) -> None:
    """Stream ASCII art from your webcam (requires opencv-python)."""
    try:
        import cv2
    except ImportError:
        console.print(
            "[red]Error: opencv-python is required for webcam support[/red]\n"
            "Install it with: pip install opencv-python"
        )
        raise typer.Exit(1)

    try:
        converter = ASCIIConverter(width=width, style=style, invert=invert)
        player = ASCIIPlayer(converter, console)
        
        console.print("[cyan]Starting webcam... Press Ctrl+C to stop[/cyan]\n")
        player.play_webcam(use_color=color)

    except KeyboardInterrupt:
        console.print("\n[yellow]Webcam stopped[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)


def main() -> None:
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
