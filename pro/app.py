from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import pymysql

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)

# Database connection
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="medical_store_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# Register
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email=%s", (data['email'],))
        if cursor.fetchone():
            return jsonify({"message": "Email already registered"}), 400
        cursor.execute("""
            INSERT INTO users (username, email, phone, password)
            VALUES (%s, %s, %s, %s)
        """, (data['username'], data['email'], data['phone'], data['password']))
        conn.commit()
        return jsonify({"message": "Registered successfully"}), 201
    except Exception as e:
        print(e)
        return jsonify({"message": "Registration failed"}), 500
    finally:
        cursor.close()
        conn.close()

# Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (data['email'], data['password']))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(identity=user['user_id'])
    return jsonify(access_token=token, username=user['username'])

# Profile
from flask_jwt_extended import jwt_required, get_jwt_identity

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, username, email, phone, role FROM users WHERE user_id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404


# Search Medicine (mock)
@app.route('/search_medicine', methods=['POST'])
def search_medicine():
    data = request.get_json()
    name = data['medicine_name']
    return jsonify([
        {"medicine_name": name, "store_name": "Apollo", "stock": 10, "distance_km": 1.5},
        {"medicine_name": name, "store_name": "MedPlus", "stock": 7, "distance_km": 2.1}
    ])

if __name__ == '__main__':
    app.run(debug=True)
