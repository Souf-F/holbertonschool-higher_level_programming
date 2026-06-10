#!/usr/bin/python3
"""
API Security and Authentication with Basic Auth and JWT.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth."""
    if username in users:
        if check_password_hash(users[username]['password'], password):
            return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token."""
    return jsonify({"error": "Token has expired"}), 401


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Protected route with basic authentication."""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Login endpoint to get JWT token."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify(
            {"error": "Username and password required"}
        ), 400

    username = data['username']
    password = data['password']

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]['role']}
    )

    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Protected route with JWT authentication."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Admin-only protected route."""
    identity = get_jwt_identity()
    current_user = users[identity]

    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
