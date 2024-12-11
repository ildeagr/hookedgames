from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from webgame.models import Peticion
import requests

def index(request):
    api_url= "https://api.rawg.io/api/games?key=737fba033eea48d093e94611b70394e3&dates=2019-01-01,2019-12-31&ordering=-added"
    response = requests.get(api_url)

    info = response.json()

    context = {
         'datos': info['results']
    }
    return render(request, "index.html",context)

def index2(request):
     return render(request, "index.html")

def login(request):
     return render(request, "login.html")

def registro(request):
     return render(request, "registro.html")

def volvercatalogo(request):
     consulta = Peticion()
     catalogue = consulta.uploadcata()

     context = {

          'lista_catalogo': catalogue
     }

     return render(request, "catalogo.html", context)

def catalogo(request):
     passw2 = ''
     email = request.POST['txtemail']
     passw = request.POST['txtpass']

     consulta = Peticion()
     respuesta=consulta.select(email)
     
     for i in respuesta:
          passw2 = i

     if passw == passw2[0]:
           request.session['usuario_id'] = email
           consulta=Peticion()
           catalogue = consulta.uploadcata()

           context = {

                'lista_catalogo' : catalogue
           }

           return render(request, "catalogo.html", context)
     else:
          return render(request, "login.html")

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

def menuempleados(request):
     return render(request, "menuempleados.html")

def gestion(request):
     name = request.POST.get('submit')

     if name == 'stock':
          return render(request, "gestionstock.html")

     elif name == 'personal':
          return render(request, "gestionpersonal.html")

     elif name == 'ventas':
          return render(request, "gestionventas.html")

     return render(request, "gestionstock.html")

def contacto(request):
     return render(request, "contacto.html")

def agregarcarrito(request):
     producto = ''
     carrito = request.session.get('carrito', {})
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


def vercarrito(request):
     carrito = request.session.get('carrito', {})

     print(carrito)
     return render(request, "carrito.html", {'carrito': carrito})

def perfil(request):
     usuario = request.session['usuario_id']
     consulta=Peticion()
     respuesta = consulta.selectclient(usuario)

     context = {
          'user' : respuesta
     }

     return render(request, "perfil.html", context)

def cerrarsesion(request):
     request.session['usuario_id'] = ''
     request.session['carrito'] = ''
     request.session['usuario_empl'] = ''
     return render(request, "index.html")

def mensaje(request):
     mensaje = 'Mensaje enviado, le contestaremos lo antes posible.'

     context = {
          'dato':mensaje
     }

     return render(request, "mensaje.html",context)




