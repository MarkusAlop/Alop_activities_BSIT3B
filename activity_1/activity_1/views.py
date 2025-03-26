import django.http

def index(request):
    return django.http.HttpResponse("Hi Hello")
