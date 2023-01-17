FROM python:3.9-slim

EXPOSE 8502

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt && rm -rf /var/lib/apt/lists/* 


COPY . /app/

ENTRYPOINT ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8502"]