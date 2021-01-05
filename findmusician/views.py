from django.shortcuts import redirect

def HomeView(request):
    response = redirect('/users/')
    return response