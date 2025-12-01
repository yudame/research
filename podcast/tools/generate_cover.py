#!/usr/bin/env python3
"""
Generate podcast episode cover art using AI image generation.

Usage:
    python generate_cover.py <episode_dir> --prompt "Your image prompt"
    python generate_cover.py <episode_dir> --auto  # Auto-generate from report.md

Requirements:
    - OpenRouter API key in environment variable OPENROUTER_API_KEY
    - requests package: pip install requests
"""

import os
import sys
import argparse
import base64
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests package not installed. Run: pip install requests")
    sys.exit(1)


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_ID = "google/gemini-3-pro-image-preview"


def read_report(episode_dir):
    """Read the episode's report.md file."""
    report_path = Path(episode_dir) / "report.md"
    if not report_path.exists():
        return None
    return report_path.read_text()


def generate_prompt_from_report(report_text, episode_title):
    """
    Generate an image prompt by analyzing the report.
    This is a simple extraction - could be enhanced with AI analysis.
    """
    # Extract first few paragraphs for context
    lines = [l.strip() for l in report_text.split('\n') if l.strip() and not l.startswith('#')]
    summary = ' '.join(lines[:3])[:500]

    # Create focused prompt
    prompt = f"""Modern podcast episode cover art for "{episode_title}":

Style: Clean, professional, abstract visualization
Layout: Bold visual elements suitable for square format
Color palette: Deep navy blues and dark blues as the dominant theme throughout
Concept: {summary[:200]}

Design as square format (1024x1024px) with space for text overlay.
Professional, minimalist aesthetic suitable for Apple Podcasts.
No text in the image - pure visual design."""

    return prompt


def generate_image(prompt, output_path, aspect_ratio="1:1"):
    """
    Generate image using OpenRouter API with Gemini.

    Args:
        prompt: Image generation prompt
        output_path: Where to save the image
        aspect_ratio: Image aspect ratio (1:1, 16:9, 9:16, etc.)
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set")
        print("Set it with: export OPENROUTER_API_KEY='your-api-key'")
        sys.exit(1)

    # Append explicit instructions to avoid text/icons and ensure consistent dark theme
    enhanced_prompt = f"""{prompt}

IMPORTANT VISUAL REQUIREMENTS:
- The ENTIRE canvas from edge to edge must be deep navy blue and dark blue tones - no borders, frames, or light backgrounds
- Dark blue fills the complete image area - not just a section or inner frame
- Use bright teal, white, and silver only as accent colors on top of the dark blue theme
- Pure abstract visualization only
- Absolutely no text, no numbers, no labels, no annotations, no icons, no logos, no symbols, no letterforms of any kind
- Clean visual design without any typography or graphic elements

COMPOSITION:
- Visual interest and detail should be concentrated in the LOWER 2/3 of the image
- Keep the TOP 1/3 relatively simple and uncluttered for text overlay placement
- Main graphic elements should flow from center to bottom
- Avoid placing busy patterns or focal points in the upper third"""

    print(f"Generating image with {MODEL_ID}...")
    print(f"Aspect ratio: {aspect_ratio}")
    print(f"Enhanced prompt: {enhanced_prompt[:150]}...")

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://research.yuda.me",
                "X-Title": "Yudame Research Podcast Cover Generator"
            },
            json={
                "model": MODEL_ID,
                "modalities": ["text", "image"],
                "n": 1,
                "image_config": {
                    "aspect_ratio": aspect_ratio
                },
                "messages": [
                    {
                        "role": "user",
                        "content": f"Generate an image: {enhanced_prompt}"
                    }
                ]
            },
            timeout=120
        )

        response.raise_for_status()
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            message = result["choices"][0].get("message", {})

            # Images are returned in the 'images' field as data URLs
            raw_images = message.get("images", [])

            if not raw_images:
                print("Error: No images returned from API")
                sys.exit(1)

            # Get first image
            img = raw_images[0]
            image_url = None

            if isinstance(img, dict):
                image_url = img.get("image_url", {}).get("url", "")
            elif isinstance(img, str):
                image_url = img

            if not image_url:
                print("Error: Could not extract image URL from response")
                sys.exit(1)

            # Save the image
            if image_url.startswith("data:"):
                # Parse data URL and save to file
                try:
                    header, b64_data = image_url.split(",", 1)
                    image_data = base64.b64decode(b64_data)
                    Path(output_path).write_bytes(image_data)
                    print(f"✓ Cover art saved to: {output_path}")
                except Exception as e:
                    print(f"Error saving image: {e}")
                    sys.exit(1)
            else:
                # URL to download (shouldn't happen with Gemini but handle it)
                import urllib.request
                print(f"Downloading from URL...")
                urllib.request.urlretrieve(image_url, output_path)
                print(f"✓ Cover art saved to: {output_path}")

            return output_path, enhanced_prompt

        print("Error: No valid response from API")
        sys.exit(1)

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed: {str(e)}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate podcast episode cover art")
    parser.add_argument("episode_dir", help="Path to episode directory")
    parser.add_argument("--prompt", help="Custom image generation prompt")
    parser.add_argument("--auto", action="store_true", help="Auto-generate prompt from report.md")
    parser.add_argument("--aspect-ratio", default="1:1", help="Image aspect ratio (default: 1:1)")
    parser.add_argument("--output", help="Output filename (default: cover.png)")

    args = parser.parse_args()

    episode_dir = Path(args.episode_dir)
    if not episode_dir.exists():
        print(f"Error: Episode directory not found: {episode_dir}")
        sys.exit(1)

    # Determine output path
    output_filename = args.output or "cover.png"
    output_path = episode_dir / output_filename

    # Get or generate prompt
    if args.auto:
        print("Auto-generating prompt from report.md...")
        report = read_report(episode_dir)
        if not report:
            print(f"Error: report.md not found in {episode_dir}")
            sys.exit(1)

        # Try to extract title from directory name
        episode_title = episode_dir.name.replace('-', ' ').title()
        prompt = generate_prompt_from_report(report, episode_title)
        print(f"\nGenerated prompt:\n{prompt}\n")
    elif args.prompt:
        prompt = args.prompt
    else:
        print("Error: Must provide either --prompt or --auto")
        sys.exit(1)

    # Generate image
    image_path, enhanced_prompt = generate_image(prompt, output_path, args.aspect_ratio)

    # Save prompt to prompts.md if it exists
    prompts_file = episode_dir / "prompts.md"
    if prompts_file.exists():
        with open(prompts_file, 'a') as f:
            f.write(f"\n\n## Cover Art Generation\n\n")
            f.write(f"**Tool Used:** OpenRouter - {MODEL_ID}\n\n")
            f.write(f"**Original Prompt:**\n```\n{prompt}\n```\n\n")
            f.write(f"**Enhanced Prompt:**\n```\n{enhanced_prompt}\n```\n\n")
            f.write(f"**Aspect Ratio:** {args.aspect_ratio}\n\n")
            f.write(f"**Output:** {output_filename}\n\n")
            f.write(f"**Date:** {os.popen('date +%Y-%m-%d').read().strip()}\n")
        print(f"✓ Prompt logged to prompts.md")

    print(f"\nDone! Cover art ready at: {image_path}")
    print(f"\nNext step: Add branding with add_logo_watermark.py")
    print(f"\nTo use in feed.xml, add this line to the episode <item>:")
    print(f'  <itunes:image href="https://research.yuda.me/podcast/episodes/{episode_dir.name}/{output_filename}?v=1"/>')


if __name__ == "__main__":
    main()
