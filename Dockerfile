FROM python:3.8-slim-buster
WORKDIR /service  
COPY . /service   
RUN pip install -r /service/requirements.txt  
ENTRYPOINT [ "python3", "/service/app.py" ]  
