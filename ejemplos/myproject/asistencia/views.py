# Create your views here.

from forms import EntradaDeAsistenciaForm
from models import EntradaDeAsistencia

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect


def asistencia(request):
    if request.method == "GET":
        form = EntradaDeAsistenciaForm()
        entradas = EntradaDeAsistencia.objects.all()
    else:
        form = EntradaDeAsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')

    data = {
        'form': form,
        'entradas': entradas
    }
    return render_to_response('asistencia/asistencia.html', data)
