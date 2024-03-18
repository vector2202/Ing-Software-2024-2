from sqlalchemy import delete
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Renta import Renta
from alchemyClasses import db
from flask import flash

def agregar_usuario(data):
    nombre = data.get("nombre")
    ap_pat = data.get("ap_pat")
    ap_mat = data.get("ap_mat")
    password = data.get("password")
    email = data.get("email")
    super_user = data.get("super_user") == 'on'
    usuario = Usuario(nombre, ap_pat, ap_mat, password, email, None, super_user)
    db.session.add(usuario)
    db.session.commit()
    return True
    
def modificar_usuario(data, id_usuario):
    nombre = data.get("nombre")
    ap_pat = data.get("apPat")
    ap_mat = data.get("apMat")
    password = data.get("password")
    email = data.get("email")
    super_user = data.get("superUser") == "on"
    print(super_user)
    print(data)
    usuario = Usuario.query.get(id_usuario)
    usuario.nombre = nombre
    usuario.apPat = ap_pat
    usuario.apMat = ap_mat
    usuario.password = password
    usuario.email = email
    usuario.superUser = super_user
    
    db.session.commit()
    return True
    
def eliminar_usuario(id_usuario):
    #renta = Renta.query.filter_by(id_usuario).delete()
    usuario = Usuario.query.filter_by(idUsuario=id_usuario).first()
    db.session.delete(usuario)
    db.session.commit()
    return True

def obtener_usuario(id_usuario):
    data = Usuario.query.get(id_usuario)
    return data
    

def obtener_usuarios():
    try:
        data = Usuario.query.all()
        return data
    except Exception as e:
        print("Error 1:" + str(e))
    return []
