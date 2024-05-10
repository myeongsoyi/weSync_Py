FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update

RUN apt-get -y install python3-pip

RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app/ /app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

