from django.http import JsonResponse
from django.shortcuts import render
import requests
import random


def cat_fact(request):
    response = requests.get('https://catfact.ninja/fact')
    fact = response.json()['fact']
    context = {'fact': fact}
    return render(request, 'index.html', context)
