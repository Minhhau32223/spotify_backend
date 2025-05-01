"""
URL configuration for backend_spotify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from music.views import SongViewSet, AlbumViewSet, UserViewSet, PlaylistViewSet, FavoriteSongViewSet,ArtistViewSet, PlaylistSongViewSet, SongsInAlbumView, SongsInPlaylistView, chat_with_ai
from music import views
from .authentication import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# router = routers.DefaultRouter()
# router.register(r'songs', SongViewSet)
# router.register(r'albums', AlbumViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'playlists', PlaylistViewSet)
# router.register(r'playlist-songs', PlaylistSongViewSet)
# router.register(r'favorite-songs', FavoriteSongViewSet)
# router.register(r'artists', ArtistViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    # path('albums/<int:album_id>/songs/', SongsInAlbumView.as_view(), name='songs-in-album'),
    # path('playlists/<int:playlist_id>/songs/', SongsInPlaylistView.as_view(), name='songs-in-playlist'),
    # path('api/', include('music.urls')),
      # ------- User --------
    path('api/users/', views.get_all_users, name='get_all_users'),
    path('api/users/<int:user_id>/', views.get_user_detail, name='get_user_detail'),

    # ------- Album --------
    path('api/albums/', views.get_all_albums, name='get_all_albums'),
    path('api/albums/<int:album_id>/', views.get_album_detail, name='get_album_detail'),
    path('api/albums/<int:album_id>/songs/', views.get_songs_in_album, name='songs_in_album'),

    # ------- Song --------
    path('api/songs/', views.get_all_songs, name='get_all_songs'),
    path('api/songs/<int:song_id>/', views.get_song_detail, name='get_song_detail'),

    # ------- Artist --------
    path('api/artists/', views.get_all_artists, name='get_all_artists'),
    path('api/artists/<int:artist_id>/', views.get_artist_detail, name='get_artist_detail'),

    # ------- Playlist --------
    path('api/playlists/', views.get_all_playlists, name='get_all_playlists'),
    path('api/playlists/<int:playlist_id>/', views.get_playlist_detail, name='get_playlist_detail'),
    path('api/playlists/<int:playlist_id>/songs/', views.get_songs_in_playlist, name='songs_in_playlist'),

    # ------- Playlist Song --------
    path('api/playlist-songs/', views.get_all_playlist_songs, name='get_all_playlist_songs'),
    path('api/playlist-songs/<int:ps_id>/', views.get_playlist_song_detail, name='get_playlist_song_detail'),

    # ------- Favorite Song --------
    path('api/favorite-songs/', views.get_all_favorite_songs, name='get_all_favorite_songs'),
    path('api/favorite-songs/<int:fs_id>/', views.get_favorite_song_detail, name='get_favorite_song_detail'),

    # ------- AI Chatbot --------
    path('api/chat/', views.chat_with_ai, name='chat_with_ai'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
