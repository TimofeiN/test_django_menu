from django.shortcuts import render
# from .models import MenuItem
from django.views.generic import TemplateView


def index_view(request):
    return render(request, 'menuapp/index.html')


class MainOne(TemplateView):
    template_name = "menuapp/m1.html"


class MainTwo(TemplateView):
    template_name = "menuapp/m2.html"


class NestOneMainOne(TemplateView):
    template_name = "menuapp/n1_m1.html"


class NestTwoMainOne(TemplateView):
    template_name = "menuapp/n2_m1.html"
