FROM python:3.8-slim-buster
WORKDIR /service
COPY . ./
ENV PYTHONPATH=/service/src
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3","app.py" ]


