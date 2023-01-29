FROM python:3.11.1-buster

ENV POETRY_HOME /etc/poetry
ENV PATH $POETRY_HOME/bin:$PATH

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.3.2

RUN useradd -m -u 1000 app
USER 1000

WORKDIR /opt/new_cale
COPY --chown=1000:1000 pyproject.toml poetry.lock /opt/new_cale
COPY --chown=1000:1000 ./app /opt/new_cale/app
RUN poetry install --no-root --no-interaction

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
