from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)
# Read DB connection from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/posts', methods=['GET'])
def posts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, content FROM posts ORDER BY id DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([
        {"id": row[0], "title": row[1], "content": row[2]}
        for row in rows
    ])

@app.route('/add-post', methods=['POST'])
def add_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", (title, content))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Post added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

