from black import main as black
from flake8 import __main__ as flake8
from isort import main as isort
from mypy import main as mypy


def main() -> None:
    """
    Lint your code with the same steps and order as in the ci.yml.
    If at some step an error occurred, then execution will stop at this step.
    (Except for Flake8, the next step will be executed even if there are errors)
    Run lint:
        $ poetry run lint
        $ lint
    """

    modules = ["app", ]

    print("\nFlake8:")
    flake8.main([*modules])

    print("\nMypy:")
    mypy.main(args=[*modules], clean_exit=True)

    print("\nIsort:")
    isort.main([*modules, "--check-only"])

    print("\nBlack:")
    black.main([*modules, "--check"], standalone_mode=False)


if __name__ == "__main__":
    main()
