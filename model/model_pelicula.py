from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db

def borra_pelicula(id_pelicula):
    pelicula = Pelicula.query.filter(Pelicula.id_pelicula == id_pelicula).first()
    db.session.delete(pelicula)
    db.session.commit()

