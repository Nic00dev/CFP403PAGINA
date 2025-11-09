from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Proyecto_pruebas
from django.shortcuts import render

from .forms import nueva_tarea
# Create your views here.

def hola(request,id):
    hola = Proyecto_pruebas.objects.get(id=id)
    
    return HttpResponse('che %s ' % hola.name)

def peron (request):

    return HttpResponse(request)

def parametrico(request,peroncha):

    return HttpResponse('hola %s' % peroncha)



def listado (request,patron):

    lista_cosas = ['roberto','flores']

    return HttpResponse('listado de cosas: %s' % lista_cosas[patron])





def conjason(request,id):

    eyecto = list(Proyecto_pruebas.objects.values());    
    return JsonResponse(eyecto,safe=False)

def condb(request,id):

    db= Proyecto_pruebas.objects.get(id=id)
    db2= Proyecto_pruebas.objects.get(id=id)
    return HttpResponse('proyecto: %s id: %s' % (db.name,db2.id));

def index (request):

    giampieri = ['hoy es un dia giampierizante','tito']
    repetir = range(3)
    return render(request,'index.html',{'giampieri':giampieri,'repetir':repetir})


''' def repaso (request,param):

    #allo = Proyecto_pruebas.objects.get(id=id);

    vagini = param
    
    return HttpResponse('resultado: %s' % vagini) '''


'''def repaso2 (request,param):

    resultado = "nada"
    if param%2 == 0:
        resultado = "par";
    else:
        resultado = "impar"

    return HttpResponse ("el numero es %s" % resultado);'''


'''def repaso3(request,param):

    listado =['tito','radetic']
    error = listado

    if param > len(listado)-1 or len(listado)<=0:
        error = "no hay datos"
        return HttpResponse ("resultado %s" % error)
    else:

        return HttpResponse ("resultado %s" % listado[param])
    '''

'''def repaso4(request,param):

    listado = {"fruta":"pera","fruta2":"manzana"}
    return JsonResponse(listado)'''

'''def repaso5(request):
    listado = Proyecto_pruebas.objects.all()
    nombres = [str(p) for p in listado]  # convierte cada objeto a string
    return HttpResponse("%s"% nombres)'''


'''def repaso6(request):

    listado =['tito','tita','maria','giampieri']
    rango = 3
    return render(request,'index.html',{'listado':listado,'rango':rango})'''

'''def repaso7(request,param):

    parametro = param;
    return render (request,'index.html',{'parametro':parametro})'''
'''def repaso8(request,param):

    boleano = 0;

    if param == 1:
        boleano = True;
    else:
        boleano = False;

    return render (request,'index.html',{'boleano':boleano})'''

'''def formularios(request):
    
    saludo = request.GET.get('titulo')
    
    print(request.GET.get('titulo'))

    if (saludo != None):
        
        return render (request,'index.html',{'form':nueva_tarea(),'saludo':"hola %s" % saludo})

    else:
        return render (request,'index.html',{'form':nueva_tarea(),'saludo':"seguro sucio?"})'''


'''def formularios2(request):

    resultado= "sin datos"
    lista = ['tomate','polenta','fideo']
    titulo = request.GET.get('titulo','')
    if titulo in lista:
        resultado = "en stock"

            

    return render(request,'index.html',{'form':nueva_tarea(),'resultado':resultado})'''


'''def formularios3(request):

    n1 = request.GET.get('numero1','');
    n2 = request.GET.get('numero2','');
    
    resultado = int(n1)+int(n2);
    return render(request,'index.html',{'form':nueva_tarea(),'resultado':resultado})'''

def formularios4(request):

    if request.method =='GET':
        fatal = request.GET.get('selecciones','');
        imagen = "defeto"
        if fatal == 'arg':
            imagen = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Flag_of_Argentina.svg/250px-Flag_of_Argentina.svg.png"
        else:
            imagen = "https://cdn.britannica.com/15/183615-050-6AB17F25/World-Data-Locator-Map-China.jpg"
        
        
        
        return render(request,'index.html',{'form':nueva_tarea,'resultado':fatal,'imagen':imagen})
    else:
        fatal = request.POST.get('selecciones','');
        imagen = "defeto"
        return render(request,'index.html',{'form':nueva_tarea,'resultado':fatal,'imagen':imagen})



def Principal(request):

    texto = "pagina principal";

    return render(request,'index.html',{'texto':texto})

def Nosotros(request):

    texto = "aca hablamos de nosotros";

    return render(request,'Nosotros.html',{'texto':texto})


def Cursos(request):

    texto = "aca ponemos los cursos"

    return render (request,'Cursos.html',{'texto':texto})

def Contactos(request):

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        mensaje = request.POST.get('mensaje')

        print("Nombre:", nombre)
        print("Email:", email)
        print("Teléfono:", telefono)
        print("Mensaje:", mensaje)

        return render(request, 'Contacto.html', {'enviado': True})

    return render(request, 'Contacto.html')

def informatica(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/Informatica.html',{'texto':texto})

def gastronomia(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/Gastronomia.html',{'texto':texto})

def Agropecuarias(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/Agropecuarias.html',{'texto':texto})

def Construcciones(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/Construcciones.html',{'texto':texto})

def Estetica(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/Estetica.html',{'texto':texto})

def Idiomas(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/Idiomas.html',{'texto':texto})

def Limpieza(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/Limpieza.html',{'texto':texto})

def mecanica(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/mecanica.html',{'texto':texto})

def Textil(request):
    texto = "aca ponemos los contactos"

    return render (request,'cursos/Textil.html',{'texto':texto})