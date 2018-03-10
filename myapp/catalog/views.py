#myapp/catalogue/views.py
#coding:"utf-8"

#third party imports
from flask import request, jsonify,make_response

#local imports
from . import catalog
from .. import db
from ..models import Product,Category

@catalog.route('/')
@catalog.route('/home')
def home():
    return make_response(jsonify({"message":"Welcome to the Catalog Home."})),200

#by default routes use GeT method
@catalog.route('/product/<int:id>')
def product(id): 
    try:
        product = Product.query.filter_by(id=id).first()
        product = {'Product':product.name,'Price':product.price}
        return make_response(jsonify(product)),200
    except AttributeError:
        return make_response (jsonify({"message":"Product does not exist."})),405


@catalog.route('/products')
def products():
    products = Product.query.all()
    res = {}
    for product in products:
         res[product.id] = {
                    'name': product.name,
                    'price': product.price,
                    'category': product.category.name
         }
    return jsonify(res)


@catalog.route('/create-category', methods=['POST'])
def create_category():
    name = request.form.get('name')
    category = Category(name) 
    db.session.add(category)
    db.session.commit()       
    return make_response(jsonify('Category created')),201

@catalog.route('/product-create', methods=['POST'])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    category_name = request.form.get('category')
    category = Category.query.filter_by(name=category_name).first()
    product = Product(name, price,category)
    db.session.add(product)
    db.session.commit()
    return make_response(jsonify({'message':'Product created.'})),201

@catalog.route('/product-update/<int:id>',methods=['GET','PUT'])
def update_product(id):
    if request.method == "PUT":
        product = Product.query.filter_by(id=id).first()
        product.name = request.form.get('name')
        product.price = request.form.get('price')
        category_name = request.form.get('category')
        product.category = Category.query.filter_by(name=category_name).first()
        db.session.commit() 
        return make_response(jsonify({'message':'Product updated'})),201
    return make_response(jsonify({'message':'Method Not Allowed'})),405

@catalog.route('/product/<int:id>/del',methods=['GET','DELETE'])
def delete_product(id):
    '''delete product'''
    if request.method == 'DELETE':
        db.session.delete(id)
        db.session.commit()
    return jsonify('You need to send  delete verb.')

  
@catalog.route('/categories',methods=['GET'])
def get_categories():
    categories = Category.query.all()
    response = {}
    for category in categories:
        response[category.id]={
         'name' : category.name 
        }
        for product in category.products:
           response[category.id]['products'] = {
             'id': product.id,
             'name': product.name,
            'price': product.price
           }
    return make_response(jsonify(response)),200
    





































