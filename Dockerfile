FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .




RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --timeout 300 --retries 5 --prefer-binary -r requirements.txt

COPY . .

CMD ["python", "main.py"]




