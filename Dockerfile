FROM python:3.9
COPY /app /app
COPY /db /db
COPY main.py /
COPY pyproject.toml /
COPY poetry.lock /
COPY logging.conf /
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
ENV POETRY_VIRTUALENVS_IN_PROJECT true
RUN pip3 install --no-cache-dir poetry==1.1.10 && poetry config virtualenvs.create false && poetry install --no-interaction

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]