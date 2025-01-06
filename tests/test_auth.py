from app.auth import SpotifyAuth

def test_get_auth_url():
    auth = SpotifyAuth("client_id", "client_secret", "http://localhost/callback")
    url = auth.get_auth_url("user-read-private")
    assert "client_id" in url
    assert "user-read-private" in url
