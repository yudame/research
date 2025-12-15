#!/usr/bin/env python3
"""
Perplexity Deep Research API - Automated Research Script

This script uses Perplexity's Deep Research API (sonar-deep-research model) to conduct
comprehensive research with citations from authoritative sources.

Usage:
    python perplexity_deep_research.py "Your research prompt here"
    python perplexity_deep_research.py --file prompt.txt
    python perplexity_deep_research.py --file prompt.txt --output results.md
    python perplexity_deep_research.py "prompt" --reasoning-effort high

Requirements:
    - PERPLEXITY_API_KEY in .env file (get at https://www.perplexity.ai/settings/api)
    - pip install requests python-dotenv

API Documentation:
    https://docs.perplexity.ai/getting-started/models/models/sonar-deep-research
"""

import requests
import os
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

# Try to load dotenv, but don't fail if not installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def get_api_key() -> str | None:
    """Get API key from environment or .env file."""
    api_key = os.getenv('PERPLEXITY_API_KEY')

    if not api_key:
        # Try loading from .env in parent directories
        for parent in [Path.cwd()] + list(Path.cwd().parents)[:3]:
            env_file = parent / '.env'
            if env_file.exists():
                with open(env_file) as f:
                    for line in f:
                        if line.startswith('PERPLEXITY_API_KEY='):
                            api_key = line.split('=', 1)[1].strip().strip('"\'')
                            break
                if api_key:
                    break

    return api_key


def run_perplexity_research(
    prompt: str,
    reasoning_effort: str = "high",
    verbose: bool = True,
    log_file: str | None = None
) -> str | None:
    """
    Submit a research request to Perplexity Deep Research API.

    Args:
        prompt: Research prompt/query
        reasoning_effort: Computational effort level (low, medium, high)
        verbose: Whether to print progress messages

    Returns:
        Research report text or None if failed
    """
    api_key = get_api_key()

    if not api_key:
        print("ERROR: PERPLEXITY_API_KEY not found")
        print("Set it in your environment or .env file")
        print("Get your API key at: https://www.perplexity.ai/settings/api")
        return None

    # Helper to log to both stdout and file
    def log(msg):
        if verbose:
            print(msg)
        if log_file:
            with open(log_file, 'a') as f:
                f.write(msg + '\n')

    if verbose or log_file:
        log("=" * 60)
        log("PERPLEXITY DEEP RESEARCH API")
        log("=" * 60)
        log(f"\nPrompt: {prompt[:200]}..." if len(prompt) > 200 else f"\nPrompt: {prompt}")
        log(f"\nConfiguration:")
        log(f"  Model: sonar-deep-research")
        log(f"  Reasoning Effort: {reasoning_effort}")
        log(f"\nSubmitting research request...")
        log(f"Expected time: 30-120 seconds")
        log("-" * 60)

    # API endpoint
    url = "https://api.perplexity.ai/chat/completions"

    # Prepare payload
    payload = {
        "model": "sonar-deep-research",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "reasoning_effort": reasoning_effort
    }

    # Headers with authentication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make API request with 180 second timeout
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=180
        )
    except requests.exceptions.Timeout:
        log("ERROR: Request timed out after 180 seconds")
        log("The research query may be too complex. Try:")
        log("  - Simplifying the prompt")
        log("  - Using reasoning_effort='medium' instead of 'high'")
        return None
    except requests.exceptions.RequestException as e:
        log(f"ERROR: Request failed: {e}")
        return None

    # Check response status
    if response.status_code == 200:
        try:
            result = response.json()

            # Extract the research content
            if 'choices' in result and len(result['choices']) > 0:
                content = result['choices'][0]['message']['content']

                # Get usage stats if available
                if 'usage' in result:
                    usage = result['usage']
                    log(f"\nAPI Usage:")
                    log(f"  Input tokens: {usage.get('prompt_tokens', 'N/A')}")
                    log(f"  Output tokens: {usage.get('completion_tokens', 'N/A')}")
                    log(f"  Total tokens: {usage.get('total_tokens', 'N/A')}")

                word_count = len(content.split())
                log(f"\n{'=' * 60}")
                log(f"RESEARCH COMPLETE")
                log(f"Length: ~{word_count} words")
                log(f"{'=' * 60}\n")

                return content
            else:
                print("ERROR: Unexpected API response format")
                print(json.dumps(result, indent=2))
                return None

        except json.JSONDecodeError:
            print("ERROR: Failed to parse API response as JSON")
            print(f"Response: {response.text[:500]}")
            return None

    elif response.status_code == 401:
        print("ERROR: Authentication failed (401 Unauthorized)")
        print("Your API key is invalid or expired")
        print("Check your key at: https://www.perplexity.ai/settings/api")
        return None

    elif response.status_code == 429:
        print("ERROR: Rate limit exceeded (429 Too Many Requests)")
        print("Wait 60 seconds and try again")
        print("Check your usage at: https://www.perplexity.ai/settings/api")
        return None

    elif response.status_code == 500:
        print("ERROR: Perplexity API server error (500)")
        print("The service may be experiencing issues")
        print("Try again in 30 seconds")
        return None

    else:
        print(f"ERROR: API returned status {response.status_code}")
        try:
            error_data = response.json()
            print(f"Error details: {json.dumps(error_data, indent=2)}")
        except:
            print(f"Response: {response.text[:500]}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Run Perplexity Deep Research on a topic",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s "Research the history of quantum computing"
    %(prog)s --file research_prompt.txt
    %(prog)s --file prompt.txt --output results.md
    %(prog)s "prompt" --reasoning-effort medium

Environment:
    PERPLEXITY_API_KEY - Your Perplexity API key (required)
                        Get one at: https://www.perplexity.ai/settings/api
        """
    )

    parser.add_argument(
        'prompt',
        nargs='*',
        help='Research prompt (or use --file)'
    )

    parser.add_argument(
        '--file', '-f',
        help='Read prompt from file'
    )

    parser.add_argument(
        '--output', '-o',
        help='Write output to file'
    )

    parser.add_argument(
        '--reasoning-effort', '-r',
        choices=['low', 'medium', 'high'],
        default='high',
        help='Computational effort level (default: high)'
    )

    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Minimal output (just the result)'
    )

    parser.add_argument(
        '--auto-save',
        action='store_true',
        help='Automatically save output and logs with timestamp (default: True unless --output specified)'
    )

    parser.add_argument(
        '--no-auto-save',
        action='store_true',
        help='Disable automatic file saving'
    )

    parser.add_argument(
        '--log-dir',
        help='Directory for output and log files (default: current directory)'
    )

    args = parser.parse_args()

    # Get prompt from arguments or file
    if args.file:
        try:
            with open(args.file, 'r') as f:
                prompt = f.read().strip()
        except FileNotFoundError:
            print(f"ERROR: File not found: {args.file}")
            sys.exit(1)
    elif args.prompt:
        prompt = ' '.join(args.prompt)
    else:
        parser.print_help()
        sys.exit(1)

    if not prompt:
        print("ERROR: Empty prompt")
        sys.exit(1)

    # Determine if auto-save should be enabled
    auto_save = not args.no_auto_save and (args.auto_save or not args.output)

    # Set up log directory
    log_dir = args.log_dir or '.'
    if log_dir != '.' and not Path(log_dir).exists():
        Path(log_dir).mkdir(parents=True, exist_ok=True)

    # Set up auto-save file paths
    output_file = args.output
    log_file = None

    if auto_save and not args.output:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = str(Path(log_dir) / f"perplexity_output_{timestamp}.md")
        log_file = str(Path(log_dir) / f"perplexity_log_{timestamp}.txt")
        print(f"Auto-save enabled:")
        print(f"  Output: {output_file}")
        print(f"  Log: {log_file}")
        print()
    elif auto_save and args.output:
        # If user specified output file, also create log file
        output_path = Path(args.output)
        output_file = str(output_path)
        log_file = str(output_path.parent / (output_path.stem + '_log.txt'))
        print(f"Saving output to: {output_file}")
        print(f"Saving log to: {log_file}")
        print()

    # Run the research
    result = run_perplexity_research(
        prompt,
        reasoning_effort=args.reasoning_effort,
        verbose=not args.quiet,
        log_file=log_file
    )

    if result:
        # Output to file or stdout
        if output_file:
            with open(output_file, 'w') as f:
                f.write(f"# Perplexity Deep Research Results\n\n")
                f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
                f.write(f"**Model:** sonar-deep-research\n\n")
                f.write(f"**Reasoning Effort:** {args.reasoning_effort}\n\n")
                f.write(f"**Prompt:** {prompt}\n\n")
                f.write("---\n\n")
                f.write(result)
            print(f"\nResults saved to: {output_file}")
            if log_file:
                print(f"Log saved to: {log_file}")
        else:
            if not args.quiet:
                print("\n" + "=" * 60)
                print("RESEARCH OUTPUT")
                print("=" * 60 + "\n")
            print(result)

        sys.exit(0)
    else:
        print("\nResearch failed. See error messages above.")
        print("\nFallback: Use browser at https://www.perplexity.ai/")
        sys.exit(1)


if __name__ == "__main__":
    main()
