from pydantic import BaseModel

class ProfessorBase(BaseModel):
    nome: str

class Professor(ProfessorBase):
    id: int
