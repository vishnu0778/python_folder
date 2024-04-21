from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'varibles':'this is the test'
    }
    return render(request, "index.html",context)
    # return HttpResponse("THis is Main page")
    
def about(request):
    return render(request, "about.html")
    # return HttpResponse("THis is about page")

def service(request):
    return HttpResponse("THis is Service page")

def login(request):
    return render(request, "login.html")