from sqlalchemy import Boolean, Column, Integer, LargeBinary, String

from alchemyClasses import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)#Not null
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)#Not null
    email = Column(String(200), unique=True, default=None)#Null
    profilePicture = Column(LargeBinary)#Longblob
    superUser = Column(Boolean, default=None)#tinyint, nullable=True

    def __init__(self, nombre, apPat, apMat, password, email, profile_picture, super_user):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profile_picture
        self.superUser = super_user

    def __str__(self):
        return f'Nombre:{self.nombre} {self.apPat}\nNum. de Cuenta:{self.idUsuario}'
