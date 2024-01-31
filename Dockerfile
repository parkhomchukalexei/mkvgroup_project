
FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
EXPOSE 8000
COPY . /web_django/
WORKDIR /web_django
RUN pip install -r requirements.txt
RUN adduser --disabled-password admin-user
RUN chown admin-user:admin-user /web_django/logs.log

USER admin-user
CMD ["python", "manage.py", "makemigrations", "0.0.0.0:8000"]
CMD ["python", "manage.py", "migrate", "0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]