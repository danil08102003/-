from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Catigories
# Create your views here.

def index(request):

   
    context = {
        'title': 'Home - Главная',
        'content': 'Строительная компания BorovGrand',
    }

    return render(request, 'main/index.html', context)



def about(request):
    
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том какая строительная компания у нас хорошая и какой хороший товар'
    }

    return render(request, 'main/about.html', context)