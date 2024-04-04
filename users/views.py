from django.shortcuts import render

# Create your views here.



def login(request):

    
    context = {
        'title': 'Home - Авторизация',
       
    }
    return render(request, 'users/login.html', context)

def reqistration(request):

    context = {
        'title': 'Home - Регистрация',
       
    }
    return render(request, 'users/reqistration.html', context)



def profile(request):

    context = {
        'title': 'Home - Кабинет',
       
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...