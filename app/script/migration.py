from collections.abc import Sequence
from os.path import join, realpath
from sys import argv

from alembic.command import downgrade, revision, upgrade
from alembic.config import Config
from fastapi import HTTPException


def main(args: Sequence[str] = argv) -> None:
    config = Config(file_=join(realpath("."), "alembic.ini"))
    command = args[1]
    match command:
        case "upgrade":
            upgrade(config, "head")
        case "downgrade":
            downgrade(config, "-1")
        case "generate":
            revision(config, message=args[2], autogenerate=True)
        case _:
            raise HTTPException(status_code=404, detail=f"Unknown command: {command}")