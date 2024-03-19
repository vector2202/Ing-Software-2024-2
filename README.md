# Ingeniería de Software 2024-2
Repositorio oficial de la materia de Ingenieria de Software de la Facultad de Ciencias de la UNAM del semestre 2024-2

## Profesores:

- Francisco Valdes Souto
- Valeria Garcia Landa
- Fernando Fong
- Erick Martínez Piza
- Adriana Hernandez Gasca


Para ejecutar el codigo primero hay que tener instalado mysql o una variacion, en mi caso use mariadb
Primero la inicializamos:
```
sudo systemctl start mariadb.service
```

Despues de esto deberemos colocarnos en el directorio FlaskProject y ejecutamos

```
sudo mariadb -u root -p
```
E ingresamos nuestra contraseña

Ahora nos va a abrir el entorno de maria, por lo que ejecutando:
```
source ./IngSoftLab.sql;
```
De esta manera cargamos nuestra base de datos en maria, en otra terminal, en el mismo directorio, ejecutamos
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
Una vez con eso abrimos el puerto que nos dice la terminal y ya
