from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World! I'm home")

def about(request):
    return HttpResponse("This is the about page")