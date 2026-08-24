#!/usr/bin/env python3
"""
Codex CLI Notification Hook
Supports multiple Codex notification events with rich macOS notifications.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from typing import Any


APP = "com.googlecode.iterm2"
GROUP = "codex"
MAX_MESSAGE_LENGTH = 220


def notify(title: str, message: str, sound: str | None = None) -> None:
    """Send a native macOS notification."""
    notifier = shutil.which("terminal-notifier")
    if not notifier:
        print("terminal-notifier not found.")
        return

    args = [
        notifier,
        "-title", title,
        "-message", message[:MAX_MESSAGE_LENGTH],
        "-group", GROUP,
        "-activate", APP,
        "-ignoreDnD",
    ]

    if sound:
        args.extend(["-sound", sound])

    subprocess.run(args, check=False)


def handle_turn_complete(data: dict[str, Any]) -> None:
    assistant = data.get("last-assistant-message") or "Task Complete"

    inputs = data.get("input_messages", [])
    prompt = " ".join(inputs).strip()

    title = f"✅ Codex • {assistant}"

    if prompt:
        message = f"Prompt: {prompt}"
    else:
        message = "The current Codex task finished successfully."

    notify(title, message, sound="Glass")


def handle_error(data: dict[str, Any]) -> None:
    message = data.get("message", "Unknown error occurred.")
    notify("❌ Codex Error", message, sound="Basso")


def handle_task_started(data: dict[str, Any]) -> None:
    task = data.get("task", "Running task...")
    notify("🚀 Codex Started", task)


def handle_auth(data: dict[str, Any]) -> None:
    status = data.get("status", "Authentication complete.")
    notify("🔐 Codex Authentication", status)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: notify.py '<NOTIFICATION_JSON>'")
        return 1

    try:
        payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        print("Invalid notification JSON.")
        return 1

    event = payload.get("type")

    handlers = {
        "agent-turn-complete": handle_turn_complete,
        "agent-error": handle_error,
        "task-started": handle_task_started,
        "auth-success": handle_auth,
    }

    handler = handlers.get(event)

    if handler:
        handler(payload)
    else:
        print(f"Ignoring notification type: {event}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
