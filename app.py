from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request,redirect,url_for

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
    

@application.route('/search', methods=['GET', 'POST'])
def search(): #FIXME
    if request.method != 'POST':
        return redirect(url_for('showProduct'))

    query = request.form.get('query', None)
    print "SEARCH_QUERY-->"+query
    if query:
        return redirect(url_for('search_results', query=query))
    else:
        return redirect(url_for('showProduct'))


@application.route('/product/<query>', defaults={'page': 1})
@application.route('/product/<query>/page-<int:page>')
def search_results(page,query): #FIXME
    print "SEARCH_RESULTS_QUERY-->"+query

    STR = "Amazon - Fire TV Stick" #FIXME
    product = getProduct(STR) #FIXME
    return render_template('index.html', product=product)


@application.route('/', methods=['GET', 'POST'])
def showProduct():
    STR = "Duracell - AAA Batteries (4-Pack)" #FIXME
    product = getProduct(STR) #FIXME
    return render_template('index.html', product=product)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
