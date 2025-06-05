# Dockerfile
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Puerto que expondrá el contenedor (Railway usa 8000 por defecto)
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
