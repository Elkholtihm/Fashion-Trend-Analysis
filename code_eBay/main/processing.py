from pymongo import MongoClient
import os
import json
import sys
import os
from decouple import config
# Add the parent directory to sys.path to allow imports from src
sys.path.append(os.path.abspath("../"))

# Now import the function
from src.cleaner import extract_price
from src.cleaner import clean_location
from src.cleaner import categorize_delivery
from src.cleaner import extract_feedback_count,update_item
from src.cleaner import clean_delivery_price
from models.categorize import assign_category
from models.sentiment_analyser import average_sentiment
from models.categorize import get_dominant_color
# Connect to MongoDB running on localhost and default port 27017

IMAGES_PATH = config('IMAGES_PATH')

client = MongoClient("mongodb://localhost:27017/")


data=client['ebay_market']['Products'].find()
data = list(data)  # Convert cursor to list

prices=list(map(lambda x:extract_price(x['price']),data))

data_with_price_handled = list(map(lambda item_price: {**item_price[0], 'price': item_price[1]}, zip(data, prices)))

data_with_location_handled = [{**item, 'location': clean_location(item['location'])} for item in data_with_price_handled]

data_with_delivery_handled = [{**item,'delivery_category':categorize_delivery(item['delivery_price'])} for item in data_with_location_handled]

for item in data_with_delivery_handled:
    item['clean_delivery_price'] = clean_delivery_price(item['delivery_price'], item['delivery_category'])

for item in data_with_delivery_handled:
    item.pop('delivery_type', None)

for item in data_with_delivery_handled:
    item.pop('date', None)

enhanced_data = config('ENHANCED_DATA_PATH')

with open(enhanced_data, 'r', encoding='utf-8') as f:
    new_data = json.load(f)

# Update each item in the new data with feedback count and clean delivery price
data_with_feedback_count=[{**d1_item, **{k: v for k, v in d2_item.items() if k not in d2_item}} for d1_item, d2_item in zip(data_with_delivery_handled, new_data)]

data_with_feedback_count=list(map(update_item, data_with_feedback_count))

for item in data_with_feedback_count:
    item['category'] = assign_category(item['title'])


data_with_sentiment_analysis=[{**item, 'average_sentiment': average_sentiment(item["feedback"])} for item in data_with_feedback_count]

colors=[{image.split('.')[0]:get_dominant_color(image)} for image in os.listdir(IMAGES_PATH)]

from collections import ChainMap
dict_colors=dict(ChainMap(*colors))

data_with_predicted_color=[{**item, 'product_look_like_color': dict_colors[str(index)]} for index,item in enumerate(data_with_sentiment_analysis) ]

# Insert the processed data into the MongoDB collection
collection = client['ebay_market']['processed_products']
collection.insert_many(data_with_predicted_color)