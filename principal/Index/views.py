from django.shortcuts import render

# Create your views here.
#>>>>>>>>>>>>>>>>>>>>>>--MOSTRAR EL INDEX--<<<<<<<<<<<<<<<<<<<<<<


def index(request):
    return render (request,'index.html')