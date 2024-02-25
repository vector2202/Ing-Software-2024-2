from alchemyClasses.Renta import Renta
from alchemyClasses import db

def borra_renta(id_renta):
    renta = Renta.query.filter(Renta.id_rentar == id_renta).first()
    db.session.delete(renta)
    db.session.commit()

