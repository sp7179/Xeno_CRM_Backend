from pymongo import MongoClient
from config.settings import MONGO_URI, DATABASE_NAME

client = MongoClient(MONGO_URI)

db = client[DATABASE_NAME]




customers_collection = db["customers"]
users_collection = db["users"]
products_collection = db["products"]
orders_collection = db["orders"]
segments_collection = db["segments"]
campaigns_collection = db["campaigns"]
communications_collection = db["communication_logs"]
campaign_analytics_collection = db["campaign_analytics"]