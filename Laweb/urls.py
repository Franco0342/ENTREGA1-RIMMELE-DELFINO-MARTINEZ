from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path('productForm/', prt, name= 'productForm' ),
    path('clienteForm/', clienteForm, name= 'clienteForm' ),
    path('pedidoForm/', pedidos, name='pedidoForm'),
    path('',inicio , name= 'inicio'),
   
]