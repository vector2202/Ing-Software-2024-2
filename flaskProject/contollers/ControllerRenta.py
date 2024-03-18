from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint

from modelos.Modelo_Renta import agregar_renta
from modelos.Modelo_Renta import modificar_renta
from modelos.Modelo_Renta import obtener_renta
from modelos.Modelo_Renta import obtener_rentas

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/rentas') #localhost:5000/renta/
def ver_rentas():
    return render_template('/rentas/rentas.html', data=obtener_rentas())

#responde a localhost:5000/renta/id/1
@renta_blueprint.route('/rentas/id/<int:id_renta>') #<tipo:nombre_variable>
def ver_renta_id(id_renta):
    data = obtener_renta(id_renta)
    if data == None:
        return redirect(url_for("renta.ver_rentas"))
    return render_template('/rentas/renta.html', data=data)


@renta_blueprint.route('/rentas/agregar', methods=['GET', 'POST'])
def agregar_rentas():
    if request.method == 'GET':
        return render_template('rentas/agregar_renta.html', data=None)
    else:
        if agregar_renta(request.form):
            return redirect(url_for('renta.ver_rentas'))
        return render_template('rentas/agregar_renta.html', data=request.form)

@renta_blueprint.route('/rentas/modificar/<int:idRenta>', methods=['GET', 'POST'])
def modificar_rentas(idRenta):
    if request.method == 'POST':
        modificar_renta(idRenta)
    return redirect(url_for("renta.ver_renta_id", id_renta=idRenta))

            
