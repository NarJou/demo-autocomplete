from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request
from fabric.api import *

application = Flask(__name__)

client = MongoClient('0.0.0.0:27017')
db = client.products

@application.route('/')
def showProduct():
    return render_template('list.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')

