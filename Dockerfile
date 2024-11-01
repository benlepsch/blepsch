FROM python:3.12

RUN pip install poetry
COPY . .

RUN poetry install

ENTRYPOINT ["poetry"]
CMD ["run", "python", "manage.py", "runserver", "0.0.0.0:8080"]