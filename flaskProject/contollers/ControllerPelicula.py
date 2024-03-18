from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import Pelicula
from alchemyClasses import db

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/') #localhost:5000/pelicula/
def ver_peliculas():
    return render_template('/pelicula/peliculas.html', data=obtener_peliculas())
    

#responde a localhost:5000/pelicula/id/1
@pelicula_blueprint.route('/id/<int:id_pelicula>') #<tipo:nombre_variable>
def ver_pelicula_id(id_pelicula):
    data = obtener_pelicula(id_pelicula)
    if data == None:
        return redirect(url_for("pelicula.ver_peliculas"))
    return render_template('/pelicula/peliculas.html', data)

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('add_user.html')
    else:
        #Obtengo la información del método post.
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        id_pelicula = request.form['id_pelicula']
        #Creo mi pelicula.
        pelicula = Pelicula(nombre,genero, duracion, inventario)
        
        #Lo guardo en la DB
        #url_for
        #flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('pelicula.agregar_pelicula')
        # Y regreso al flujo que me hayan especificado.
        return render_template('pelicula_added.html', name=nombre, num_cta=id_pelicula)
    
@pelicula_blueprint.route('/eliminar', methods=['GET', 'POST'])
def eliminar_pelicula():
    id_pelicula = obtener_pelicula(request.args.get("id_pelicula"))
    if Modelo_Pelicula.eliminar_pelicula(id_pelicula):
        return redirect(url_for("pelicula.ver_peliculas"))
    else:
        return redirect(url_for("pelicula.ver_pelicula"), id_pelicula)
@pelicula_blueprint.route('/eliminar', methods=['GET', 'POST'])
def modificar_pelicula():    
    if request.method == "GET":
        data = obtener_pelicula(request.args.get("id_pelicula"))
        if data == None:
            return redirect(url_for("pelicula.ver_peliculas"))
        return render_template('/pelicula/modificar_pelicula.html', data)
    else:
        id_pelicula = request.form.get("id_pelicula")
        Modelo_Pelicula(requets.form)
        return redirect(url_for("pelicula.ver_peliculas"), id_pelicula)
        
    

