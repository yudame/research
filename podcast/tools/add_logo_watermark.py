#!/usr/bin/env python3
"""
Add podcast logo watermark to episode cover art.

Usage:
    python add_logo_watermark.py <cover_image> [--logo path/to/logo.png]

Requirements:
    pip install pillow
"""

import sys
import argparse
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Error: pillow package not installed. Run: pip install pillow")
    sys.exit(1)


def add_watermark(cover_path, logo_path, position='bottom-right', opacity=0.9, size_ratio=0.15):
    """
    Add logo watermark to cover image.

    Args:
        cover_path: Path to the cover image
        logo_path: Path to the logo image
        position: 'bottom-right', 'bottom-left', 'top-right', 'top-left', 'center'
        opacity: Logo opacity (0.0 to 1.0)
        size_ratio: Logo size as ratio of cover width (0.1 to 0.3)
    """
    cover_path = Path(cover_path)
    logo_path = Path(logo_path)

    if not cover_path.exists():
        print(f"Error: Cover image not found: {cover_path}")
        sys.exit(1)

    if not logo_path.exists():
        print(f"Error: Logo not found: {logo_path}")
        sys.exit(1)

    print(f"Loading cover: {cover_path}")
    print(f"Loading logo: {logo_path}")

    # Load images
    cover = Image.open(cover_path).convert('RGBA')
    logo = Image.open(logo_path).convert('RGBA')

    # Calculate logo size (as percentage of cover width)
    logo_width = int(cover.width * size_ratio)
    aspect_ratio = logo.height / logo.width
    logo_height = int(logo_width * aspect_ratio)

    # Resize logo
    logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)

    # Apply opacity
    if opacity < 1.0:
        alpha = logo.split()[3]
        alpha = alpha.point(lambda p: int(p * opacity))
        logo.putalpha(alpha)

    # Calculate position with padding
    padding = int(cover.width * 0.05)  # 5% padding

    positions = {
        'bottom-right': (cover.width - logo_width - padding, cover.height - logo_height - padding),
        'bottom-left': (padding, cover.height - logo_height - padding),
        'top-right': (cover.width - logo_width - padding, padding),
        'top-left': (padding, padding),
        'center': ((cover.width - logo_width) // 2, (cover.height - logo_height) // 2),
    }

    pos = positions.get(position, positions['bottom-right'])

    # Create a transparent layer for the logo
    watermark_layer = Image.new('RGBA', cover.size, (0, 0, 0, 0))
    watermark_layer.paste(logo, pos, logo)

    # Composite the watermark onto the cover
    watermarked = Image.alpha_composite(cover, watermark_layer)

    # Save back to original path
    output_path = cover_path.parent / f"{cover_path.stem}_watermarked{cover_path.suffix}"
    watermarked.convert('RGB').save(output_path, 'PNG', quality=95)

    print(f"✓ Watermarked cover saved to: {output_path}")

    # Replace original
    cover_path.unlink()
    output_path.rename(cover_path)
    print(f"✓ Original replaced: {cover_path}")

    return cover_path


def main():
    parser = argparse.ArgumentParser(description="Add logo watermark to episode cover art")
    parser.add_argument("cover", help="Path to cover image")
    parser.add_argument("--logo", help="Path to logo (default: ../cover.png)")
    parser.add_argument("--position", default="bottom-right",
                       choices=['bottom-right', 'bottom-left', 'top-right', 'top-left', 'center'],
                       help="Logo position (default: bottom-right)")
    parser.add_argument("--opacity", type=float, default=0.9,
                       help="Logo opacity 0.0-1.0 (default: 0.9)")
    parser.add_argument("--size", type=float, default=0.15,
                       help="Logo size ratio 0.1-0.3 (default: 0.15)")

    args = parser.parse_args()

    # Default logo path
    if not args.logo:
        script_dir = Path(__file__).parent
        args.logo = script_dir.parent / "cover.png"

    add_watermark(
        args.cover,
        args.logo,
        position=args.position,
        opacity=args.opacity,
        size_ratio=args.size
    )

    print("\nDone! Logo watermark applied.")


if __name__ == "__main__":
    main()
