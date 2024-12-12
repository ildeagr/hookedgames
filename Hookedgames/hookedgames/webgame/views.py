from django.shortcuts import render, redirect
from urllib3 import request

from webgame.models import Peticion
import requests


# Carga la webapi en la página pricipal
def index(request):
    api_url= "https://api.rawg.io/api/games?key=737fba033eea48d093e94611b70394e3&dates=2019-01-01,2019-12-31&ordering=-added"
    response = requests.get(api_url)

    info = response.json()

    context = {
         'datos': info['results']
    }
    return render(request, "index.html",context)

# Muestra el formulario de contacto
def contacto(request):
     return render(request, "contacto.html")

# Comprueba datos del cliente para inicio sesion
def login(request):
     return render(request, "login.html")

# Carga el catálogo si se inicia sesion con éxito
def catalogo(request):
     passw2 = ''
     email = request.POST['txtemail']
     passw = request.POST['txtpass']

     consulta = Peticion()
     respuesta=consulta.select(email)
     
     for i in respuesta:
          passw2 = i

     if passw == passw2[1]:
           del request.session['carrito']
           request.session['usuario_email'] = email
           request.session['usuario_id'] = passw2[0]
           consulta=Peticion()
           catalogue = consulta.uploadcata()

           context = {

                'lista_catalogo' : catalogue
           }

           return render(request, "catalogo.html", context)
     else:

          context = {
               'mensaje': 'Error de credenciales.vuelva a intentarlo o registre nuevo usuario.'
          }
          return render(request, "login.html",context)


# Página para volver al catálogo una vez iniciada la sesion
def volvercatalogo(request):
     consulta = Peticion()
     catalogue = consulta.uploadcata()

     context = {

          'lista_catalogo': catalogue
     }

     return render(request, "catalogo.html", context)


# Muestra la página para registrarse como cliente nuevo
def registro(request):
     return render(request, "registro.html")

# Registra los datos del nuevo cliente en la BBDD
def nuevocliente(request):
     dni = request.POST['txtdni']
     nom = request.POST['txtnombre']
     passw = request.POST['txtpass']
     email = request.POST['txtemail']
     direc = request.POST['txtdirec']
     tele = request.POST['txttelf']

     datos=(int(dni),nom,passw,email,direc,int(tele))

     consulta = Peticion()
     rowcount=consulta.insert(datos)

     if rowcount != 0:
          return render(request, "login.html")

     else:
          return render(request, "registro.html")


# Agrega articulos al carrito
def agregarcarrito(request):
     if 'carrito' not in request.session:
          request.session['carrito'] = []
          request.session['cantidades'] = []

     idg = request.POST['agregar']
     carrito = request.session['carrito']
     cantidades = request.session['cantidades']

     if idg in carrito:
          i = 0
          for clave, valor in cantidades:
               if clave == idg:
                    cantidades[i][idg] +=1
               else:
                    i += 1
          return redirect("volvercatalogo")
     else:
         carrito.append(idg)
         cantidades.append({idg,1})
         request.session['carrito'] = carrito
         request.session['cantidades'] = cantidades

     return redirect("volvercatalogo")

# Comprueba datos del cliente para inicio sesion
def eliminarcarrito(request):
     idg = request.POST['eliminar']
     carrito = request.session['carrito']
     cantidades = request.session['cantidades']

     i=0
     for clave, valor in cantidades:
          if clave == idg:
               cantidades.pop(i)
          else:
               i +=1

     carrito.remove(idg)
     request.session['carrito'] = carrito
     request.session['cantiades'] = cantidades

     return render(request, "carrito.html")

# Muestra lo que contiene el carrito
def vercarrito(request):
     carrito = request.session['carrito']
     cantidades = request.session['cantidades']
     datos = ",".join(carrito)

     consulta = Peticion()
     cesta = consulta.selectcarro(datos)

     i = 0
     for diccionariocantidades in cantidades:
          for clave, valor in diccionariocantidades.items():
               cesta[i][clave] = valor
               i += 1

     print(cantidades)

     context = {
          'lista': cesta,
     }
     return render(request, "carrito.html", context)

# Muestra los datos de perfil del cliente de la sesion abierta
def perfil(request):
     usuario = request.session['usuario_email']
     consulta=Peticion()
     respuesta = consulta.selectclient(usuario)

     context = {
          'user' : respuesta
     }

     return render(request, "perfil.html", context)

# Borra los datos almacenados de la sesion y muestra la página principal
def cerrarsesion(request):
     del request.session['usuario_id']
     del request.session['usuario_email']
     del request.session['carrito']
     del request.session['usuario_empl']
     return render(request, "index.html")

# Muestra un mensaje cuando mandamos un formulario de contacto
def mensaje(request):
     mensaje = 'Mensaje enviado, le contestaremos lo antes posible.'

     context = {
          'dato':mensaje
     }

     return render(request, "mensaje.html",context)


# Comprueba datos del empleado para inicio sesion
def loginempleados(request):
      return render(request, "loginempleados.html")

# Muestra el menu empleados una vez iniciada la sesion
def menuempleados(request):
     passw2 = ''
     user = request.POST['txtuser']
     passw = request.POST['txtpass']

     consulta = Peticion()
     respuesta = consulta.selectempl(user)

     for i in respuesta:
          passw2 = i

     if passw == passw2[0]:
          request.session['usuario_empl'] = user

          return render(request, "menuempleados.html")
     else:
          return render(request, "loginempleados.html")

# Para volver al menú empleados si la sesion está abierta
def volveralmenuempleados(request):
     return render(request, "menuempleados.html")

# Muestra la página de gestion según lo seleccionado
def gestion(request):
     name = request.POST.get('submit')

     if name == 'stock':
          return render(request, "gestionstock.html")

     elif name == 'personal':
          return render(request, "gestionpersonal.html")

     elif name == 'ventas':
          consulta = Peticion()
          ventas = consulta.selectventas()

          context = {

               'lista_catalogo': ventas
          }
          return render(request, "gestionventas.html",context)

     return render(request, "gestionstock.html")




from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

# Muestra el stock de un juego concreto
def buscarstock(request):
     titulo = request.POST['titulo']
     consulta = Peticion()
     consultastock = consulta.select_stock(titulo)

     context = {
          'Gestion_Almacenes': consultastock,
          'buscar': 'True',
          'ver': 'False'
     }
     return render(request, "gestionstock.html", context)

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

# Modifica el stock de un articulo
def modificarstock(request):
     idg = request.POST['txtidg']
     cant = request.POST['txtcantidad']
     datos = (int(cant),int(idg))

     consulta = Peticion()
     rowcount = consulta.modificardatos(datos)

     if rowcount != 0:
          resultado = consulta.mostrar_stock_completo()

          context = {
               'Gestion_Almacenes': resultado,
               'buscar': 'False',
               'ver': 'True'
          }
          return render(request, "gestionstock.html", context)
     else:
          return render(request, "gestionstock.html")

# Muestra el stock completo
def verstockcompleto(request):
     consulta = Peticion()
     stockcompleto = consulta.mostrar_stock_completo()
     context = {
          'Gestion_Almacenes': stockcompleto,
               'ver': 'True'
     }
     return render(request, "gestionstock.html", context)


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Inserta un empleado nuevo
def alta_empleado(request):
     if request.method == 'POST':
          emp_id = request.POST['id']
          nombre = request.POST['nombre']
          passw = request.POST['password']
          puesto = request.POST['puesto']
          sede = request.POST['sede']

          emp_id = int(emp_id)
          sede = int(sede)
          accion = Peticion()
          accion.alta_empleado(emp_id,nombre,passw,puesto,sede)

          return render(request, "gestionpersonal.html")

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

# Borra un empleado
def baja_empleado(request):
     if request.method == 'POST':
          emp_id = request.POST['Id']
          accion = Peticion()
          rowcount = accion.baja_empleado(int(emp_id))

          if rowcount != 0:
               context = {
                    'mensajeerror': 'OperaciÓn realizada',
               }
               return render(request, "gestionpersonal.html")

          else:

               context = {
                    'mensajeerror' : 'Error en la operación',
               }
               return render(request, "gestionpersonal.html")


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

# Modifica datos de un empleado
def modi_empleado(request):
     if request.method == 'POST':
          emp_id = request.POST['id']
          nombre = request.POST['nombre']
          passw = request.POST['password']
          puesto = request.POST['puesto']
          sede = request.POST['sede']

          emp_id = int(emp_id)
          sede = int(sede)
          accion = Peticion()
          accion.modi_empleado(emp_id,nombre,passw,puesto,sede)


          return render(request, "gestionpersonal.html")


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

#Muestra la info de un empleado
def ver_empleado(request):
     if request.method == 'POST':
          emp_id = int(request.POST['id'])
          accion = Peticion()

          tabla = accion.ver_empleado(emp_id)

          context = {
                 'lista': tabla,
                 'tabla' : 'True'
          }

          return render(request, "gestionpersonal.html", context)