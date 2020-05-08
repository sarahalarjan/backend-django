import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from DjangoRestApiMongoDB.music.models import Song, Artist, Album


# Create a GraphQL type for the song model
class SongType(DjangoObjectType):
    class Meta:
        model = Song


# Create a GraphQL type for the artist model
class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist


# Create a GraphQL type for the album model
class AlbumType(DjangoObjectType):
    class Meta:
        model = Album


# Create a Query type
class Query(ObjectType):
    song = graphene.Field(SongType, id=graphene.Int())
    artist = graphene.Field(ArtistType, id=graphene.Int())
    album = graphene.Field(AlbumType, id=graphene.Int())
    songs = graphene.List(SongType)

    def resolve_song(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Song.objects.get(pk=id)

        return None

    def resolve_artist(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Artist.objects.get(pk=id)

        return None

    def resolve_album(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Album.objects.get(pk=id)

        return None

    def resolve_songs(self, info, **kwargs):
        return Song.objects.all()


# Create Input Object Types


class ArtistInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class AlbumInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    artist = graphene.ObjectType(ArtistInput)


class SongInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    album = graphene.ObjectType(AlbumInput)
    artist = graphene.ObjectType(ArtistInput)


schema = graphene.Schema(query=Query)
