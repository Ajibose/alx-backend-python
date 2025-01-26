# containerize the django messaging app
FROM python:3.10
RUN pip install -r requirements.txt
COPY . ./messaging_app
EXPOSE 8000
