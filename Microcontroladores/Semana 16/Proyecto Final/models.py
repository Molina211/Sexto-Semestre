from sqlalchemy import String, Integer, Column, Boolean, Float, DateTime
from database import Base

class Informacion(Base):
    __tablename__ = "Informacion"
    IDInfo = Column(Integer, primary_key=True, index=True)
    claveDinamica = Column(String(4))
    alarmaBuzzer = Column(Boolean, default=False)
    temperatura = Column(Float)
    fecha_hora = Column(DateTime)