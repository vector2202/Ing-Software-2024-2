from sqlalchemy import delete
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from alchemyClasses import db
from flask import flash


def agregar_pelicula(data):
    try:
        nombre = data.get("nombre")
        genero = data.get("genero")
        duracion = data.get("duracion")
        #None duracion
        inventario = data.get("inventario")
        pelicula = Pelicula(nombre, genero, duracion, inventario)
        db.session.add(pelicula)
        db.session.commit()
        return True
    except Exception as e:
        print("Error" + str(e))
    
    
def modificar_pelicula(data, id_pelicula):
    print("ID:", id_pelicula)
    nombre = data.get("nombre")
    genero = data.get("genero")
    duracion = data.get("duracion")
    #None duracion
    inventario = data.get("inventario")
    print(data)
    
    pelicula = Pelicula.query.get(id_pelicula)
    pelicula.nombre = nombre
    pelicula.genero = genero
    pelicula.duracion = duracion
    pelicula.inventario = inventario
    
    db.session.commit()
    
def eliminar_pelicula(id_pelicula):
     #renta = Renta.query.filter_by(id_pelicula=id_pelicula).first()
    pelicula = Pelicula.query.filter_by(idPelicula=id_pelicula).first()
    #print("Renta", renta)
    #if renta != None:
    #    db.session.delete(renta)
    db.session.delete(pelicula)
    db.session.commit()
    return True

def obtener_pelicula(id_pelicula):
    data = Pelicula.query.get(id_pelicula)
    return data
    

def obtener_peliculas():
    try:
        data = Pelicula.query.all()
        print("Data", data)
        return data
    except Exception as e:
        print("Error 1:" + str(e))
    return []
