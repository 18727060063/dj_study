from django.shortcuts import render_to_response
# Create your views here.
from DjangoApp.models import NormalPeople


def index(request):
    bb= NormalPeople.objects.all()
    return render_to_response('index.html', {'data': bb})

