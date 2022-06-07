from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)
def today(request):
    return render(request,'today-special.html',{})
def menu(request):
    return render(request,'menu.html',{})
def contact(request):
    return render(request,'contact.html',{})
