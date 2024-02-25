from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    id_pelicula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False)#Not null
    genero = Column(String(45), default=None)#def null
    duracion = Column(Integer, default=None)#def null
    inventario = Column(Integer, nullable=True, default=1)#def null

    def __init__(self, id_pelicula, nombre, genero=None, duracion=None, inventario=1):
        self.id_pelicula = id_pelicula
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f'Nombre:{self.nombre} Genero: {self.genero}\nId:{self.id_pelicula}'
