from pymongo import MongoClient

db_connection = MongoClient("mongodb://mongodb:27017")
db = db_connection.todo_list
