#!/usr/bin/env python3
"""
Generate podcast episode cover art using AI image generation.

Usage:
    python generate_cover.py <episode_dir> --prompt "Your image prompt"
    python generate_cover.py <episode_dir> --auto  # Auto-generate from report.md

Requirements:
    - OpenAI API key in environment variable OPENAI_API_KEY
    - openai package: pip install openai
"""

import os
import sys
import argparse
import json
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Error: openai package not installed. Run: pip install openai")
    sys.exit(1)


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

Style: Clean, professional, scientific
Layout: Bold typography with subtle data visualization elements
Color palette: Deep blues and teals with white/silver accents
Concept: {summary[:200]}

Design as a square format (1400x1400px) with space for episode title overlay.
Professional, minimalist aesthetic suitable for Apple Podcasts.
No text in the image - pure visual design."""

    return prompt


def generate_image(prompt, output_path, size="1024x1024", model="dall-e-3"):
    """
    Generate image using OpenAI DALL-E.

    Args:
        prompt: Image generation prompt
        output_path: Where to save the image
        size: Image size (1024x1024, 1792x1024, or 1024x1792)
        model: dall-e-2 or dall-e-3
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='your-api-key'")
        sys.exit(1)

    # Append explicit instructions to avoid text/icons/annotations
    enhanced_prompt = f"""{prompt}

IMPORTANT: Pure abstract visualization only. Absolutely no text, no numbers, no labels, no annotations, no icons, no logos, no symbols, no letterforms of any kind. Clean visual design without any typography or graphic elements."""

    client = OpenAI(api_key=api_key)

    print(f"Generating image with {model}...")
    print(f"Enhanced prompt: {enhanced_prompt[:150]}...")

    try:
        response = client.images.generate(
            model=model,
            prompt=enhanced_prompt,
            size=size,
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        revised_prompt = getattr(response.data[0], 'revised_prompt', None)

        print(f"Image generated successfully!")
        if revised_prompt:
            print(f"Revised prompt: {revised_prompt[:100]}...")

        # Download image
        import urllib.request
        print(f"Downloading to {output_path}...")
        urllib.request.urlretrieve(image_url, output_path)

        print(f"✓ Cover art saved to: {output_path}")
        return output_path, revised_prompt

    except Exception as e:
        print(f"Error generating image: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate podcast episode cover art")
    parser.add_argument("episode_dir", help="Path to episode directory")
    parser.add_argument("--prompt", help="Custom image generation prompt")
    parser.add_argument("--auto", action="store_true", help="Auto-generate prompt from report.md")
    parser.add_argument("--size", default="1024x1024", help="Image size (default: 1024x1024)")
    parser.add_argument("--model", default="dall-e-3", help="Model to use (default: dall-e-3)")
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
    image_path, revised_prompt = generate_image(prompt, output_path, args.size, args.model)

    # Save prompt to prompts.md if it exists
    prompts_file = episode_dir / "prompts.md"
    if prompts_file.exists():
        with open(prompts_file, 'a') as f:
            f.write(f"\n\n## Cover Art Generation\n\n")
            f.write(f"**Tool Used:** OpenAI {args.model}\n\n")
            f.write(f"**Original Prompt:**\n```\n{prompt}\n```\n\n")
            if revised_prompt:
                f.write(f"**Revised Prompt:**\n```\n{revised_prompt}\n```\n\n")
            f.write(f"**Output:** {output_filename}\n\n")
            f.write(f"**Date:** {os.popen('date +%Y-%m-%d').read().strip()}\n")
        print(f"✓ Prompt logged to prompts.md")

    print(f"\nDone! Cover art ready at: {image_path}")
    print(f"\nTo use in feed.xml, add this line to the episode <item>:")
    print(f'  <itunes:image href="https://yudame.github.io/research/podcast/episodes/{episode_dir.name}/{output_filename}"/>')


if __name__ == "__main__":
    main()
