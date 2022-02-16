import contextlib
import os
from pathlib import Path

import alembic.config


@contextlib.contextmanager
def working_directory(path):
    """Changes working directory and returns to previous on exit."""
    prev_cwd = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev_cwd)


def migrate():
    migrations_path = Path(__file__).parent
    with working_directory(migrations_path):
        alembicArgs = [
            "--raiseerr",
            "upgrade",
            "head",
        ]
        alembic.config.main(argv=alembicArgs)
