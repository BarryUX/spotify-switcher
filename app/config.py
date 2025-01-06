from dotenv import load_dotenv
import os

# Load environment variables
print("Loading .env...")
load_dotenv()

# Spotify app credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPES = "user-read-private user-read-email playlist-read-private"

# Print to confirm they are loaded
print(f"CLIENT_ID: {CLIENT_ID}")
print(f"CLIENT_SECRET: {CLIENT_SECRET}")
print(f"REDIRECT_URI: {REDIRECT_URI}")
