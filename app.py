from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

inventory_db = []
data = requests.get('https://dummyjson.com/products')

products = data.json().get('products')

for product in products:
    product_inventory = {
        'product_id': product.get('id'),
        'stock': product.get('stock')
    }

    inventory_db.append(product_inventory)

@app.route('/stock/<int:product_id>', methods=['GET'])
def find_stock_by_id(product_id):
    for product in inventory_db:
        if product['product_id']==product_id:
            return jsonify(product), 200
        
@app.route('/change/<int:product_id>/<int:new_value>', methods=['POST'])
def change_product_stock(product_id, new_value):
    for product in inventory_db:
        if product['product_id']==product_id:
            product['stock']=new_value
            return jsonify({'message': 'product has been updated'})
        
app.run(debug=True, host='0.0.0.0')

