from django.template.defaulttags import register
from django.shortcuts import render, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from radioApp.models import Location, Station, Genre, Area
from itertools import cycle
from collections import OrderedDict
import json


# Create your views here.
def index(request):
    groupTypes = ['success', 'secondary', 'info', 'warning', 'danger', 'primary', 'dark', 'light']
    genresDict = OrderedDict(zip(Genre.objects.order_by('genre'), cycle(groupTypes)))
    locationsDict = OrderedDict(zip(Location.objects.all().order_by('location'), cycle(groupTypes)))
    locAreasDict = OrderedDict(map(lambda el: [el,zip(Area.objects.filter(loc__id=el.id).order_by('area'), cycle(groupTypes))], list(locationsDict)))

    cookieLst = json.loads(request.COOKIES['djradio_cookie']) if 'djradio_cookie' in request.COOKIES else []
    favourites = Station.objects.filter(id__in=cookieLst).order_by('name')
    for st in favourites:
        st.image=st.images[0]["path"]
        

    context = {
        'title': "Radio DJango, the most pythonic music in the world!",
        'genresDict': genresDict,
        'locAreasDict': locAreasDict,
        'locationsDict' : locationsDict,
        'favourites': favourites,
        'cookieLst': cookieLst 
        }
    return render(request, 'home.html', context)

def byGenre(request, genreId):
    cookieLst = json.loads(request.COOKIES['djradio_cookie']) if 'djradio_cookie' in request.COOKIES else []
    stations = Station.objects.filter(genre__id=genreId).order_by('name')
    #    list(filter(lambda st:st.genre.genre==genreName, Station.objects.all().order_by('name')))
    for st in stations:
        st.image=st.images[0]["path"]
        
        
    page = request.GET.get('page', 1)

    paginator = Paginator(stations, 15)
    try:
        stations = paginator.page(page)
    except PageNotAnInteger:
        stations = paginator.page(1)
    except EmptyPage:
        stations = paginator.page(paginator.num_pages)


    context = {
        'title': stations[0].genre,   
        'stations': stations,
        'favourites': cookieLst
        }
    return render(request, 'genreStations.html', context)
    

def byArea(request, areaId):
    cookieLst = json.loads(request.COOKIES['djradio_cookie']) if 'djradio_cookie' in request.COOKIES else []
    stations = Station.objects.filter(area__id=areaId).order_by('name')
    #    stations = list(filter(lambda st:st.area.area==areaName, Station.objects.all().order_by('name')))
    for st in stations:
        st.image=st.images[0]["path"]
#         st.stationUrl=st.stationUrl+("/;" if st.stationUrl.count("/")==2 else "")

    page = request.GET.get('page', 1)

    paginator = Paginator(stations, 15)
    try:
        stations = paginator.page(page)
    except PageNotAnInteger:
        stations = paginator.page(1)
    except EmptyPage:
        stations = paginator.page(paginator.num_pages)


    context = {
        'title': stations[0].area,    
        'stations': stations,
        'favourites': cookieLst,
        }
    return render(request, 'areaStations.html', context)


def addToFavs(request, stationId):
    cookieLst = json.loads(request.COOKIES['djradio_cookie']) if 'djradio_cookie' in request.COOKIES else []
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if stationId not in cookieLst:
        cookieLst.append(stationId)
        response.set_cookie(key='djradio_cookie', value=json.dumps(cookieLst), max_age=365*2*24*3600)
    return response

def remFromFavs(request, stationId):
    cookieLst = json.loads(request.COOKIES['djradio_cookie']) if 'djradio_cookie' in request.COOKIES else []
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    if stationId in cookieLst:
        cookieLst.remove(stationId)
        response.set_cookie(key='djradio_cookie', value=json.dumps(cookieLst), max_age=365*2*24*3600)
    return response