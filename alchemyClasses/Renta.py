from alchemyClasses import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from datetime import date

class Renta(db.Model):

    __tablename__ = 'rentar'
    id_rentar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False)
    id_pelicula = Column(Integer, ForeignKey('pelicula.id_pelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=False)#tinyint
    

    def __init__(self, id_usuario, id_pelicula, fecha=date.today(), dias_renta=5, estatus=False):
        #self.id_rentar = id_renta
        self.id_usuario = id_usuario
        self.id_pelicula = id_pelicula
        self.fecha_renta = fecha
        self.dias_de_renta = dias_renta
        self.estatus = estatus

    def __str__(self):
        return f"Id: {self.id_rentar}\nUsuario: {self.id_usuario}\nPelicula: {self.id_pelicula}\nFecha:{self.fecha_renta}\nDias: {self.dias_de_renta}"
