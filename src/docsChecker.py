import validators
from pathlib import Path
from urllib.parse import urlparse


def is_url(string):
    """Check if a string is a valid URL."""
    return validators.url(string) is True


def is_local_path(string):
    """Check if a string is a valid local path."""
    path = Path(string)
    return path.exists()