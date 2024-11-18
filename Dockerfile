# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copie o script Python para o container
COPY app.py /app/

# Instale dependências, se houver
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o script Python
CMD ["python", "app.py"]
