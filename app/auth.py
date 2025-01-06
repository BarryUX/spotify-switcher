import requests


class SpotifyAuth:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token_url = "https://accounts.spotify.com/api/token"
        self.auth_url = "https://accounts.spotify.com/authorize"

    def get_auth_url(self, scopes):
        """Generate the Spotify authorization URL."""
        auth_url = (
            f"{self.auth_url}?client_id={self.client_id}"
            f"&response_type=code"
            f"&redirect_uri={self.redirect_uri}"
            f"&scope={scopes}"
        )
        return auth_url

    def get_tokens(self, auth_code):
        """Exchange the authorization code for access and refresh tokens."""
        payload = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        try:
            response = requests.post(self.token_url, data=payload)
            # Debug: Print the raw response
            print("Raw Token Response:")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")
            print(f"Request Payload: {payload}")

            if response.status_code != 200:
                raise Exception(f"Token exchange failed: {response.status_code} - {response.text}")

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to exchange tokens: {e}")

    def refresh_token(self, refresh_token):
        """Use the refresh token to obtain a new access token."""
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        try:
            response = requests.post(self.token_url, data=payload)
            # Debug: Print the raw response
            print("Raw Refresh Response:")
            print(f"Status Code: {response.status_code}")
            print(f"Response Body: {response.text}")
            print(f"Request Payload: {payload}")

            if response.status_code != 200:
                raise Exception(f"Refresh token exchange failed: {response.status_code} - {response.text}")

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to refresh tokens: {e}")
