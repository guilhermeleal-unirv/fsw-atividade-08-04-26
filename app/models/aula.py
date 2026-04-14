from pydantic import BaseModel
from typing import List

class AulaBase(BaseModel):
    data: str
    professor_id: int

class AulaCreate(AulaBase):
    pass

class Aula(AulaBase):
    id: int
    presencas: List[int] = []
