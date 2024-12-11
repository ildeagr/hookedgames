from django.shortcuts import render, redirect
from webgame.models import Peticion
import requests

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


# Carga la webapi en la página pricipal
def index(request):
    api_url= "https://api.rawg.io/api/games?key=737fba033eea48d093e94611b70394e3&dates=2019-01-01,2019-12-31&ordering=-added"
    response = requests.get(api_url)

    info = response.json()

    context = {
         'datos': info['results']
    }
    return render(request, "index.html",context)

def gestionventas(request):
     return render(request, "gestionventas.html")

# Comprueba datos del cliente para inicio sesion
def login(request):
     return render(request, "login.html")

# Muestra la página para registrarse como cliente nuevo
def registro(request):
     return render(request, "registro.html")

# Página para volver al catálogo una vez iniciada la sesion
def volvercatalogo(request):
     consulta = Peticion()
     catalogue = consulta.uploadcata()

     context = {

          'lista_catalogo': catalogue
     }

     return render(request, "catalogo.html", context)

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

# Registra los datos del nuevo cliente en la BBDD
def nuevocliente(request):
     nom = request.POST['txtnombre']
     ape = request.POST['txtapellido']
     passw = request.POST['txtpass']
     email = request.POST['txtemail']
     direc = request.POST['txtdirec']
     tele = request.POST['txttelf']

     datos=(0,nom,ape,passw,email,direc,tele)

     consulta = Peticion()
     rowcount=consulta.insert(datos)

     if rowcount != 0:
          return render(request, "login.html")

     else:
          return render(request, "regitro.html")

# Comprueba datos del empleado para inicio sesion
def loginempleados(request):
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

# Muestra el menu empleados una vez iniciada la sesion
def menuempleados(request):
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

# Muestra el formulario de contacto
def contacto(request):
     return render(request, "contacto.html")

# Agrega articulos al carrito
def agregarcarrito(request):
     producto = ''
     carrito = request.session.get('carrito', [])
     idg = request.POST['agregar']

     consulta = Peticion()
     resultado = consulta.selectproduct(idg)

     for i in resultado:
          producto = i

     if producto[0] in carrito:
        carrito[producto[0]]['cantidad'] += 1
     else:
         carrito[producto[0]] = {
              'titulo': producto[1],
              'carátula': producto[2],
              'precio': producto[5],
              'cantidad': 1
         }
     request.session['carrito'] = carrito

     return redirect("volvercatalogo")

# Muestra lo que contiene el carrito
def vercarrito(request):
     carrito = request.session.get('carrito', {})

     print(carrito)
     return render(request, "carrito.html", {'carrito': carrito})

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
     request.session['usuario_id'] = ''
     request.session['usuario_email'] = ''
     request.session['carrito'] = ''
     request.session['usuario_empl'] = ''
     return render(request, "index.html")

# Muestra un mensaje cuando mandamos un formulario de contacto
def mensaje(request):
     mensaje = 'Mensaje enviado, le contestaremos lo antes posible.'

     context = {
          'dato':mensaje
     }

     return render(request, "mensaje.html",context)

# Muestra el stock de un juego concreto
def buscarstock(request):
     titulo = request.POST['titulo']
     consulta = Peticion()
     consultastock = consulta.select_stock(titulo)
     context = {
          'Gestion_Almacenes': consultastock,
          'ver': 'False'
     }
     return render(request, "gestionstock.html", context)

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


