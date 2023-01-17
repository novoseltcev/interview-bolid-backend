<p align="center">
  <a href="https://github.com/tiangolo/fastapi" target="_blank">
    <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white" alt="FastAPI" transform="scale">
  </a>
</p>
<p align="center">
    <em>Тестовое задание в компанию НВП Болид</em>
</p>

---
<p align="center">
  <a href="https://github.com/saywhy-ru/vpn-backend/actions" target="_blank">
    <img src="https://github.com/sunnamed434/UIElementsUnturned/workflows/CI/badge.svg" alt="CI">
  </a>
  <a href="https://mypy.readthedocs.io/en/stable/" target="_blank">
    <img src="http://www.mypy-lang.org/static/mypy_badge.svg" alt="Checked with mypy">
  </a>
  <a href="https://pycqa.github.io/isort/" target="_blank">
    <img src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336" alt="Imports: isort">
  </a>
  <a href="https://black.readthedocs.io/en/stable/" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
  </a>
</p>

---

## Working with GIT

We use [Trunk Based Development](https://trunkbaseddevelopment.com/) to work with `git`

## Commit/Branch Styling

### Commit Styling:
```text
<type>[!](<scope>): [#<issue num>] <description>
```
### Branch Styling:
```text
<type>/[#<issue num>-]<task_name>
```

Types:
   - **feat** - new functionality
   - **bug** - fix the bug by issue
   - **fix** - fix the bug, if you found it (without issue)
   - **chore** - refactoring and another routine (maybe without issue)


## Setup

1. Clone repository and `cd` into its directory:

```shell
$ git clone https://github.com/novoseltcev/interview-bolid-backend.git && cd interview-bolid-backend
```

2. Install poetry:

```shell
$ curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies and activate python-env:

```shell
$ poetry install && poetry shell
```

4. Configure environment:
    1. Copy example environment preset and open its:
    ```console
    $ cp .env.example .env && vim .env
    ```
    2. Configurate DB connection for local db or use default values for docker running:
   ```text
   POSTGRES_USER=
   POSTGRES_PASSWORD=
   POSTGRES_HOST=
   POSTGRES_PORT=
   POSTGRES_DB=
   ```

5. Run server:
    1. Local development server:
   ```console
   $ migrate upgrade && app
   ```
    2. Inside container:
   ```console
   $ docker-compose up -d --build && poetry run preset
   ```

8. [Open URL](http://0.0.0.0:5000?page=1&perPage=100)

## Code Quality Assurance
We use linter `flake8`, static type checker `mypy`, PEP 8 compliant opinionated formatter `black`, imports sortings utility `isort`.

### Lint your code:

```console
$ lint
```

### Format your code:

```console
$ format
```

### Set preset:

```console
$ preset
```
