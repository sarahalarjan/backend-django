from rest_framework import serializers 
from music.models import Artist
from music.models import Song 
from music.models import Album
 
# class MusicSerializer(serializers.ModelSerializer):
#     title = serializers.CharField(max_length=70)
#     artist_id = serializers.IntegerField()
#     class Meta:
#         model = Album
#         fields = ('id',
#                   'title',
#                   'artist_id',
#                   )
class AlbumSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=70)
    artist_id = serializers.IntegerField()
    class Meta:
        model = Album
        fields = ('id',
                  'title',
                  'artist_id',
                  )

def create(self, validated_data):
        return Album.objects.create(**validated_data)
   
 
class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=70)

    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  )

def create(self, validated_data):
        return Artist.objects.create(**validated_data)  

class SongSerializer(serializers.ModelSerializer):
 
      title = serializers.CharField(max_length=70)
      artist = serializers.ReadOnlyField(source='artist.name')
      album = serializers.ReadOnlyField(source='album.title')
      artist_id = serializers.IntegerField()
      album_id = serializers.IntegerField()
      
      class Meta:
        model = Song
        fields = ('id',
                  'title',
                  'artist',
                  'album',
                  'artist_id',
                  'album_id'
                  )
                 

def create(self, validated_data):
        return Song.objects.create(**validated_data)
