from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(200), nullable=True)

    produtos = relationship("Produto", back_populates="categoria")

    def __repr__(self):
        return f"Categoria - id: {self.id} - nome: {self.nome} - descrição: {self.descricao}"
    
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    marca = Column(String(50), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    categoria = relationship("Categoria", back_populates="produtos")

    def __repr__(self):
        return f"Produto - id: {self.id} - nome: {self.nome} - marca: {self.marca} - categoria_id: {self.categoria_id} "