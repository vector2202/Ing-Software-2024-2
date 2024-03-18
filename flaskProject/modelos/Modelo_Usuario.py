from sqlalchemy import delete
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Renta import Renta
from alchemyClasses import db
from flask import flash

def agregar_usuario(data):
    nombre = data.get("nombre")
    ap_pat = data.get("ap_pat")
    ap_mat = data.get("ap_mat")
    password = data.get("psswd")
    email = data.get("email")
    super_user = data.get("super_user")
    usuario = Usuario(nombre, ap_pat, ap_mat, password, email, None, super_user)
    db.session.add(usuario)
    db.session.commit()
    
def modificar_usuario(data):
    id_usuario = data.get("id_usuario")
    nombre = data.get("nombre")
    ap_pat = data.get("ap_pat")
    ap_mat = data.get("ap_mat")
    password = data.get("psswd")
    email = data.get("email")
    super_user = data.get("super_user")
    
    usuario = Usuario.query.get(id_usuario)
    usuario.nombre = nombre
    usuario.ap_pat = ap_pat
    usuario.ap_mat = ap_mat
    usuario.password = password
    usuario.email = email
    usuario.super_user = super_user
    
    db.session.commit()
    return True
    
def eliminar_usuario(id_usuario):
    renta = Renta.query.filter_by(id_usuario).delete()
    usuario = Usuario.query.filter_by(id_usuario).first()
    db.session.delete(usuario)
    db.session.commit()

def obtener_usuario(id_usuario):
    data = Usuario.query.get(id_usuario)
    return data
    

def obtener_usuarios():
    data = Usuario.query.all()
    return data
