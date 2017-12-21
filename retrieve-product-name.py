import json

f = open('products.json', 'r')
products = json.load(f)

names = []

for name in products:
    names.append({'name':name.get('name')})

with open('product-names.json', 'w') as outf:
    json.dump(names,outf)
