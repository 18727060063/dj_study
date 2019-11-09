from django.shortcuts import render_to_response
# Create your views here.
from DjangoApp import loadNormalData
from DjangoApp.models import NormalPeople


def index(request):
    # loadNormalData.readTecExcel()
    bb= NormalPeople.objects.all()
    return render_to_response('index.html', {"data": bb})

def load_original_data(request):
    loadNormalData.readTecExcel()
    return render_to_response('index.html')
