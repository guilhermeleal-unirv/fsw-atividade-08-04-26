from fastapi import APIRouter, HTTPException
from typing import List
from ..models.professor import Professor, ProfessorBase
from ..database.memory_db import professores_db, get_next_id

router = APIRouter(prefix="/professores", tags=["Professores"])

@router.get("", response_model=List[Professor])
def listar_professores():
    """Lista todos os professores, incluindo os pré-cadastrados."""
    return professores_db

@router.post("", response_model=Professor, status_code=201)
def criar_professor(professor: ProfessorBase):
    """Cadastra um novo professor."""
    novo_professor = Professor(id=get_next_id(professores_db), **professor.model_dump())
    professores_db.append(novo_professor)
    return novo_professor
