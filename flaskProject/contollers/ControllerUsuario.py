from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint

from alchemyClasses import db
from modelos.Modelo_Usuario import agregar_usuario
from modelos.Modelo_Usuario import eliminar_usuario
from modelos.Modelo_Usuario import modificar_usuario
from modelos.Modelo_Usuario import obtener_usuario
from modelos.Modelo_Usuario import obtener_usuarios

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/usuarios') #localhost:5000/usuario/
def ver_usuarios():
    return render_template('/usuarios/usuarios.html', data=obtener_usuarios())

#responde a localhost:5000/usuario/id/1
@usuario_blueprint.route('/usuarios/id/<int:idUsuario>') #<tipo:nombre_variable>
def ver_usuario_id(idUsuario):
    data = obtener_usuario(idUsuario)
    if data == None:
        return redirect(url_for("usuario.ver_usuarios"))
    return render_template('/usuarios/usuario.html', data=data)

@usuario_blueprint.route('/usuarios/agregar', methods=['GET', 'POST'])
def agregar_usuarios():
    if request.method == 'GET':
        return render_template('usuarios/agregar_usuario.html', data=None)
    else:
        if agregar_usuario(request.form):
            return redirect(url_for('usuario.ver_usuarios'))
        return render_template('usuarios/agregar_usuario.html', data=request.form)
    
@usuario_blueprint.route('/usuarios/eliminar/<int:idUsuario>', methods=['GET', 'POST'])
def eliminar_usuarios(idUsuario):
    if eliminar_usuario(idUsuario):
        return redirect(url_for("usuario.ver_usuarios"))
    else:
        return redirect(url_for("usuario.ver_usuario", idUsuario=idUsuario))
    
@usuario_blueprint.route('/usuarios/modificar/<int:idUsuario>', methods=['GET', 'POST'])
def modificar_usuarios(idUsuario):    
    if request.method == "GET":
        data = obtener_usuario(idUsuario)
        if data == None:
            return redirect(url_for("usuario.ver_usuarios"))
        return render_template('/usuarios/modificar_usuario.html', data=data)
    else:
        modificar_usuario(request.form, id_usuario=idUsuario)
        return redirect(url_for("usuario.ver_usuarios"))
        
