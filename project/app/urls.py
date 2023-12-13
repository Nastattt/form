from django.urls import path
from .views import *


urlpatterns = [
    path('',index, name = "home"),
    path('myform',myForm,name = 'form'),
    path('news', news, name='news')
    #path('users',user,name= "user"),
]