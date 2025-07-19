import logging
import os
import sys

from PyQt6.QtCore import QCoreApplication, QProcess
from PyQt6.QtWidgets import QApplication

from core.event_service import EventService
from core.utils.cli_server import CliPipeHandler
from core.utils.win32.utilities import find_focused_screen


def reload_application(msg="Reloading Application...", forced=False):
    try:
        logging.info(msg)
        if hasattr(sys, "_cli_pipe_handler") and sys._cli_pipe_handler is not None:
            sys._cli_pipe_handler.stop_cli_pipe_server()
        QApplication.processEvents()
        QProcess.startDetached(sys.executable, sys.argv)
        if forced:
            os._exit(0)
        else:
            QCoreApplication.exit(0)
    except Exception as e:
        logging.error(f"Error during reload: {e}")
        os._exit(0)


def exit_application(msg="Exiting Application..."):
    logging.info(msg)
    try:
        if hasattr(sys, "_cli_pipe_handler") and sys._cli_pipe_handler is not None:
            sys._cli_pipe_handler.stop_cli_pipe_server()
        QCoreApplication.exit(0)
        # sys.exit(0)
    except:
        os._exit(0)


def process_cli_command(command: str):
    """
    Process CLI commands received from the Named Pipe server.
    Args:
        command (str): The command received from the CLI.
    """
    # Parse the command and options

    parts = command.strip().split()
    base_command = parts[0] if parts else ""

    # Extract screen parameter if present
    screen_name = None
    if "--screen" in command:
        screen_name = command.split("--screen", 1)[1].strip()
    elif "-s" in command:
        screen_name = command.split("-s", 1)[1].strip()

    if base_command == "reload":
        reload_application("Reloading Application from CLI...")

    elif base_command == "stop":
        exit_application("Exiting Application from CLI...")

    elif base_command in ["show-bar", "hide-bar", "toggle-bar"]:
        action = base_command.split("-")[0]
        EventService().emit_event("handle_bar_cli", action, screen_name)

    elif base_command == "toggle-widget":
        from core.global_state import get_bar_screens

        available_screens = get_bar_screens()
        if "--follow-mouse" in command:
            screen_name = find_focused_screen(follow_mouse=True, follow_window=False, screens=available_screens)
        elif "--follow-focus" in command:
            screen_name = find_focused_screen(follow_mouse=False, follow_window=True, screens=available_screens)

        widget_name = parts[1] if len(parts) > 1 else None
        if screen_name is not None:
            EventService().emit_event("handle_widget_cli", widget_name, screen_name)


def start_cli_server():
    handler = CliPipeHandler(process_cli_command)
    handler.start_cli_pipe_server()
    sys._cli_pipe_handler = handler
