from app.api import SpotifyAPI

def test_headers():
    api = SpotifyAPI("test_token")
    headers = api._headers()
    assert headers["Authorization"] == "Bearer test_token"
