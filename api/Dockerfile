FROM python:3.6.6
COPY . /api
WORKDIR /api
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

CMD ["python", "run.py"]
