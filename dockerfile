FROM python:3.14

WORKDIR /library

COPY library.py .

CMD ["python", "library.py"]
