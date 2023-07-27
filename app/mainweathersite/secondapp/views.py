from django.shortcuts import render
from django.http import HttpResponse
from .models import weatherInput, weatherQuery

def index(request):
    weatherQuery_latest = weatherQuery.objects.order_by("-pub_date")[:5] # orders question by publish date
    context = {"weatherQuery_latest":weatherQuery_latest,}
    return render(request,"secondapp/index.html",context)
# Create your views here.

def search(request,location_id):
    return HttpResponse("You've selected the location %s." % location_id)

def weather(request,location_id):
    response = "The weather of %s is"
    return HttpResponse(response % location_id)