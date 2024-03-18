from flask import Blueprint, request, render_template, flash, url_for
from random import randint
from alchemyClasses import Usuario

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/') #localhost:5000/usuario/
def ver_usuarios():
    return "select * from usuario"

#responde a localhost:5000/usuario/id/1
@usuario_blueprint.route('/id/<int:id_usuario>/<string:nombre>') #<tipo:nombre_variable>
def ver_usuario_id(id_usuario, nombre):
    return f"select * from usuario where {id_usuario} == id_usuario"
#return f"Se hace el query con el id {id_usuario} y el nombre {nombre}"


@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        #Obtengo la información del método post.
        nombre = request.form['nombre']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        passwd = request.form['passwd']
        email = request.form['email']
        profile_picture = request.form['profile']
        id_usuario = request.form['id_usuario']
        super_user = request.form['super']
        #Creo mi usuario.
        usuario = Usuario(nombre, ap_pat, ap_mat, passwd, email, profile_picture, super_user)
        
        #Lo guardo en la DB
        #url_for
        #flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('usuario.agregar_usuario')
        # Y regreso al flujo que me hayan especificado.
        return render_template('user_added.html', name=nombre, num_cta=id_usuario)
