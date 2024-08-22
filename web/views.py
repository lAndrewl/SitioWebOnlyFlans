from django.shortcuts import render, redirect
#1) Importamos el modelo
from .models import Flan,Contact,ContactForm
from .forms import FlanFormModel,ContactFormForm,ContactFormModel
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    #flanes = Flan.objects.all()
    #2) Realizamos la consulta filtrando los flanes que tengan is_private=False
    flanes_publicos = Flan.objects.filter(is_private=False)
    # productos = Productos.objects.all() "select * from productos"
    context={
        'title':'Bienvenido a OnlyFlans',
        #'flanes': flanes,
        'flanes_publicos': flanes_publicos,#3) Agregamos a la variable de contexto o context
    }
    return render(request,'index.html',context)

def acerca(request):
    context={
        'title':'Acerca'
    }
    return render(request,'acerca.html',context)

@login_required
def bienvenido(request):
    if not request.session.get('has_visited', False):
        request.session['has_visited'] = True
        show_welcome_message = True
    else:
        show_welcome_message = False

    # Aquí asumo que flanes_privados se obtiene de alguna manera, como un queryset
    flanes_privados = Flan.objects.filter(is_private=True)  # Cambia esto según tu lógica

    return render(request, 'bienvenido.html', {
        'title': 'Bienvenido',
        'flanes_privados': flanes_privados,
        'show_welcome_message': show_welcome_message
    })
# @login_required
# def bienvenido(request):
#     flanes_privados = Flan.objects.filter(is_private=True)
#     context={
#         'title':'Bienvenido',
#         'flanes_privados': flanes_privados,
#     }
#     return render(request,'bienvenido.html',context)

# def contacto(request):
#     if request.method == 'POST':
#         form = ContactFormForm(request.POST)
#         if form.is_valid():
#             contact_form=ContactFormForm.objects.create(**form.cleaned_data)
#             return HttpResponseRedirect('/exito')
#     else:
#         form = ContactFormForm()
#     return render(request, 'contacto.html',{'form': form})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/exito')
        else:
            print(form.errors)  # Imprime los errores del formulario
    else:
        form = ContactFormModel()
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')