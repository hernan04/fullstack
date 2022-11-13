import mysql.connector


class Conectar():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                db='portal'

            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!", descripcionError)

    def ListarArtistas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                senteciaSQL = "SELECT id_artista, artista.nombre_apellido, artista.mail, artista.insta, artista.face, categoria.nombre, categoria.subcategoria, categoria.descripcion FROM artista INNER JOIN categoria ON artista.id_categoria = categoria.id_categoria"
                cursor.execute(senteciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!", descripcionError)

    def ListarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from usuario"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                # self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!", descripcionError)

    def ListarPedidos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from pedido"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                # self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!", descripcionError)

    def ListarCategoria(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from categoria"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                return resultados
            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!", descripcionError)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    def InsertarArtista(self, artista):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "insert into artista values (null,%s,%s,%s,%s,%s,%s,%s,%s);"
                data = (
                    artista.getNombre_apellido(),
                    artista.getTelefono(),
                    artista.getMail(),
                    artista.getFace(),
                    artista.getInsta(),
                    artista.getId_usuario(),
                    artista.getId_categoria(),
                    artista.getId_pedido(),)

                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()
                print("Artista insertado correctamente")
            except mysql.connector.Error as d_Error:
                print("¡Ops, algo salió mal!", d_Error)


# -------------------------------------------------------------------------------------------------------------------
# ELIMINAR ARTISTA

    def EliminarArtista(self, id_artista):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from artista WHERE id_artista = %s "
                data =(id_artista,)
                cursor.execute(sentenciaSQL,data)
                self.conexion.commit()
                self.conexion.close()
                print("Artista eliminado correctamente")
            except mysql.connector.Error as d_Error:
                print("No se conectó", d_Error)
#----------------------------------------------------------------------------------------------------------------------
# EDITAR ARTISTA

    def EditarArtista(self,artista,id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "UPDATE artista SET id_artista = %s, nombre_apellido= %s, telefono = %s, mail = %s, insta = %s, face = %s, id_categoria = %s, id_pedido = %s, id_usuario = %s WHERE id_artista ="+str(id)

                data = (
                  artista.getId_artista(),
                  artista.getNombre_apellido(),
                  artista.getTelefono(),
                  artista.getMail(),
                  artista.getInsta(),
                  artista.getFace(),
                  artista.getId_categoria(),
                  artista.getId_pedido(),
                  artista.getId_usuario())

                cursor.execute(sentenciaSQL,data)

                self.conexion.commit()
                self.conexion.close()
                print("Artista editado correctamente")        

            except mysql.connector.Error as d_Error:
                                print("¡Ops, algo salió mal! No se conectó a la base de datos", d_Error)

# -------------Clase Artista-----------------------------------------------------------------------------------------
class Artista():
    def __init__(self, id_artista, nombre_apellido, telefono, mail, face, insta, id_usuario, id_categoria, id_pedido) -> None:
        self.id_artista = id_artista
        self.nombre_apellido = nombre_apellido
        self.telefono = telefono
        self.mail = mail
        self.face = face
        self.insta = insta
        self.id_usuario = id_usuario
        self.id_categoria = id_categoria
        self.id_pedido = id_pedido

    def getId_artista(self):
        return self.id_artista

    def getNombre_apellido(self):
        return self.nombre_apellido

    def getTelefono(self):
        return self.telefono

    def getId_mail(self):
        return self.mail

    def getFace(self):
        return self.face

    def getId_insta(self):
        return self.insta

    def getId_usuario(self):
        return self.id_usuario

    def getId_categoria(self):
        return self.id_categoria

    def getId_pedido(self):
        return self.id_pedido

    def setId_artista(self, id_artista):
        self.id_artista = id_artista

    def setNombre_apellido(self, nombre_apellido):
        self.nombre_apellido = nombre_apellido

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setmail(self, mail):
        self.mail = mail

    def setFace(self, face):
        self.face = face

    def setId_insta(self, insta):
        self.insta = insta

    def setId_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def setId_categoria(self, id_categoria):
        self.id_categoria = id_categoria

    def setId_pedido(self, id_pedido):
        self.id_pedido = id_pedido


def __str__(self) -> str:
    return str(self.id_artista) + ' ' + str(self.nombre_apellido) + ' ' + self.telefono + ' ' + str(self.mail) + ' ' + str(self.face) + ' ' + str(self.insta) + ' ' + str(self.id_usuario) + ' ' + str(self.id_categoria) + ' ' + self.id_pedido


class Usuario():
    def __init__(self, id_usuario, nombre_apellido, mail, telefono, id_pedido) -> None:
        self.id_usuario = id_usuario
        self.nombre_apellido = nombre_apellido
        self.mail = mail
        self.telefono = telefono
        self.id_pedido = id_pedido

    def getId_usuario(self):
        return self.id_usuario

    def getNombre_apellido(self):
        return self.nombre_apellido

    def getMail(self):
        return self.mail

    def getTelefono(self):
        return self.telefono

    def getId_pedido(self):
        return self.id_pedido

    def setId_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def setNombre(self, nombre_apellido):
        self.nombre_apellido = nombre_apellido

    def setMail(self, mail):
        self.mail = mail

    def setTelefono(self, telefono):
        self.telefono = telefono

    def setId_pedido(self, id_pedido):
        self.id_pedido = id_pedido


def __str__(self) -> str:
    return str(self.id_usuario) + ' ' + str(self.nombre_apellido) + ' ' + str(self.mail) + ' ' + self.telefono + ' ' + str(self.id_pedido)


class Categoria():
    def __init__(self, id_categoria, nombre) -> None:
        self.id_categoria = id_categoria
        self.nombre = nombre

    def __str__(self) -> str:
        return str(self.id_categoria)+' '+self.nombre

    def getId_categoria(self):
        return self.id_categoria

    def getNombre(self):
        return self.nombre

    def setId_categoria(self, id_categoria):
        self.id_categoria = id_categoria

    def setNombre(self, nombre):
        self.nombre = nombre


class Pedido():
    def __init__(self, id_pedido, detalle, entrega, medio_pago, fecha) -> None:
        self.id_pedido = id_pedido
        self.detalle = detalle
        self.entrega = entrega
        self.medio_pago = medio_pago
        self.fecha = fecha

    def __str__(self) -> str:
        return str(self.id_pedido) + ' ' + str(self.detalle) + ' ' + str(self.entrega) + ' ' + str(self.medio_pago) + ' ' + str(self.fecha)

    def getId_pedido(self):
        return self.id_pedido

    def getDetalle(self):
        return self.detalle

    def getEntrega(self):
        return self.entrega

    def getMedio_pago(self):
        return self.medio_pago

    def getFecha(self):
        return self.fecha

    def setId_pedido(self, id_pedido):
        self.id_pedido = id_pedido

    def setDetalle(self, detalle):
        self.pedido = detalle

    def setEntrega(self, entrega):
        self.entrega = entrega

    def setMedio_pago(self, medio_pago):
        self.medio_pago = medio_pago

    def setFecha(self, fecha):
        self.fecha = fecha
