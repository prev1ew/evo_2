from django.shortcuts import render, redirect
from .models import Persons
from .forms import PersonsForm


def index(request):
    result = ''
    if request.method == 'POST':
        form = PersonsForm(request.POST)
        if form.is_valid():
            form.save()
            result = f'Привет, {request.POST["name"]}'
        else:
            result = f'Уже виделись, {request.POST["name"]}'

    form = PersonsForm
    data = {'form': form,
            'result': result
            }

    return render(request, 'main/index.html', data)


def show_list(request):
    persons = Persons.objects.all()
    data = {'persons': persons}
    return render(request, 'main/list.html', data)
