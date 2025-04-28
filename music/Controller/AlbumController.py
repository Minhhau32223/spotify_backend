from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.AlbumService import AlbumService

@api_view(['GET'])
def get_all_albums(request):
    albums = AlbumService.get_all_albums()
    return Response([album.__dict__ for album in albums])

@api_view(['GET'])
def get_album_detail(request, album_id):
    album = AlbumService.get_album_by_id(album_id)
    return Response(album.__dict__) if album else Response({'error': 'Not found'}, status=404)
