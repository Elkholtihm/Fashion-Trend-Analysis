from pymongo import MongoClient
import json
client= MongoClient("mongodb://localhost:27017/")
from decouple import config

db=client['ebay_market']

collection=db['Products']
# Assuming your JSON data is loaded into a variable called `data`
# Example: data = [{"name": "item1", "price": 10}, {"name": "item2", "price": 20}]
path_to_data=config('ROW_DATA_PATH')
with open(path_to_data, 'r',encoding='utf-8') as file:
    data = json.load(file)

collection.insert_many(data)