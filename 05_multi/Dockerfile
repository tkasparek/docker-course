from ubuntu

RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean

RUN adduser --home /app azdo

COPY --chown=azdo requirements.txt /app/

RUN pip install -r /app/requirements.txt

USER azdo

WORKDIR /app

EXPOSE 8000

COPY main.py /app/

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8000
