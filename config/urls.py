"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import RedirectView

import menuapp.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('1', views.MainOne.as_view(), name='m1'),
    path('2', views.MainTwo.as_view(), name='m2'),
    path('3', views.MainTwo.as_view(), name='m3'),
    path('n1', views.NestOneMainOne.as_view(), name='nest_1'),
    path('n2', views.NestTwoMainOne.as_view(), name='nest_2'),

]
