import subprocess

from black import main as black
from isort import main as isort


def main() -> None:
    """
    Format your code with isort, autoflake, black.
        1. Isort sort imports one per line
        2. Autoflake remove unused imports
        3. Isort format your imports - correct order of imports
        4. Black format your code - PEP 8 standard
    Run format:
        $ poetry run format
        $ format
    Note:
        It's not a magic wand that will fix everything.
        You have to write type annotations:^)
    """

    modules = [
        "app",
    ]

    isort.main([*modules, "--force-single-line-imports"])
    subprocess.run(
        [
            "autoflake",
            "--remove-all-unused-imports",
            "--recursive",
            "--remove-unused-variables",
            "--in-place",
            *modules,
            "--exclude=__init__.py",
        ]
    )
    isort.main([*modules])
    black.main([*modules])


if __name__ == "__main__":
    main()
