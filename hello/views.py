from django.http import HttpResponse

def index(request):
    return HttpResponse ("Hello!")

def about(request):
    return HttpResponse (" <h1>Thank you </h1>")