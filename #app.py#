from datetime import datetime
from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256

from model.model_usuario import borra_usuario
from model.model_pelicula import borra_pelicula
from model.model_renta import borra_renta

#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
def show(table:int) -> None:
    if table == 1:
        for user in Usuario.query.all():
            print(user)
    elif table == 2:
        for movie in Pelicula.query.all():
            print(movie)
    elif table == 3:
        for rent in Renta.query.all():
            print(rent)

def search_id(table:int, id_param:int)->None:
    if table == 1:
        for user in Usuario.query.filter(and_(Usuario.id_usuario == id_param)):
            print(f"Usuario con id {id_param} es: {user.__str__()}")
    elif table == 2:
        for movie in Pelicula.query.filter(and_(Usuario.id_usuario == id_param)):
            print(f"Pelicula con id {id_param} es: {movie.__str__()}")
    else:
        for rent in Renta.query.filter(and_(Usuario.id_usuario == id_param)):
            print(f"Renta con {id_param} es: {rent.__str__()}")

def update(table:int, _id:int, new_name=None) -> None:
    if table == 1:
        entity = Usuario.query.filter(Usuario.id_usuario == _id).first()
        entity.nombre = new_name        
    elif table == 2:
        entity = Pelicula.query.filter(Pelicula.id_pelicula == _id).first()
        entity.nombre = new_name
    else:
        entity = Renta.query.filter(Renta.id_rentar == _id).first()
        entity.fecha = datetime.today()
    db.session.commit()
    
def drop(table:int, _id=None) -> None:
    if table == 1:
        if _id == None:
            registers = db.session.query(Usuario).all()
            for register in registers:
                registersRent = db.session.query(Renta).filter_by(Renta.id_usuario == register.id_usuario).all()
                for registerRent in registersRent:
                    db.session.delete(registerRent)
                db.session.delete(register)
        else: 
            borra_usuario(_id)
            registersRent = db.session.query(Renta).filter_by(Renta.id_usuario == _id).all()
            for registerRent in registersRent:
                db.session.delete(registerRent)
                print("Borrado con éxito!")
    elif table == 2:
        if _id == None:
            registers = db.session.query(Pelicula).all()
            for register in registers:
                registersRent = db.session.query(Renta).filter_by(Renta.id_pelicula == register.id_pelicula).all()
                for registerRent in registersRent:
                    db.session.delete(registerRent)
                db.session.delete(register)
        else: 
            borra_pelicula(_id)
            registersRent = db.session.query(Renta).filter_by(Renta.id_pelicula == _id).all()
            for registerRent in registersRent:
                db.session.delete(registerRent)
            print("Borrado con éxito!")
    else:
        if _id == None:
            registers = db.session.query(Renta).all()
            for register in registers:
                db.session.delete(register)
        else: 
            borra_renta(_id)
            print("Borrado con éxito!")
    db.session.commit()
    
if __name__ == '__main__':
    with app.app_context():
        _input = 0
        while(_input < 4):
            try:
                _input = int(input("1. Ver registros\n2. Filtrar por ID\n3. Actualizar\n4. Eliminar\n5.Salir"))
                if _input == 1:
                    print("Seleccione la tabla:")
                    _input = int(input("1. Usuario\n2. Pelicula\n3. Renta\n"))
                    show(_input)
                elif _input == 2:
                    print("Seleccione la tabla:")
                    _input = int(input("1. Usuario\n2. Pelicula\n3. Renta\n"))
                    _id = int(input("Ingrese el id"))
                    search_id(_input, _id)
                elif _input == 3:
                    print("Seleccione la tabla:")
                    _input = int(input("1. Usuario\n2. Pelicula\n3. Renta\n"))
                    _id = int(input("Ingrese el id"))
                    if _input == 1 or _input == 2:
                        new_name = input("Ingrese nuevo nombre: ")
                        update(_input, _id, new_name)
                    elif _input == 3:
                        update(_input, _id)
                elif _input == 4:
                    print("Seleccione la tabla:")
                    _input = int(input("1. Usuario\n2. Pelicula\n3. Renta\n"))
                    _id = input("Ingrese el id (-1 para toda la tabla): ")
                    if _id == -1:
                        drop(_input)
                    else:
                        drop(_input, _id)
                else:
                    print("Opcion no valida, Saliendo")
            except Exception as e:
                print(e)
                _input = 0
#Create
"""valeria = Alumno('Valeria', 'Ramirez', 319311918, apMat=None, password=sha256(cipher("Developer123#")).hexdigest())
db.session.add(valeria)
db.session.commit()"""
