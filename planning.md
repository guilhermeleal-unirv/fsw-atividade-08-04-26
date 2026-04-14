# Planejamento: API RESTful de Controle de Frequência

## 1. Visão Geral
Sistema minimalista para gestão de presença em ambiente acadêmico, focado em simplicidade e performance.

## 2. Requisitos Técnicos
- **Linguagem:** Python 3.11+
- **Framework:** FastAPI
- **Web Server:** Uvicorn
- **Dependências:** `fastapi`, `uvicorn`, `pydantic`
- **Ambiente:** Dockerizado

## 3. Modelo de Dados (Entidades)
- **Professor:** - `id` (UUID ou int)
  - `nome` (str)
- **Aluno:** - `id` (UUID ou int)
  - `nome_completo` (str)
  - `cpf` (str, 11 caracteres)
- **Aula:** - `id` (UUID ou int)
  - `data` (ISO 8601 string)
  - `professor_id` (Relacional)
  - `presencas` (List[int/UUID]): Lista de IDs dos alunos presentes.

## 4. Definição de Endpoints (Swagger Style)
- **Professores:**
  - `GET /professores`: Retorna lista de objetos.
  - `POST /professores`: Cria novo professor (Payload: nome).
- **Alunos:**
  - `GET /alunos`: Retorna lista de objetos.
  - `POST /alunos`: Cria novo aluno (Payload: nome_completo, cpf).
- **Aulas:**
  - `GET /aulas`: Retorna lista com detalhes da aula.
  - `POST /aulas`: Cria aula (Payload: data, professor_id).
  - `PUT /aulas/{id}`: Atualização completa (Payload: data, professor_id, presencas).

## 5. Estrutura de Execução (Docker)
- **Dockerfile:** Baseado em `python:3.11-slim`.
- **Porta:** 8000.