from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.UserService import UserService

@api_view(['GET'])
def get_all_users(request):
    users = UserService.get_all_users()
    return Response([u.__dict__ for u in users])

@api_view(['GET'])
def get_user_detail(request, user_id):
    user = UserService.get_user_by_id(user_id)
    return Response(user.__dict__) if user else Response({'error': 'Not found'}, status=404)
