from rest_framework.decorators import api_view
from rest_framework.response import Response
from music.BUS.UserService import UserService
from music.BUS.AlbumService import AlbumService
from music.BUS.SongService import SongService
from music.BUS.PlaylistService import PlaylistService
from music.BUS.PlaylistSongService import PlaylistSongService
from music.BUS.FavoriteSong import FavoriteSongService
from music.BUS.ArtistService import ArtistService
import requests

# ---------- USER CONTROLLER ----------
@api_view(['GET'])
def get_all_users(request):
    users = UserService.get_all_users()
    return Response([u.__dict__ for u in users])

@api_view(['GET'])
def get_user_detail(request, user_id):
    user = UserService.get_user_by_id(user_id)
    return Response(user.__dict__) if user else Response({'error': 'Not found'}, status=404)

@api_view(['POST'])
def create_user(request):
    """
    Phương thức POST để tạo mới người dùng
    """
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({'error': 'Missing required fields'}, status=400)

    user = UserService.create_user(username, email, password)
    return Response(user.__dict__, status=201)

# ---------- ALBUM CONTROLLER ----------
@api_view(['GET'])
def get_all_albums(request):
    albums = AlbumService.get_all_albums()
    return Response([album.__dict__ for album in albums])

@api_view(['GET'])
def get_album_detail(request, album_id):
    album = AlbumService.get_album_by_id(album_id)
    return Response(album.__dict__) if album else Response({'error': 'Not found'}, status=404)
@api_view(['POST'])
def create_album(request):
    name = request.data.get('name')
    description = request.data.get('description')
    image = request.data.get('image')
    bg_color = request.data.get('bg_color')

    if not name or not description or not image or not bg_color:
        return Response({'error': 'Missing required fields'}, status=400)

    album = AlbumService.create_album(name, description, image, bg_color)
    return Response(album.__dict__, status=201)

# ---------- SONG CONTROLLER ----------
@api_view(['GET'])
def get_all_songs(request):
    songs = SongService.get_all_songs()
    return Response([song.__dict__ for song in songs])

@api_view(['GET'])
def get_song_detail(request, song_id):
    song = SongService.get_song_by_id(song_id)
    return Response(song.__dict__) if song else Response({'error': 'Not found'}, status=404)
@api_view(['POST'])
def create_song(request):
    name = request.data.get('name')
    album_id = request.data.get('album_id')
    artist_id = request.data.get('artist_id')
    desc = request.data.get('desc')
    duration = request.data.get('duration')
    file = request.data.get('file')
    image = request.data.get('image')

    if not name or not album_id or not artist_id or not duration or not file or not image:
        return Response({'error': 'Missing required fields'}, status=400)

    song = SongService.create_song(name, file, image, desc, duration, album_id, artist_id)
    return Response(song.__dict__, status=201)

# ---------- ARTIST CONTROLLER ----------
@api_view(['GET'])
def get_all_artists(request):
    artists = ArtistService.get_all_artists()
    return Response([artist.__dict__ for artist in artists])

@api_view(['GET'])
def get_artist_detail(request, artist_id):
    artist = ArtistService.get_artist_by_id(artist_id)
    return Response(artist.__dict__) if artist else Response({'error': 'Not found'}, status=404)
@api_view(['POST'])
def create_artist(request):
    name = request.data.get('name')
    bio = request.data.get('bio')
    image = request.data.get('profile_image')

    if not name or not bio or not image:
        return Response({'error': 'Missing required fields'}, status=400)

    artist = ArtistService.create_artist(name, bio, image)
    return Response(artist.__dict__, status=201)
# ---------- PLAYLIST CONTROLLER ----------
@api_view(['GET'])
def get_all_playlists(request):
    playlists = PlaylistService.get_all_playlists()
    return Response([playlist.__dict__ for playlist in playlists])

@api_view(['GET'])
def get_playlist_detail(request, playlist_id):
    playlist = PlaylistService.get_playlist_by_id(playlist_id)
    return Response(playlist.__dict__) if playlist else Response({'error': 'Not found'}, status=404)
@api_view(['POST'])
def create_playlist(request):
    name = request.data.get('name')
    user_id = request.data.get('user_id')

    if not name or not user_id:
        return Response({'error': 'Missing required fields'}, status=400)

    playlist = PlaylistService.create_playlist(name, user_id)
    return Response(playlist.__dict__, status=201)
# ---------- PLAYLIST SONG CONTROLLER ----------
@api_view(['GET'])
def get_all_playlist_songs(request):
    playlist_songs = PlaylistSongService.get_all_playlist_songs()
    return Response([ps.__dict__ for ps in playlist_songs])

@api_view(['GET'])
def get_playlist_song_detail(request, ps_id):
    playlist_song = PlaylistSongService.get_playlist_song_by_id(ps_id)
    return Response(playlist_song.__dict__) if playlist_song else Response({'error': 'Not found'}, status=404)

@api_view(['POST'])
def create_playlist_song(request):
    playlist_id = request.data.get('playlist_id')
    song_id = request.data.get('song_id')

    if not playlist_id or not song_id:
        return Response({'error': 'Missing required fields'}, status=400)

    playlist_song = PlaylistSongService.create_playlist_song(playlist_id, song_id)
    return Response(playlist_song.__dict__, status=201)
# ---------- FAVORITE SONG CONTROLLER ----------
@api_view(['GET'])
def get_all_favorite_songs(request):
    favorite_songs = FavoriteSongService.get_all_favorite_songs()
    return Response([fs.__dict__ for fs in favorite_songs])

@api_view(['GET'])
def get_favorite_song_detail(request, fs_id):
    favorite_song = FavoriteSongService.get_favorite_song_by_id(fs_id)
    return Response(favorite_song.__dict__) if favorite_song else Response({'error': 'Not found'}, status=404)
@api_view(['POST'])
def create_favorite_song(request):
    user_id = request.data.get('user_id')
    song_id = request.data.get('song_id')

    if not user_id or not song_id:
        return Response({'error': 'Missing required fields'}, status=400)

    favorite_song = FavoriteSongService.create_favorite_song(user_id, song_id)
    return Response(favorite_song.__dict__, status=201)
# ---------- SONGS IN ALBUM ----------
@api_view(['GET'])
def get_songs_in_album(request, album_id):
    songs = SongService.get_songs_in_album(album_id)
    return Response([s.__dict__ for s in songs])

# ---------- SONGS IN PLAYLIST ----------
@api_view(['GET'])
def get_songs_in_playlist(request, playlist_id):
    songs = SongService.get_songs_in_playlist(playlist_id)
    return Response([s.__dict__ for s in songs])

# ---------- CHAT WITH AI ----------
GEMINI_API_KEY = "AIzaSyAeZXWWu-4iiv-CJgOuUqr869pmlulszPY"

def get_ai_response(message):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        body = {
            "contents": [
                {
                    "parts": [{"text": message}]
                }
            ]
        }
        response = requests.post(url, json=body)
        if response.status_code != 200:
            return "Xin lỗi, tôi không thể trả lời lúc này."
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Xin lỗi, hiện tại tôi không thể trả lời lúc này."

# Hàm xử lý câu hỏi từ người dùng
def get_database_response(message):
    # Kiểm tra nếu câu hỏi có liên quan đến người dùng (ví dụ: "Thông tin user id 1")
    if "user" in message and "id" in message:
        user_id = int(message.split('id')[-1].strip())  # Giả sử người dùng nhập 'user id 1'
        user = UserService.get_user_by_id(user_id)
        if user:
            return f"User found: {user.username}, Email: {user.email}"
        else:
            return "User not found."
    
    # Kiểm tra nếu câu hỏi có liên quan đến album (ví dụ: "Danh sách bài hát trong album X")
    elif "album" in message and "songs" in message:
        album_name = message.split('album')[-1].strip()  # Giả sử người dùng nhập 'album X songs'
        songs = AlbumService.get_songs_by_album(album_name)
        if songs:
            return "Songs in album: " + ", ".join([song.name for song in songs])
        else:
            return "No songs found for this album."
    
    return None  # Nếu câu hỏi không liên quan đến cơ sở dữ liệu, trả về None

@api_view(['POST'])
def chat_with_ai(request):
    user_message = request.data.get('message')
    if not user_message:
        return Response({'reply': "Bạn chưa nhập nội dung tin nhắn."})

    # Kiểm tra câu hỏi có liên quan đến dữ liệu trong cơ sở dữ liệu không
    db_reply = get_database_response(user_message)
    if db_reply:
        return Response({'reply': db_reply})

    # Nếu không có dữ liệu từ database, gọi Gemini API để trả lời
    ai_reply = get_ai_response(user_message)
    return Response({'reply': ai_reply})