from sqlalchemy import Integer, String
from atleta.models import AtletaModel
from contrib.models import BaseModel
from sqlalchemy.orm import Mapped, mapped_column,relationship


class CentroTreinamentoModel(BaseModel):
  __tablename__ = 'centro_treinanto'
  
  pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
  nome: Mapped[str] = mapped_column(String(50), nullable=False )
  endereco: Mapped[str] = mapped_column(String(60), nullable=False )
  proprietario: Mapped[str] = mapped_column(String(20), nullable=False )
  Atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')
  