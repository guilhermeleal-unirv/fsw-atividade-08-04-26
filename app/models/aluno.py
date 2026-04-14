from pydantic import BaseModel

class AlunoBase(BaseModel):
    nome_completo: str
    cpf: str

class Aluno(AlunoBase):
    id: int
