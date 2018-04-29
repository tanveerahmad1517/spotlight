from django.shortcuts import render

def login(request):
    data = {

    }
    return render(request, 'login.html', context=data)
