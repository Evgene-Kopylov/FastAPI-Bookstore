FROM python:3.10

WORKDIR /code/backend

COPY ./backend/requirements.txt /code/backend/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/backend/requirements.txt

COPY ./backend /code/backend

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]
