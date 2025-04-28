from music.DAO.ChatDAO import ChatDAO
from music.DTO.ChatDTO   import ChatDTO

class ChatService:
    @staticmethod
    def get_ai_response(message):
        answer = ChatDAO.send_to_gemini(message)
        return ChatDTO(question=message, answer=answer)
