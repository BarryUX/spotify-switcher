import json
import os

TOKEN_FILE = "data/tokens.json"

def save_tokens(profile, tokens, profile_details=None):
    """Save tokens and profile details for a specific profile to a file."""
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            all_profiles = json.load(f)
    else:
        all_profiles = {}

    # Merge tokens and optional profile details
    all_profiles[profile] = {**tokens, **(profile_details or {})}

    # Save to file
    with open(TOKEN_FILE, "w") as f:
        json.dump(all_profiles, f, indent=4)

def load_tokens(profile):
    """Load tokens for a specific profile from a file."""
    if not os.path.exists(TOKEN_FILE):
        return None
    with open(TOKEN_FILE, "r") as f:
        all_profiles = json.load(f)
    return all_profiles.get(profile)
