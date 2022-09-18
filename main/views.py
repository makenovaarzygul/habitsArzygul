from http.client import HTTPResponse
from django.shortcuts import render,redirect

from .models import Habits
from .forms import HabitsForm

def index(request):
    habits = Habits.objects.order_by('-id') #сортировка по айди,от новых привычек к старым
    return render(request, 'main/index.html',{'title':'Главная страница сайта','habits': habits})

def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = HabitsForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ФОРМА НЕВЕРНАЯ'


    form = HabitsForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request, 'main/create.html',context)


