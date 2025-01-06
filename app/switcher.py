from app.auth import SpotifyAuth
from app.api import SpotifyAPI
from app.config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES
from app.utils import save_tokens, load_tokens

if __name__ == "__main__":
    profile = input("Which profile would you like to use? (profile1/profile2): ").strip()

    # Initialize SpotifyAuth
    auth = SpotifyAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

    # Check and handle authentication
    tokens = load_tokens(profile)
    if not tokens or "access_token" not in tokens:
        print(f"No valid tokens found for {profile}. Reauthenticate.")
        print("Visit this URL to authorize the app:")
        print(auth.get_auth_url(SCOPES))
        auth_code = input("Enter the authorization code: ")
        tokens = auth.get_tokens(auth_code)
        save_tokens(profile, tokens)

    # Test the API with the new tokens
    print(f"Testing API with Access Token: {tokens['access_token']}")
    spotify = SpotifyAPI(tokens["access_token"])
    try:
        user_profile = spotify.get_current_user()
        print("User Profile Response:")
        print(user_profile)
    except Exception as e:
        print(f"Failed to fetch user profile: {e}")


print(f"Access Token for API Call: {tokens['access_token']}")
