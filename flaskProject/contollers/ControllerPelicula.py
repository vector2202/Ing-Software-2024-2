from flask import Blueprint, request, render_template, url_for, redirect
from random import randint

from alchemyClasses import db

from modelos.Modelo_Pelicula import obtener_pelicula
from modelos.Modelo_Pelicula import obtener_peliculas
from modelos.Modelo_Pelicula import agregar_pelicula
from modelos.Modelo_Pelicula import eliminar_pelicula
from modelos.Modelo_Pelicula import modificar_pelicula

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/peliculas') #localhost:5000/pelicula/
def ver_peliculas():
    return render_template('/peliculas/peliculas.html', data=obtener_peliculas())

#responde a localhost:5000/pelicula/id/1
@pelicula_blueprint.route('/peliculas/id/<int:idPelicula>') #<tipo:nombre_variable>
def ver_pelicula_id(idPelicula):
    data = obtener_pelicula(idPelicula)
    if data == None:
        return redirect(url_for("pelicula.ver_peliculas"))
    return render_template('/peliculas/pelicula.html', data=data)

@pelicula_blueprint.route('/peliculas/agregar', methods=['GET', 'POST'])
def agregar_peliculas():
    if request.method == 'GET':
        return render_template('peliculas/agregar_pelicula.html', data=None)
    else:
        if agregar_pelicula(request.form):
            return redirect(url_for('pelicula.ver_peliculas'))
        return render_template('peliculas/agregar_pelicula.html', data=request.form)
    
@pelicula_blueprint.route('/peliculas/eliminar/<int:idPelicula>', methods=['GET', 'POST'])
def eliminar_peliculas(idPelicula):
    if eliminar_pelicula(idPelicula):
        return redirect(url_for("pelicula.ver_peliculas"))
    else:
        return redirect(url_for("pelicula.ver_pelicula", id_pelicula=idPelicula))
    
@pelicula_blueprint.route('/peliculas/modificar/<int:idPelicula>', methods=['GET', 'POST'])
def modificar_peliculas(idPelicula):
    if request.method == "GET":
        data = obtener_pelicula(idPelicula)
        if data == None:
            return redirect(url_for("pelicula.ver_peliculas"))
        return render_template('/peliculas/modificar_pelicula.html', data=data)
    else:
        modificar_pelicula(request.form, id_pelicula=idPelicula)
        return redirect(url_for("pelicula.ver_peliculas"))
