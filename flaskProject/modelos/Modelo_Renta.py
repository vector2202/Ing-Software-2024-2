from sqlalchemy import delete
from alchemyClasses.Renta import Renta
from alchemyClasses import db
from flask import flash

def agregar_renta(data):
    id_renta = data.get("id_renta")
    id_pelicula = data.get("id_pelicula")
    fecha_renta = data.get("fecha_renta")
    dias_renta = data.get("dias_renta")
    estatus = data.get("estatus")

    renta = Renta(id_renta, id_pelicula, fecha_renta, dias_renta, estatus)
    db.session.add(renta)
    db.session.commit()
    
def modificar_renta(id_renta):
    renta = Renta.query.get(id_renta)
    renta.estatus = not renta.estatus
    db.session.commit()

def obtener_renta(id_renta):
    data = Renta.query.get(id_renta)
    return data    

def obtener_rentas():
    data = Renta.query.all()
    return data
