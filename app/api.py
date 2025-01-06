import requests

class SpotifyAPI:
    BASE_URL = "https://api.spotify.com/v1"

    def __init__(self, access_token):
        self.access_token = access_token

    def _headers(self):
        return {"Authorization": f"Bearer {self.access_token}"}

    def get_current_user(self):
        """Fetch the current user's profile."""
        response = requests.get(f"{self.BASE_URL}/me", headers=self._headers())
        return response.json()

    def get_user_playlists(self):
        """Fetch the current user's playlists."""
        response = requests.get(f"{self.BASE_URL}/me/playlists", headers=self._headers())
        return response.json()

def get_current_user(self):
    """Fetch the current user's profile."""
    response = requests.get(f"{self.BASE_URL}/me", headers=self._headers())
    print("Raw API Response:")
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    response.raise_for_status()  # Raise an exception for HTTP errors

    if not response.text.strip():  # Handle empty response body
        raise Exception("API returned an empty response.")
    
    return response.json()
