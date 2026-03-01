from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from crud import init_db, get_items, add_item, delete_item
from auth import register_user, login_user

app = Flask(__name__, static_folder='.')
CORS(app)
db = init_db()

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result, status = register_user(db, data)
    return jsonify(result), status

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result, status = login_user(db, data)
    return jsonify(result), status

@app.route('/items', methods=['GET'])
def read_items():
    return jsonify(get_items(db))

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    return jsonify(add_item(db, data))

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item_route(item_id):
    return jsonify(delete_item(db, item_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)