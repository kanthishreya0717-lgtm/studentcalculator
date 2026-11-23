FROM python:3.12-slim

WORKDIR /app

COPY grade.py .

CMD ["python", "grade.py"]