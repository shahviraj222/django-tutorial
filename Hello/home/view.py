from django.shortcuts import render,HttpResponse
# url dispatching
def index(requeset):
    return HttpResponse("This is my home page")

def about(requeset):
    return HttpResponse("This is my about page")
def services(requeset):
    return HttpResponse("This is my services page")
def contact(requeset):
    return HttpResponse
