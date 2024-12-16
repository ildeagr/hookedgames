import cx_Oracle


class Peticion:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

# Inserta un cliente nuevo
    def insert(self,datos):
        registro = 0
        cursor = self.connection.cursor()
        try:
            consulta = "INSERT INTO CLIEN VALUES (:P1, :P2, :P3, :P4, :P5, :P6)"
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
            consulta = "SELECT DNI, USER_PASSWORD FROM CLIEN WHERE CORREO=:P1"
            cursor.execute(consulta, (email,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor.fetchall()

# Devuelve la contraseña si el empleado existe
    def selectempl(self,user):
        cursor = self.connection.cursor()
        try:
            consulta = "SELECT EMP_PASSWORD FROM EMPLEADOS WHERE idEmpleado=:P1"
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

# Devuelve el stock del titulo indicado
    def select_stock(self, titulo):
        cursor = self.connection.cursor()
        try:
            consulta = "select games.idgame, games.titulo ,games.plataforma, games.precio, stock.cantidad from games inner join stock on games.idgame = stock.idgame where games.titulo = :P1"
            cursor.execute(consulta, (titulo,))

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

# Modifica el stock
    def modificardatos(self, datos):
        registro = 0
        cursor = self.connection.cursor()
        try:
            consulta = "UPDATE STOCK SET CANTIDAD = :P1 WHERE IDSTOCK = :P2"
            cursor.execute(consulta, datos)
            registro = cursor.rowcount
            self.connection.commit()
        except self.connection.Error as error:
            print("Error: ", error)

        return registro

# Muestra el stock completo
    def mostrar_stock_completo(self, ):
        cursor = self.connection.cursor()
        try:
            consulta = "select stock.idstock, stock.cantidad, stock.precio, stock.sede, games.titulo from stock inner join games on stock.idgame = games.idgame"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor

# Trae la informacion de los elementos del carrito
    def selectcarro(self, datos):
        cursor = self.connection.cursor()
        try:
            consulta = "select * from games where idgame IN("+datos+")"
            cursor.execute(consulta)

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor.fetchall()

# Inserta un nuevo empleado
    def alta_empleado(self, emp_id, nombre,passw, puesto, sede):
        rowcount = 0
        cursor = self.connection.cursor()
        try:
            rowcount = cursor.var(cx_Oracle.NUMBER)
            cursor.callproc("ALTA_BAJA_MODI_HK.alta_HK", (emp_id, nombre, passw, puesto, sede,rowcount))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return rowcount

# Borra un empleado
    def baja_empleado(self, emp_id):
        rowcount = 0
        cursor = self.connection.cursor()
        try:
            rowcount = cursor.var(cx_Oracle.NUMBER)
            cursor.callproc("ALTA_BAJA_MODI_HK.baja_HK", (emp_id,))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return rowcount

# Modifica un empleado
    def modi_empleado(self, emp_id, nombre,passw, puesto, sede):
        rowcount = 0
        cursor = self.connection.cursor()
        try:
            rowcount = cursor.var(cx_Oracle.NUMBER)
            cursor.callproc("ALTA_BAJA_MODI_HK.modi_HK", ( emp_id, nombre,passw, puesto, sede, rowcount))
            self.connection.commit()

        except self.connection.Error as error:
            print("Error: ", error)

        return rowcount

# Trae la informacion del empleado indicado
    def ver_empleado(self, emp_id):
        datos = ()
        cursor = self.connection.cursor()
        try:
            nom = cursor.var(cx_Oracle.STRING)
            pues = cursor.var(cx_Oracle.STRING)
            sed = cursor.var(cx_Oracle.NUMBER)

            cursor.callproc("ALTA_BAJA_MODI_HK.ver_HK", (emp_id,nom,pues,sed))
            self.connection.commit()

            datos=(emp_id,nom.getvalue(),pues.getvalue(),int(sed.getvalue()))

        except self.connection.Error as error:
            print("Error: ", error)

        return datos

