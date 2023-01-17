import uvicorn

from app.core.settings import get_settings


def main() -> None:
    uvicorn.run(
        "app.__main__:app",
        host=get_settings().HOST,
        port=get_settings().PORT,
        reload=True,
    )


if __name__ == "__main__":
    main()
