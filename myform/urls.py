from django.contrib import admin
from django.urls import path
from . import views

app_name='myform'

urlpatterns = [
    #path("register/", views.register,name='register'),
    path("create/<int:form>/",views.createtextformview, name='createtextformview'),
    #path("createmcq/<int:form>/",views.createmcqformview, name='createmcqformview'),
    path("formview/<int:form>/",views.formview, name='formview'),
    #path("form/<int:form>/",views.formview, name='formview'),
    path("answers/<int:form>",views.answersview, name='answersview'),
    path("",views.createformview, name='createformview'),
]