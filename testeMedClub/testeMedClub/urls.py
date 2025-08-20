"""
URL configuration for testeMedClub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path,include
from usuarios.views import LoginView
from itens import views as ItemViewSet
from usuarios import views as UsuarioViewSet
from itens.api.serializers import ItemSerializer
from usuarios.serializer import UsuarioSerializer
from rest_framework.routers import DefaultRouter
route = DefaultRouter()

route.register(r'items',ItemViewSet.ItemViewSet, basename='item')
route.register(r'usuarios',UsuarioViewSet.UsuarioViewSet, basename='usuario')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('login/', LoginView.as_view(), name="login"),
    
]


