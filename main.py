from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import users_collection
from models import User
from bson import ObjectId
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    password = password.encode("utf-8")[:72]
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password = plain_password.encode("utf-8")[:72]
    return pwd_context.verify(plain_password, hashed_password)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-flax-alpha-40.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)       

@app.get("/")
def root():
    return {"msg": "Backend running"}


@app.post("/register")
def register_user(user: User):
    user_dict = user.dict()

    user_dict["password"] = hash_password(user.password)

    users_collection.insert_one(user_dict)
    return {"msg": "User registered securely"}

   

@app.post("/login")
def login(email: str, password: str):
    user = users_collection.find_one({"email": email})

    if not user:
        return {"error": "Invalid email"}

    if not verify_password(password, user["password"]):
        return {"error": "Invalid password"}

    return {
        "msg": "Login successful",
        "user_id": str(user["_id"])
    }

@app.get("/user/{user_id}")
def get_user(user_id: str):
    user = users_collection.find_one(
        {"_id": ObjectId(user_id)},
        {"password": 0}  
    )

    if not user:
        return {"error": "User not found"}

    user["_id"] = str(user["_id"])
    return user