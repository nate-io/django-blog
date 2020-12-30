from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  response = '<h1>Blog Home</h1>'

  return HttpResponse(response)

def about(request):
  response = '<h1>Blog About</h1>'

  return HttpResponse(response) 