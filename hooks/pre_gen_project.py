"""Module with pre-generation cookiecutter hooks."""
import re
import sys


def check_sanity(value):
    """Check whether user input is sane."""
    return re.match(r"[a-z0-9\-_]+", value, re.IGNORECASE)


# Check sanity of the inputs
user_input = {
    "project": {
        "value": "{{ cookiecutter.project }}",
        "pattern": r"^[a-zA-Z][a-zA-Z0-9\-_\s]+$",
    },
    "azure_user": {
        "value": "{{ cookiecutter.azure_user }}",
        "pattern": r"^[a-zA-Z\-_]+$",
    },
    "azure_project": {
        "value": "{{ cookiecutter.azure_project }}",
        "pattern": r"^[^_.][^:/\\~&%;@'\"?<>|#$*}{,+=[\]]+[^.]$",
    },
    "azure_repo": {
        "value": "{{ cookiecutter.azure_repo }}",
        "pattern": r"^[a-zA-Z][a-zA-Z0-9\-_]+$",
    },
    "azure_url": {
        "value": "{{ cookiecutter.azure_url }}",
        "pattern": r"^https://[a-zA-Z\-_]+@dev.azure.com/[a-zA-Z\-_]+/[a-zA-Z][a-zA-Z0-9\-_]+/_git/[a-zA-Z][a-zA-Z0-9\-_]+$",
    },
}

# Check sanity of the inputs
for field, check in user_input.items():
    if not re.match(check["pattern"], check["value"]):
        print(f"ERROR: Input {field!r} contains invalid characters: {check['value']!r}!")
        sys.exit(1)
