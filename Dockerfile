FROM python:3.12-slim

WORKDIR /app

ADD ngrams.py .

CMD ["python", "ngrams.py"] 
