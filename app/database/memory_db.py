from typing import List
from pydantic import BaseModel

# Persistência em memória
class ProfessorPlaceholder(BaseModel):
    id: int
    nome: str

professores_db: List[ProfessorPlaceholder] = [
    ProfessorPlaceholder(id=1, nome="João Silva"),
    ProfessorPlaceholder(id=2, nome="Maria Souza")
]
alunos_db = []
aulas_db = []

def get_next_id(db: List) -> int:
    return max([item.id for item in db], default=0) + 1
