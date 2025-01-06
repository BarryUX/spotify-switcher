from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route (GET)
@app.route('/', methods=['GET'])
def home():
    return "Welcome to Spotify Switcher!"

# Switch profile route (supports POST and GET for debugging)
@app.route('/switch-profile', methods=['GET', 'POST'])
def switch_profile():
    print(f"Request Method: {request.method}")
    if request.method == 'POST':
        data = request.json
        if not data or 'profile' not in data:
            return jsonify({"error": "Profile not specified"}), 400
        profile = data.get('profile')
        return jsonify({"message": f"Switched to {profile}!"})
    return "Switch Profile Route. Use POST to switch profiles."

# User profile route (GET)
@app.route('/user-profile', methods=['GET'])
def user_profile():
    # Simulate fetching user profile
    return jsonify({
        "name": "Spotify User",
        "profile": "default"
    })

# Custom error handler for 405 Method Not Allowed
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed. Check the HTTP method for this route."}), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
