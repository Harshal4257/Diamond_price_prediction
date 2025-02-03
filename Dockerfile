FROM python:3.8-slim-buster
WORKDIR /service
COPY requirements.txt .
COPY . ./
ENV PYTHONPATH=/service/src
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080 
ENTRYPOINT [ "python3","app.py" ]


