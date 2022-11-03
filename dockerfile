FROM python:3.10

EXPOSE 8000

WORKDIR /user
COPY . /user
RUN pip install -r requirements.txt
