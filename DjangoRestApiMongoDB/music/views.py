from django.shortcuts import render

from music.models import Song
from music.models import Artist
from music.models import Album
from music.serializers import SongSerializer
from music.serializers import ArtistSerializer
from music.serializers import AlbumSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# class musicView(APIView):
#     def get(self, request):
#         albums = Album.objects.all()
#         artists = Artist.objects.all()
#         songs = Song.objects.all()
#         serializer = AlbumSerializer(albums, many=True)
#         return Response({"music": serializer.data})

#     def post(self, request):
#         album = request.data.get('album')

#         # Create an album from the above data
#         serializer = AlbumSerializer(data=album)
#         if serializer.is_valid(raise_exception=True):
#             album_saved = serializer.save()
#         return Response({"success": "Album '{}' created successfully".format(album_saved.title)})

class AlbumView(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response({"albums": serializer.data})

    def post(self, request):
        album = request.data.get('album')

        # Create an album from the above data
        serializer = AlbumSerializer(data=album)
        if serializer.is_valid(raise_exception=True):
            album_saved = serializer.save()
        return Response({"success": "Album '{}' created successfully".format(album_saved.title)})

class ArtistView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response({"artists": serializer.data})

    def post(self, request):
        artist = request.data.get('artist')

        # Create an artist from the above data
        serializer =ArtistSerializer(data=artist)
        if serializer.is_valid(raise_exception=True):
            artist_saved = serializer.save()
        return Response({"success": "artist '{}' created successfully".format(artist_saved.name)})

class SongView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response({"songs": serializer.data})

    
    def pre_save(self, obj):
        song.artist = self.request.user
    def post(self, request):
        song = request.data.get('song')
        # Create an song from the above data
        serializer =SongSerializer(data=song)
        if serializer.is_valid(raise_exception=True):
            song_saved = serializer.save()
        return Response({"success": "song '{}' created successfully".format(song_saved.title)})

    
 
 
