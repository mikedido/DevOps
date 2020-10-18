FROM python:3.6

ENV FLASK_APP app.py

COPY run.py gunicorn-cfg.py requirements.txt .env ./
COPY . app

RUN pip install -r requirements.txt

EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]