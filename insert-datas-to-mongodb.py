import json
from pymongo import MongoClient

client = MongoClient('35.224.255.11:27017')
db = client.test.products

f = open('products.json', 'r')
products = json.load(f)

for product in products:
  db.insert_one({
    "sku":product['sku'],
    "name":product['name'],
    "type":product['type'],
    "price":product['price'],
    "upc":product['upc'],
    "category":product['category'],
    "shipping":product['shipping'],
    "description":product['description'],
    "manufacturer":product['manufacturer'],
    "model":product['model'],
    "url":product['url'],
    "image":product['image']
  })
