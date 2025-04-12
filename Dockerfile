FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем модель отдельно и проверяем её наличие
COPY cup_classifier.keras .
RUN ls -l cup_classifier.keras && \
    chmod 644 cup_classifier.keras

# Копируем Python файлы
COPY predict.py api.py ./

EXPOSE 8000

# Добавим проверку наличия файлов перед запуском
CMD ls -l && python api.py