from django.contrib import admin
from django.urls import path
from home import view

urlpatterns = [
    path("",view.index,name="home"),
    path("about",view.about,name="about"),
    path("services",view.services,name="services"),
    path("contact",view.contact,name="contact")

]
