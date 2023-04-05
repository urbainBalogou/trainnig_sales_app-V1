from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from .models import Formation


def index(request):
    """ formations = Formation.objects.all()
    pizza_name_price = [formation.nom + ": " + str(formation.prix) + " F"for formation in formations]
    pizza_name_price_str = ", ".join(pizza_name_price)
    return HttpResponse('Les Formations:' + pizza_name_price_str)"""
    formations = Formation.objects.all().order_by("prix")
    return render(request, 'menu/index.html', {'formations': formations})

def api_get_formations(request):
    formations = Formation.objects.all().order_by("prix")
    json = serializers.serialize("json", formations)
    return HttpResponse(json)

# Create your views here.
