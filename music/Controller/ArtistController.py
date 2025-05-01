from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.ArtistService import ArtistService

@api_view(['GET'])
def get_all_artists(request):
    artists = ArtistService.get_all_artists()
    return Response([artist.__dict__ for artist in artists])

@api_view(['GET'])
def get_artist_detail(request, artist_id):
    artist = ArtistService.get_artist_by_id(artist_id)
    return Response(artist.__dict__) if artist else Response({'error': 'Not found'}, status=404)
