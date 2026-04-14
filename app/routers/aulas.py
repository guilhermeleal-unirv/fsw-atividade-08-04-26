from fastapi import APIRouter, HTTPException
from typing import List
from ..models.aula import Aula, AulaBase, AulaCreate
from ..database.memory_db import aulas_db, professores_db, alunos_db, get_next_id

router = APIRouter(prefix="/aulas", tags=["Aulas"])

@router.get("", response_model=List[Aula])
def listar_aulas():
    """Lista todas as aulas cadastradas."""
    return aulas_db

@router.post("", response_model=Aula, status_code=201)
def criar_aula(aula: AulaCreate):
    """
    Cria uma nova aula indicando apenas data e o professor_id.
    A lista de presenças será inicializada como vazia.
    """
    if not any(p.id == aula.professor_id for p in professores_db):
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    
    nova_aula = Aula(id=get_next_id(aulas_db), **aula.model_dump(), presencas=[])
    aulas_db.append(nova_aula)
    return nova_aula

@router.put("/{aula_id}", response_model=Aula)
def atualizar_aula(aula_id: int, aula_atualizada: Aula):
    """
    Atualiza todos os dados de uma aula específica, permitindo modificar 
    a lista de presenças com os IDs dos alunos.
    """
    if aula_id != aula_atualizada.id:
        raise HTTPException(status_code=400, detail="ID da aula na rota difere do ID no corpo da requisição")
    
    for i, aula in enumerate(aulas_db):
        if aula.id == aula_id:
            # Validar se o professor referenciado existe
            if not any(p.id == aula_atualizada.professor_id for p in professores_db):
                raise HTTPException(status_code=404, detail="Professor referenciado não encontrado")
            
            # Validar se os alunos referenciados nas presenças existem
            ids_alunos_cadastrados = {a.id for a in alunos_db}
            for pid in aula_atualizada.presencas:
                if pid not in ids_alunos_cadastrados:
                    raise HTTPException(status_code=404, detail=f"Aluno com ID {pid} não encontrado")

            # Atualizar os dados da aula
            aulas_db[i] = aula_atualizada
            return aula_atualizada
            
    raise HTTPException(status_code=404, detail="Aula não encontrada")
