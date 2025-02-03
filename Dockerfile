FROM python:3.8-slim-buster
WORKDIR /service
COPY . ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3","app.py" ]