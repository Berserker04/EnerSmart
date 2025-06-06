
# EnerSmart - Sistema Experto de Ahorro Energético

Este sistema experto proporciona recomendaciones personalizadas para reducir el consumo energético en el hogar, basado en las prácticas actuales del usuario.

## 🚀 Requisitos

- Python 3.11 o superior
- pip
- (Opcional) Docker

## 🔧 Instalación

```bash
# Clonar el repositorio o descomprimir el archivo
cd enersmart

# (Opcional) Crear entorno virtual
python -m venv venv
source venv/bin/activate      # En Linux/Mac
venv\Scripts\activate       # En Windows

# Instalar dependencias
pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
uvicorn main:app --reload
```

El servidor estará disponible en: [http://localhost:8000](http://localhost:8000)

## 🐳 Ejecución con Docker (Opcional)

```bash
# Construir imagen
docker build -t enersmart .

# Ejecutar contenedor
docker run -p 8000:8000 enersmart
```

## 📚 Endpoints Clave

- `/api/diagnostic` - POST: Generar diagnóstico energético
- `/api/recommendations` - GET: Listar recomendaciones
- `/docs` - Interfaz interactiva Swagger UI

## 👨‍💻 Desarrolladores

- Carlos Andrés Hernández Copete
- Evelyn Montoya

Entrega: 06/06/2025
