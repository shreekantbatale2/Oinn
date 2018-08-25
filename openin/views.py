from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<H2> hi shree </h2>")
