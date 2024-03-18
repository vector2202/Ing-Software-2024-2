from alchemyClasses import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from datetime import date

class Renta(db.Model):

    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Boolean, default=False)#tinyint
    

    def __init__(self, id_usuario, id_pelicula, fecha=date.today(), dias_renta=5, estatus=False):
        self.idUsuario = id_usuario
        self.idPelicula = id_pelicula
        self.fecha_renta = fecha
        self.dias_de_renta = dias_renta
        self.estatus = estatus

    def __str__(self):
        return f"Id: {self.id_rentar}\nUsuario: {self.idUsuario}\nPelicula: {self.idPelicula}\nFecha:{self.fecha_renta}\nDias: {self.dias_de_renta}"
