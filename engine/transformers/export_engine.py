from pathlib import Path
from datetime import datetime


def ensure_export_directories():

    Path("data/exports").mkdir(
        parents=True,
        exist_ok=True
    )

    Path("data/processed").mkdir(
        parents=True,
        exist_ok=True
    )


def generate_export_filename(
    prefix: str,
    extension: str
):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    return f"{prefix}_{timestamp}.{extension}"