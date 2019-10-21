FROM python:3.7

COPY main.py /

EXPOSE 65432

ENTRYPOINT ["python3", "main.py"]
