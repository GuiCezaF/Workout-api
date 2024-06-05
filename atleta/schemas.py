from contrib.schemas import BaseSchema
from typing import Annotated
from pydantic import Field, PositiveFloat


class Atleta(BaseSchema):
  nome: Annotated[str, Field(description='Nome do atleta', example='guilherme', max_length=50)]
  cpf: Annotated[str, Field(description='CPF do atleta', example='123.456.789-10', max_length=11)]
  idade: Annotated[int, Field(description='Idade do atleta', example='20',)]
  peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example='100',)]
  altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example='1.93',)]
  sexo: Annotated[str, Field(description='sexo do atleta', example='M', max_length=1)]