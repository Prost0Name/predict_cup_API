FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cup_classifier.keras .

COPY predict.py api.py ./

EXPOSE 8000

CMD ls -l && python api.py