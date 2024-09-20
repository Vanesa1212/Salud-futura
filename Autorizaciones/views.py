from django.shortcuts import render, redirect, get_object_or_404
from .models import AutorizacionMedica, Pacientes
from .forms import AutorizacionMedicaForm, PacientesForm

# Create your views here.

def listar_autorizaciones(request):
    autorizaciones = AutorizacionMedica.objects.all()
    return render(request, 'autorizaciones/listar.html', {'autorizaciones': autorizaciones})

def crear_autorizacion(request):
    if request.method == 'POST':
        form = AutorizacionMedicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autorizaciones')
    else:
        form = AutorizacionMedicaForm()
    return render(request, 'autorizaciones/crear.html', {'form': form})

def editar_autorizacion(request, pk):
    autorizacion = get_object_or_404(AutorizacionMedica, pk=pk)
    if request.method == 'POST':
        form = AutorizacionMedicaForm(request.POST, instance=autorizacion)
        if form.is_valid():
            form.save()
            return redirect('listar_autorizaciones')
    else:
        form = AutorizacionMedicaForm(instance=autorizacion)
    return render(request, 'autorizaciones/editar.html', {'form': form})

def listar_pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, 'pacientes/listar.html', {'pacientes': pacientes})

def crear_pacientes(request):
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacientesForm()
    return render(request, 'pacientes/crear.html', {'form': form})

def editar_pacientes(request, pk):
    pacientes = get_object_or_404(Pacientes, pk=pk)
    if request.method == 'POST':
        form = PacientesForm(request.POST, instance=pacientes)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacientesForm(instance=pacientes)
    return render(request, 'pacientes/editar.html', {'form': form})