#!/usr/bin/env python3
"""
Retrieve humanization results from Humbot API.

Usage:
    python retrieve_result.py <task_id> [--wait] [--max-wait 60]
    
    --wait: Keep polling until task completes
    --max-wait: Maximum seconds to wait (default: 60)
"""

import sys
import json
import time
import argparse
import requests
from typing import Optional


# API Configuration
import os

API_BASE = "https://test123.humbot.ai/api/humbot/v1"
API_KEY = os.getenv("HUMBOT_API_KEY")
AUTH_HEADER = os.getenv("HUMBOT_AUTH_HEADER")

if not API_KEY:
    print("Error: HUMBOT_API_KEY environment variable not set", file=sys.stderr)
    print("Set it with: export HUMBOT_API_KEY='your-api-key'", file=sys.stderr)
    sys.exit(1)

if not AUTH_HEADER:
    print("Error: HUMBOT_AUTH_HEADER environment variable not set", file=sys.stderr)
    print("Set it with: export HUMBOT_AUTH_HEADER='your-auth-header'", file=sys.stderr)
    sys.exit(1)


def retrieve_result(task_id: str) -> dict:
    """
    Retrieve result for a task from Humbot API.
    
    Args:
        task_id: The task ID from create_task
    
    Returns:
        dict with result data or error info
    """
    url = f"{API_BASE}/retrieve"
    
    headers = {
        "Authorization": AUTH_HEADER,
        "api-key": API_KEY,
    }
    
    params = {"task_id": task_id}
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        
        result = response.json()
        
        if result.get("err_code") == 0:
            data = result["data"]
            return {
                "success": True,
                "status": data.get("subtask_status"),
                "completed": data.get("task_status", False),
                "input": data.get("input"),
                "output": data.get("output"),
                "input_words": data.get("input_words"),
                "output_words": data.get("words_used"),
                "detection_result": data.get("detection_result"),
                "detection_score": data.get("detection_score"),
                "mode": data.get("mode")
            }
        else:
            return {
                "success": False,
                "error": f"API error: {result.get('err_msg', 'Unknown error')}"
            }
    
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Request timed out"
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"Network error: {str(e)}"
        }
    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "Invalid response from API"
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}"
        }


def wait_for_completion(task_id: str, max_wait: int = 60, poll_interval: int = 2) -> dict:
    """
    Poll the API until task completes or timeout.
    
    Args:
        task_id: The task ID
        max_wait: Maximum seconds to wait
        poll_interval: Seconds between polls
    
    Returns:
        Final result dict
    """
    start_time = time.time()
    attempts = 0
    
    while True:
        attempts += 1
        elapsed = time.time() - start_time
        
        if elapsed > max_wait:
            return {
                "success": False,
                "error": f"Timeout after {max_wait}s ({attempts} attempts)"
            }
        
        result = retrieve_result(task_id)
        
        if not result["success"]:
            return result
        
        if result["completed"]:
            return result
        
        # Still processing
        status = result.get("status", "unknown")
        print(f"⏳ Status: {status} (attempt {attempts}, {elapsed:.0f}s elapsed)", file=sys.stderr)
        
        time.sleep(poll_interval)


def format_output(result: dict, verbose: bool = True) -> str:
    """Format the result for display."""
    if not result["success"]:
        return f"Error: {result['error']}"
    
    if not result["completed"]:
        return f"Task still processing (status: {result.get('status')})"
    
    lines = []
    
    # Output text
    lines.append("=" * 60)
    lines.append("HUMANIZED TEXT")
    lines.append("=" * 60)
    lines.append(result["output"])
    lines.append("")
    
    # Stats
    lines.append("=" * 60)
    lines.append("STATISTICS")
    lines.append("=" * 60)
    lines.append(f"Original:    {result['input_words']} words")
    lines.append(f"Humanized:   {result['output_words']} words")
    lines.append(f"Detection:   {result['detection_result'].upper()} (score: {result['detection_score']}/100)")
    lines.append(f"Model:       {result['mode']}")
    lines.append("")
    
    if verbose and result.get('input'):
        lines.append("=" * 60)
        lines.append("ORIGINAL TEXT (first 500 chars)")
        lines.append("=" * 60)
        original = result['input']
        if len(original) > 500:
            lines.append(original[:500] + "...")
        else:
            lines.append(original)
        lines.append("")
    
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Retrieve humanization results from Humbot",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "task_id",
        help="Task ID from create_task.py"
    )
    
    parser.add_argument(
        "--wait",
        action="store_true",
        help="Keep polling until task completes"
    )
    
    parser.add_argument(
        "--max-wait",
        type=int,
        default=60,
        help="Maximum seconds to wait (default: 60)"
    )
    
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON instead of formatted text"
    )
    
    parser.add_argument(
        "--no-original",
        action="store_true",
        help="Don't show original text in output"
    )
    
    args = parser.parse_args()
    
    # Get result
    if args.wait:
        print(f"Polling for task {args.task_id}...", file=sys.stderr)
        result = wait_for_completion(args.task_id, args.max_wait)
    else:
        result = retrieve_result(args.task_id)
    
    # Output
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(format_output(result, verbose=not args.no_original))
        
        if result["success"] and result["completed"]:
            sys.exit(0)
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
