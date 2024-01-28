# Import
from flask import Flask, request, jsonify

# Create app
app = Flask(__name__)

# Display Homepage
@app.route("/")
def home():
    return "This is the homepage, go to /get-user/<user_id> to search"

# Handling null user
@app.route("/get-user/")
def get_user_null():
    return "Please input a user id to search for."

# Get user route
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

# Creating a user
@app.route("/create-user", methods=["POST"])
def create_user():
    if request.method == "POST": # Verify we are using the post method.
        data = request.get_json()
        
    return jsonify(data), 201

# Run app
if __name__ == "__main__":
    app.run(debug=True)