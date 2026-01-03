# 1️⃣ Use official lightweight Python image
FROM python:3.12-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Prevent Python from writing pyc files & enable logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 4️⃣ Install system dependencies 
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 5️⃣ Copy requirements 
COPY requirements.txt .

# 6️⃣ Install Python dependencies
RUN pip install -r requirements.txt

# 7️⃣ Copy application code
COPY app ./app

# 8️⃣ Expose FastAPI port
EXPOSE 8000

# 9️⃣ Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
