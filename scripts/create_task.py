#!/usr/bin/env python3
"""
Create a humanization task using the Humbot API.

Usage:
    python create_task.py "Your text here" [--model-type Quick|Standard|Advanced]
    python create_task.py --file input.txt [--model-type Quick]
"""

import sys
import json
import argparse
import requests
from pathlib import Path


# API Configuration
API_BASE = "https://humbot.ai/api/humbot/v1"

# Get API key from environment or prompt user
import os
API_KEY = os.getenv("HUMBOT_API_KEY", "")


def create_task(text: str, model_type: str = "Quick") -> dict:
    """
    Submit text to Humbot API for humanization.
    
    Args:
        text: The text to humanize
        model_type: One of "Quick", "Standard", or "Advanced"
    
    Returns:
        dict with task_id on success, or error info
    """
    if not API_KEY:
        return {
            "success": False,
            "error": "HUMBOT_API_KEY not set. Please get your API key from https://humbot.ai/ai-humanizer-api"
        }
    
    url = f"{API_BASE}/create"
    
    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY,
    }
    
    payload = {
        "input": text,
        "model_type": model_type
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        if result.get("error_code") == 0:
            return {
                "success": True,
                "task_id": result["data"]["task_id"],
                "model_type": model_type,
                "input_length": len(text)
            }
        else:
            return {
                "success": False,
                "error": f"API error: {result.get('error_msg', 'Unknown error')}"
            }
    
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Request timed out. The API might be slow or unavailable."
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"Network error: {str(e)}"
        }
    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "Invalid response from API (not JSON)"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        }


def main():
    parser = argparse.ArgumentParser(
        description="Submit text to Humbot for humanization",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "text",
        nargs="?",
        help="The text to humanize (or use --file)"
    )
    
    parser.add_argument(
        "--file",
        type=str,
        help="Read input text from file"
    )
    
    parser.add_argument(
        "--model-type",
        type=str,
        choices=["Quick", "Standard", "Advanced"],
        default="Quick",
        help="Model type to use (default: Quick)"
    )
    
    args = parser.parse_args()
    
    # Get input text
    if args.file:
        try:
            text = Path(args.file).read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.text:
        text = args.text
    else:
        print("Error: Provide text as argument or use --file", file=sys.stderr)
        parser.print_help()
        sys.exit(1)
    
    # Validate text
    if not text.strip():
        print("Error: Input text is empty", file=sys.stderr)
        sys.exit(1)
    
    word_count = len(text.split())
    if word_count < 10:
        print(f"Warning: Very short text ({word_count} words). Results may vary.", file=sys.stderr)
    
    # Submit task
    print(f"Submitting {word_count} words to Humbot ({args.model_type} mode)...", file=sys.stderr)
    
    result = create_task(text, args.model_type)
    
    if result["success"]:
        # Output just the task_id for easy script chaining
        print(result["task_id"])
        print(f"✓ Task created: {result['task_id']}", file=sys.stderr)
        print(f"  Use: python retrieve_result.py {result['task_id']}", file=sys.stderr)
    else:
        print(f"✗ Failed: {result['error']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
