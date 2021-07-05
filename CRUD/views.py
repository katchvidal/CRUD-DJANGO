from django.shortcuts import render, redirect
from .models import Persona
from .form import PersonaForm
#   Vistas Basadas en clases
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

# Create your views here.
'''
#   Vistas Basadas en Funciones
def create(request):
    form = PersonaForm

    if request.method == 'POST':
         form = PersonaForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('read')

    return render(request, 'create.html', {'form' : form})


def read(request):
    
    querys = Persona.objects.all()

    return render(request, 'read.html', {'querys' : querys})


def update(request, id):

    persona = Persona.objects.get(id = id)

    if request.method == 'GET':
        form = PersonaForm( instance    =   persona  )
        contexto = {
            'form' : form
        }
    else:
        form = PersonaForm(request.POST, instance = persona)
        contexto = {
            'form' : form
        }
        if form.is_valid():
            form.save()
            return redirect('read')

    return render(request, 'create.html', contexto)


def delete(request, id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('read')

'''
#   Vistas Basadas en Clases CRUD

class PersonaList(ListView):
    model = Persona
    template_name = 'read02.html'

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'create.html'
    #   En la Plantilla El formulario se va a pasar con el nombre de form
    success_url = reverse_lazy('read')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'create.html'
    success_url = reverse_lazy('read')

class PersonaDelete(DeleteView):
    model   =   Persona
    template_name = 'Check.html'
    success_url = reverse_lazy('read')