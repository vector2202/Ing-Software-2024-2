from alchemyClasses.Usuario import Usuario
from alchemyClasses import db

def borra_usuario(id_usuario):
    usuario = Usuario.query.filter(Usuario.id_usuario == id_usuario).first()
    db.session.delete(usuario)
    db.session.commit()
