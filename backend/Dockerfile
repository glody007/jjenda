FROM python:3.6.6
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "run.py", "-h", "0.0.0.0"]
