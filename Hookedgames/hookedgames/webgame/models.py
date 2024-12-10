import cx_Oracle


class Peticion:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

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

    def select(self,email):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT USER_PASSWORD FROM CLIEN WHERE CORREO=:P1"
            cursor.execute(consulta, (email,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor.fetchall()

    def selectempl(self,user):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT USER_PASSWORD FROM EMPLEADOS WHERE idEmpleado=:P1"
            cursor.execute(consulta, (user,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor.fetchall()

    def selectproduct(self,idg):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM GAMES WHERE idGame=:P1"
            cursor.execute(consulta, (idg,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor.fetchall()

    def uploadcata(self):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM GAMES"
            cursor.execute(consulta)
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor


    def selectclient(self,email):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT * FROM CLIENT WHERE CORREO=:P1"
            cursor.execute(consulta, (email,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor