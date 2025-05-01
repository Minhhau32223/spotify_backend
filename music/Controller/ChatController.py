from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.ChatService import ChatService

@api_view(['POST'])
def chat_with_ai(request):
    message = request.data.get('message')
    if not message:
        return Response({'error': 'Missing message.'})
    chat = ChatService.get_ai_response(message)
    return Response({'question': chat.question, 'reply': chat.answer})
