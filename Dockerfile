FROM python:3.11-slim

WORKDIR /app

# Instalar dependências necessárias para a API
RUN pip install --no-cache-dir fastapi uvicorn pydantic

# Copiar todos os arquivos locais para o container
COPY . .

# Expor a porta 8000 que será usada pelo uvicorn
EXPOSE 8000

# Executar a aplicação com uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
