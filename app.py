from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request

application = Flask(__name__)

client = MongoClient('35.224.255.11:27017')
db = client.test.products

def getProduct(key):
    try:
        productObject = db.find_one({'name':key})
        productDict = {
            'name':productObject['name'],
            'model':productObject['model'],
            'sku':productObject['sku'],
            'type':productObject['type'],
            'price':productObject['price']
            }
        return productDict
    except Exception, e:
        return str(e)

@application.route('/')
def showProduct():
    STR = "Duracell - AAA Batteries (4-Pack)" #FIXME
    product = getProduct(STR) #FIXME
    return render_template('index.html', product=product)

if __name__ == "__main__":
    application.run(host='0.0.0.0')

