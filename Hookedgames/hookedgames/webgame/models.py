import cx_Oracle


class Peticion:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

# Inserta un cliente nuevo
    def insert(self,datos):
        registro = 0
        cursor = self.connection.cursor()
        try:
            consulta = "INSERT INTO CLIENTES VALUES (:P1, :P2, :P3, :P4, :P5, :P6, :P7)"
            cursor.execute(consulta, datos)

            registro = cursor.rowcount

            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return registro

# Devuelve la contraseña si el usuario existe
    def select(self,email):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT USER_PASSWORD FROM CLIEN WHERE CORREO=:P1"
            cursor.execute(consulta, (email,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor.fetchall()

# Devuelve la contraseña si el empleado existe
    def selectempl(self,user):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT USER_PASSWORD FROM EMPLEADOS WHERE idEmpleado=:P1"
            cursor.execute(consulta, (user,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor.fetchall()

# Devuelve la info de un juego concreto para añadir al carro de compra
    def selectproduct(self,idg):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM GAMES WHERE idGame=:P1"
            cursor.execute(consulta, (idg,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor.fetchall()

# Devuelve el catálogo completo de juegos
    def uploadcata(self):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM GAMES"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

# Devuelve la tabla completa de ventas
    def selectventas(self):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM VENTAS"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

# Devuelve la info del cliente con sesion abierta para mostarsela
    def selectclient(self,email):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM CLIENT WHERE CORREO=:P1"
            cursor.execute(consulta, (email,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def select_stock(self, titulo):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM GAMES WHERE TITULO=:P1"
            cursor.execute(consulta, (titulo,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

    def modificardatos(self, datos):
        registro = 0
        cursor = self.connection.cursor()
        try:
            consulta = "UPDATE GAMES SET CANTIDAD = :P1 WHERE IDSTOCK = :P2"
            cursor.execute(consulta, datos)
            registro = cursor.rowcount
            self.connection.commit()
        except self.connection.Error as error:
            print("Error: ", error)

        return registro

    def mostrar_stock_completo(self, ):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM GAMES"
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
