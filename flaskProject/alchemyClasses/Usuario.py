from sqlalchemy import Boolean, Column, Integer, LargeBinary, String

from alchemyClasses import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    ap_pat = Column(String(200), nullable=False)#Not null
    ap_mat = Column(String(200))
    password = Column(String(64), nullable=False)#Not null
    email = Column(String(200), unique=True, default=None)#Null
    profile_picture = Column(LargeBinary)#Longblob
    super_user = Column(Boolean, default=None)#tinyint, nullable=True

    def __init__(self, nombre, apPat, apMat, password, email, profile_picture, super_user):
        #self.id_usuario = id
        self.nombre = nombre
        self.ap_pat = apPat
        self.ap_mat = apMat
        self.password = password
        self.email = email
        self.profile_picture = profile_picture
        self.super_user = super_user

    def __str__(self):
        return f'Nombre:{self.nombre} {self.ap_pat}\nNum. de Cuenta:{self.id_usuario}'
