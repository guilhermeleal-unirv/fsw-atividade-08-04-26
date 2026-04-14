from fastapi import APIRouter
from typing import List
from ..models.aluno import Aluno, AlunoBase
from ..database.memory_db import alunos_db, get_next_id

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.get("", response_model=List[Aluno])
def listar_alunos():
    """Lista todos os alunos cadastrados."""
    return alunos_db

@router.post("", response_model=Aluno, status_code=201)
def criar_aluno(aluno: AlunoBase):
    """Cadastra um novo aluno."""
    novo_aluno = Aluno(id=get_next_id(alunos_db), **aluno.model_dump())
    alunos_db.append(novo_aluno)
    return novo_aluno
