from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('genre/<int:genreId>', views.byGenre, name='byGenre'),
    path('area/<int:areaId>', views.byArea, name='byArea'),
    path('addfavs/<int:stationId>', views.addToFavs, name='addToFavs'),
    path('remfavs/<int:stationId>', views.remFromFavs, name='remFromFavs'),
]
