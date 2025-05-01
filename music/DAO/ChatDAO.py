import requests

GEMINI_API_KEY = "AIzaSyAeZXWWu-4iiv-CJgOuUqr869pmlulszPY"

class ChatDAO:
    @staticmethod
    def send_to_gemini(message):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        body = {
            "contents": [{"parts": [{"text": message}]}]
        }
        response = requests.post(url, json=body)
        if response.status_code == 200:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return "Xin lỗi, tôi không thể trả lời lúc này."
