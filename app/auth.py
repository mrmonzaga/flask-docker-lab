from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

def register_user(db, data):
    existing = db.users.find_one({"username": data["username"]})
    if existing:
        return {"error": "Username already exists"}, 400
    
    hashed = generate_password_hash(data["password"])
    db.users.insert_one({
        "username": data["username"],
        "password": hashed
    })
    return {"message": "User registered successfully"}, 201

def login_user(db, data):
    user = db.users.find_one({"username": data["username"]})
    if not user:
        return {"error": "User not found"}, 404
    
    if not check_password_hash(user["password"], data["password"]):
        return {"error": "Invalid password"}, 401
    
    return {"message": "Login successful", "username": data["username"]}, 200