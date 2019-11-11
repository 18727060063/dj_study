import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render_to_response
from DjangoApp import models


def index(request):
    return render_to_response('index.html')


def load_original_data(request):
        peoples = models.NormalPeople.objects.filter(pName__icontains=request.GET.get("name"))
        print(peoples.count())
        return JsonResponse(json.loads(serializers.serialize("json", peoples)), safe=False)

