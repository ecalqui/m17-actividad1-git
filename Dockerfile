# Imagen base con Python 3.10
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el script al contenedor
COPY script-2.py .

# Comando por defecto al arrancar el contenedor
CMD ["python", "script-2.py"]
