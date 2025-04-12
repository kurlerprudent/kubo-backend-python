import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()


from pymongo import MongoClient

# You can change this when you use a cloud hosted version of the database
client = MongoClient('localhost',27017)

# MONGO_URI = os.getenv("MONGO_URI") or 
# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

db = client["hospital_system"]

