# Exercise - Python - Unit Tests

## Virtual environment

Install `pipenv`:

```
pip install pipenv
```

Note: On Linux it may be `pip3`.

Install dependencies:

```
pipenv install --dev
```

Now you can run the following commands:

Run application:

```
pipenv run python -m bibook
```

Run linter:

```
pipenv run pylint bibook
```

Run unit tests:

```
pipenv run pytest
```
