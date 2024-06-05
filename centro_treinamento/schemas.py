from typing import Annotated

from pydantic import Field
from contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
  nome: Annotated[str, Field(description='Nome do Centro de treinamento', example='CT IronBerg', max_length=50)]
  endereco: Annotated[str, Field(description='Endereço do Centro de treinamento', example='Rua X, 105', max_length=60)]
  proprietario: Annotated[str, Field(description='Proprietario do Centro de treinamento', example='Cariane', max_length=30)]
