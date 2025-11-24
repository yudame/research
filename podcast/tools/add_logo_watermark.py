#!/usr/bin/env python3
"""
Add podcast logo watermark and text overlays to episode cover art.

Usage:
    python add_logo_watermark.py <cover_image> \
        --series "Series Name" \
        --episode "Ep 3 - Topic" \
        [--logo path/to/logo.png]

Requirements:
    pip install pillow
"""

import sys
import argparse
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: pillow package not installed. Run: pip install pillow")
    sys.exit(1)


def add_watermark(cover_path, logo_path, position='top-left', opacity=0.9, size_ratio=0.12,
                  brand_text=None, series_text=None, episode_text=None, border_width=0, border_color='#FFC20E'):
    """
    Add logo watermark and text overlays to cover image.

    Args:
        cover_path: Path to the cover image
        logo_path: Path to the logo image
        position: 'bottom-right', 'bottom-left', 'top-right', 'top-left', 'center'
        opacity: Logo opacity (0.0 to 1.0)
        size_ratio: Logo size as ratio of cover width (0.1 to 0.3)
        brand_text: Podcast brand name (e.g., "Yudame Research") - appears next to logo
        series_text: Series name text (e.g., "Cardiovascular Health")
        episode_text: Episode info text (e.g., "Ep 3 - HRV")
        border_width: Width of border in pixels (0 = no border)
        border_color: Hex color for border (default: yellow from logo)
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

    # Add border if requested
    if border_width > 0:
        cover = add_border(cover, border_width, border_color)

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

    # Add text overlays if provided
    if brand_text or series_text or episode_text:
        watermarked = add_text_overlays(watermarked, brand_text, series_text, episode_text,
                                       logo_width, logo_height, pos, position)

    # Save back to original path
    output_path = cover_path.parent / f"{cover_path.stem}_watermarked{cover_path.suffix}"
    watermarked.convert('RGB').save(output_path, 'PNG', quality=95)

    print(f"✓ Watermarked cover saved to: {output_path}")

    # Replace original
    cover_path.unlink()
    output_path.rename(cover_path)
    print(f"✓ Original replaced: {cover_path}")

    return cover_path


def add_border(image, border_width, border_color='#FFC20E'):
    """
    Add a solid color border around the image.

    Args:
        image: PIL Image object
        border_width: Width of border in pixels
        border_color: Hex color string (e.g., '#FFC20E' for yellow)
    """
    # Convert hex color to RGB
    border_color = border_color.lstrip('#')
    r, g, b = tuple(int(border_color[i:i+2], 16) for i in (0, 2, 4))

    # Create new image with border
    new_width = image.width + (border_width * 2)
    new_height = image.height + (border_width * 2)
    bordered = Image.new('RGBA', (new_width, new_height), (r, g, b, 255))

    # Paste original image in center
    bordered.paste(image, (border_width, border_width), image)

    return bordered


def add_text_overlays(image, brand_text=None, series_text=None, episode_text=None,
                     logo_width=0, logo_height=0, logo_pos=(0, 0), logo_position='top-left'):
    """
    Add text overlays to the image.

    Args:
        image: PIL Image object
        brand_text: Podcast brand name (appears next to logo)
        series_text: Series name
        episode_text: Episode info
        logo_width: Width of logo for text positioning
        logo_height: Height of logo for text positioning
        logo_pos: (x, y) position of logo
        logo_position: Logo position string
    """
    # Convert to RGB for drawing
    img = image.convert('RGB')
    draw = ImageDraw.Draw(img)

    width, height = img.size
    padding = int(width * 0.05)

    # Try to load nice fonts, fall back to default
    try:
        # Try common macOS system fonts
        brand_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", int(width * 0.055))
        series_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", int(width * 0.05))
        episode_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", int(width * 0.065))
    except:
        try:
            brand_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", int(width * 0.055))
            series_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", int(width * 0.05))
            episode_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", int(width * 0.065))
        except:
            # Fallback to default
            brand_font = ImageFont.load_default()
            series_font = ImageFont.load_default()
            episode_font = ImageFont.load_default()

    # Start position based on logo location
    if logo_position == 'top-left':
        # Brand text goes to the right of logo
        brand_x = logo_pos[0] + logo_width + int(padding * 0.4)
        brand_y = logo_pos[1] + (logo_height // 2) - (int(width * 0.055) // 2)  # Center vertically with logo

        # Series/episode text starts below logo with margin
        content_y = logo_pos[1] + logo_height + int(padding * 0.8)
        content_x = padding
    else:
        # Default to top
        brand_x = padding
        brand_y = padding
        content_y = brand_y + int(width * 0.055) + int(padding * 0.5)
        content_x = padding

    # Draw brand text next to logo (if logo is top-left)
    if brand_text and logo_position == 'top-left':
        shadow_offset = 2
        draw.text((brand_x + shadow_offset, brand_y + shadow_offset),
                 brand_text, fill=(0, 0, 0, 180), font=brand_font)
        draw.text((brand_x, brand_y), brand_text, fill=(255, 255, 255, 255), font=brand_font)

    # Draw series text
    if series_text:
        bbox = draw.textbbox((0, 0), series_text, font=series_font)
        text_height = bbox[3] - bbox[1]

        shadow_offset = 2
        draw.text((content_x + shadow_offset, content_y + shadow_offset),
                 series_text, fill=(0, 0, 0, 180), font=series_font)
        draw.text((content_x, content_y), series_text, fill=(255, 255, 255, 255), font=series_font)

        content_y += text_height + int(padding * 0.3)

    # Draw episode text below series
    if episode_text:
        bbox = draw.textbbox((0, 0), episode_text, font=episode_font)
        text_height = bbox[3] - bbox[1]

        shadow_offset = 3
        draw.text((content_x + shadow_offset, content_y + shadow_offset),
                 episode_text, fill=(0, 0, 0, 200), font=episode_font)
        draw.text((content_x, content_y), episode_text, fill=(255, 255, 255, 255), font=episode_font)

    return img.convert('RGBA')


def main():
    parser = argparse.ArgumentParser(description="Add logo watermark to episode cover art")
    parser.add_argument("cover", help="Path to cover image")
    parser.add_argument("--logo", help="Path to logo (default: ../cover.png)")
    parser.add_argument("--position", default="bottom-right",
                       choices=['bottom-right', 'bottom-left', 'top-right', 'top-left', 'center'],
                       help="Logo position (default: bottom-right)")
    parser.add_argument("--opacity", type=float, default=0.9,
                       help="Logo opacity 0.0-1.0 (default: 0.9)")
    parser.add_argument("--size", type=float, default=0.12,
                       help="Logo size ratio 0.1-0.3 (default: 0.12)")
    parser.add_argument("--brand", default="Yudame Research",
                       help="Podcast brand name (default: 'Yudame Research')")
    parser.add_argument("--series", help="Series name text (e.g., 'Cardiovascular Health')")
    parser.add_argument("--episode", help="Episode text (e.g., 'Ep 3 - HRV')")
    parser.add_argument("--border", type=int, default=0,
                       help="Border width in pixels (default: 0 = no border)")
    parser.add_argument("--border-color", default="#FFC20E",
                       help="Border color in hex (default: #FFC20E = yellow)")

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
        size_ratio=args.size,
        brand_text=args.brand,
        series_text=args.series,
        episode_text=args.episode,
        border_width=args.border,
        border_color=args.border_color
    )

    print("\nDone! Logo and text overlays applied.")


if __name__ == "__main__":
    main()
