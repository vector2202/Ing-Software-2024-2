from datetime import datetime
import pymysql
import random
import string
import os
def connectDB():
    connection = pymysql.connect(host='localhost',
                               user='usuario',
                               password='contraseña',
                               database='basededatos')
    return connection

#Inserte 1 registro en cada tabla
def insertRandom(connection):
    insertUserRandom(connection)
    insertMoviesRandom(connection)
    insertRentRandom(connection)
def insertUserRandom(connection):
    try:
        with connection.cursor() as cursor:
            name = generateRandomString(random.randint(2,16))
            apPat = generateRandomString(random.randint(2,12))
            apMat = generateRandomString(random.randint(2,12))
            password = generateRandomString(random.randint(8,64))
            email = generateRandomString(random.randint(4,16)) + '@' + generateRandomString(random.randint(5, 10)) + '.com'
            profile = os.urandom(100)
            superUser = random.choice([True, False])
            sql = "INSERT INTO personas (nombre, apPat, apMat, password, email, profilePicture, superUser) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (name, apPat, apMat, password, email, profile, superUser)
            cursor.execute(sql, values)
        connection.commit()
        print("Datos insertados correctamente.")
    except Exception as e:
        print(e)
    connection.close()
    
def insertMoviesRandom(connection):
    try:
        with connection.cursor() as cursor:
            name = generateRandomString(random.randint(2,200))
            genero = generateRandomString(random.randint(2,45))
            duracion = random.randint(60,200)
            inventario = random.randint(1, 10)
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            values = (name, genero, duracion, inventario)
            cursor.execute(sql, values)
        connection.commit()
        print("Datos insertados correctamente.")
    except Exception as e:
        print(e)
    connection.close()
    
def insertRentRandom(connection):
    try:
        with connection.cursor() as cursor:
            id_user = get_id(connection, "idUsuario", "usuarios")
            id_movie = get_id(connection, "idPelicula", "peliculas")
            days = random.randint(2,7)
            status = random.choice([True, False])
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            values = (id_user, id_movie, datetime.today(), days, status)
            cursor.execute(sql, values)
        connection.commit()
        print("Datos insertados correctamente.")
    except Exception as e:
        print(e)
    connection.close()

def select(table, connection):
    try:
        tableData = []
        query = f"SELECT * FROM {table}"
        with connection.cursor() as cursor:
            cursor.execute(query)
            content = cursor.fetchall()
            for data in content:
                tableData.append(data)
        return tableData
    except Exception as e:
        print(f"Error: {e}")

def get_id(connection, id_name, table):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT {id_name} FROM {table}")
        ids = [fila[f"{id_name}"] for fila in cursor.fetchall()]
        if ids:
            return random.choice(ids)    
    return None
def generateRandomString(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

#Ejercicio 2
def filterUsers(_filter, connection):
    try:
        users = []
        query = f"SELECT * FROM usuarios WHERE apMat REGEXP %s OR apPat REGEXP %s"
        with connection.cursor() as cursor:
            cursor.execute(query, (_filter, _filter))
            content = cursor.fetchall()
            for data in content:
                users.append(data)
        return users
    except Exception as e:
        print(f"Error: {e}")

def insert(datos, tabla, connection):
    try:
        query = f"INSERT INTO {tabla} {datos} VALUES"
        with connection.cursor() as cursor:
            cursor.exectute(query)
        connection.commit()
        return True
    except Exception as e: 
        print(f"Error: {e}")
        return False
#Ejercicio 3
def updateMovie(name, genre, connection):
    try:
        name = name.lower()
        query = f"UPDATE peliculas SET genero = {genre} WHERE nombre={name}"
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.commit()
        return True
    except Exception as e: 
        print(f"Error: {e}")
        return False

#Ejercicio 4
def supressRents(connection, fecha):
    try:
        #Obtener el corte de fecha
        query = f"DELETE FROM rentar WHERE fecha_renta < {fecha}"
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.commit()
        return True
    except Exception as e: 
        print(f"Error: {e}")
        return False
def main():
    connection = connectDB()
    insertRandom(connection)
