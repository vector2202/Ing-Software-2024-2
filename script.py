import pymysql

def connectDB():
    connection = pymysql.connect(host='localhost',
                               user='usuario',
                               password='contraseña',
                               database='basededatos')
    return connection

#Inserte 1 registro en cada tabla
def insertRandom(connection):
    insertUserRandom()
    insertMoviesRandom()
    insertRentRandom()
def insertUserRandom():
    pass
def insertMoviesRandom():
    pass
def insertRentRandom():
    pass


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


#Ejercicio 2
def filterUsers(filter, connection):
    try:
        users = []
        query = f"SELECT * FROM usuarios WHERE apellido=Torres"
        with connection.cursor() as cursor:
            cursor.execute(query)
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
        query = f"UPDATE peliculas set genero = {genre} WHERE nombre={name}"
        with connection.cursor() as cursor:
            cursor.execute(query)
        connection.commit()
        return True
    except Exception as e: 
        print(f"Error: {e}")
        return False

#Ejercicio 4
def supressRents(connection):
    try:
        #Obtener el corte de fecha
        query = f"DELETE FROM rentar WHERE fecha_renta < algo"
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
