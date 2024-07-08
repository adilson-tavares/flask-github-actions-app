FROM python:3.9-alpine3.20

WORKDIR /app

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 9001

ENTRYPOINT ["python3"]
CMD ["app.py"]