from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.SongService import SongService

@api_view(['GET'])
def get_all_songs(request):
    songs = SongService.get_all_songs()
    return Response([song.__dict__ for song in songs])

@api_view(['GET'])
def get_song_detail(request, song_id):
    song = SongService.get_song_by_id(song_id)
    return Response(song.__dict__) if song else Response({'error': 'Not found'}, status=404)
