from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response
from django.template import RequestContext

# from .weather import weatherscript, twitterscript
from .models import *
from .. import weatherscript, twitterscript, analysis

# Create your views here.
def home(request):
    return render_to_response('home.html', { "weather_list": Weather.objects.all() }, context_instance=RequestContext(request)) 

def add(request):
   if (request.method == "POST"): #check if form is submitted
        lat = float(request.POST['latitude'])
        long = float((request).POST['longitude'])
        r = Region(latitude = lat, longitude = long)
        r.save()
        weatherscript.getweather(r, lat, long)
        twitterscript.pullTweets(r, lat, long)
        analysis.analyze(r)
        return render_to_response('map.html', {"weather_list": Stats.objects.all() }, context_instance=RequestContext(request))

def clear(request):
   if (request.method == "POST"): #check if form is submitted
       Weather.objects.all().delete()
       Region.objects.all().delete()
       Stats.objects.all().delete()
       Tweets.objects.all().delete()
       return render_to_response('home.html', {"weather_list": Stats.objects.all() }, context_instance=RequestContext(request))
