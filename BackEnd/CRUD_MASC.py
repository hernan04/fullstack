# CRUD

import mysql.connector

class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'portal'

            )
        except mysql.connector.Error as descripcionError:
            print("¡No se pudo conectar!",descripcionError)

# CREATE

    def InsertarValor(self,nombre_apellido, mail):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "INSERT INTO artista VALUES(%s,%s)"
                data= (nombre_apellido, mail)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")
   

# READ

    def BuscarObjeto(self, nombre_apellido):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "SELECT * from artista where nombre_apellido like %s "
                
                cursor.execute(sentenciaSQL)
                resultadoREAD = cursor.fetchall()
                self.conexion.close()
               
                return resultadoREAD

            except:
                print("No se pudo concectar a la base de datos")


# UPDATE

    def ActualizarValor(self,nombre_apellido):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "UPDATE INTO artista VALUES (%s)"
                data= (nombre_apellido)

                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print("No se pudo concectar a la base de datos")


# DELETE

    def EliminarObjeto(self, ID):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from artista where id = ID"
                cursor.execute(sentenciaSQL)

                self.conexion.commit()                
                self.conexion.close()
           
            except:
                print("No se pudo concectar a la base de datos")