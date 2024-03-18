from sqlalchemy import delete
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from alchemyClasses import db
from flask import flash


def agregar_pelicula(data):
    nombre = data.get("nombre")
    genero = data.get("genero")
    duracion = data.get("duracion")
    #None duracion
    inventario = data.get("inventario")
    pelicula = Pelicula(nombre, genero, duracion, inventario)
    db.session.add(pelicula)
    db.session.commit()
    
def modificar_pelicula(data):
    id_pelicula = data.get("id_pelicula")
    nombre = data.get("nombre")
    genero = data.get("genero")
    duracion = data.get("duracion")
    #None duracion
    inventario = data.get("inventario")
    
    pelicula = Pelicula.query.get(id_pelicula)
    pelicula.nombre = nombre
    pelicula.genero = genero
    pelicula.duracion = duracion
    pelicula.inventario = inventario
    
    db.session.commit()
    return True
    
def eliminar_pelicula(id_pelicula):
    renta = Renta.query.filter_by(id_pelicula).delete()
    pelicula = Pelicula.query.filter_by(id_pelicula).first()
    db.session.delete(pelicula)
    db.session.commit()

def obtener_pelicula(id_pelicula):
    data = Pelicula.query.get(id_pelicula)
    return data
    

def obtener_peliculas():
    data = Pelicula.query.all()
    return data
