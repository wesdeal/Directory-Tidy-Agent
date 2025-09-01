# make log for agent actions.
# logs in json format
import json
from pathlib import Path
from datetime import datetime
from rules import rules
log_file = Path("log.json")

def log_action(action, file_name, folder_name=None):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "file_name": str(file_name),
        "folder_name": folder_name
    }

    if log_file.exists():
        try:
            with open(log_file, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []
    else:
        logs = []

    logs.append(log_entry)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=4)