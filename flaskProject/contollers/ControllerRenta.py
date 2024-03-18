from flask import Blueprint, request, render_template, flash, url_for
from random import randint
from alchemyClasses import Renta

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/') #localhost:5000/renta/
def ver_rentas():
    return "select * from renta"

#responde a localhost:5000/renta/id/1
@renta_blueprint.route('/id/<int:id_renta>/<string:nombre>') #<tipo:nombre_variable>
def ver_renta_id(id_renta, nombre):
    return f"select * from renta where {id_renta} == id_renta"
#return f"Se hace el query con el id {id_renta} y el nombre {nombre}"


@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        #Obtengo la información del método post.
        id_usuario = request.form['id_usuario']
        id_pelicula = request.form['id_pelicula']
        fecha = request.form['fecha']
        dias_renta = request.form['dias_renta']
        estatus = request.form['estatus']
        id_renta = request.form['id_renta']
        
        #Creo mi renta.
        renta = Renta(id_usuario, id_pelicula, fecha, dias_renta, estatus)
        
        #Lo guardo en la DB
        #url_for
        #flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('renta.agregar_renta')
        # Y regreso al flujo que me hayan especificado.
        return render_template('renta_added.html', name="Renta", num_cta=id_renta)
