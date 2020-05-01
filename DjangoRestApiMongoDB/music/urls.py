from django.urls import path
# from music import views 
from .views import AlbumView,ArtistView,SongView
app_name = "music"
urlpatterns = [ 
     path('albums/', AlbumView.as_view()),
     path('artists/', ArtistView.as_view()),
     path('songs/', SongView.as_view()),
    # url(r'^api/songs$', views.songs_list),
    # url(r'^api/artists$', views.artist_list),
    # url(r'^api/albums$', views.album_list),
]