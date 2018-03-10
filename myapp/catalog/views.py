#myapp/catalogue/views.py
#coding:"utf-8"

#third party imports
from flask import request, jsonify

#local imports
from . import catalog
from .. import db
from ..models import Product,Category

@catalog.route('/')
@catalog.route('/home')
def home():
    return jsonify("Welcome to the Catalog Home.")

#by default routes use GeT method
@catalog.route('/product/<int:id>')
def product(id): 
    try:
        product = Product.query.filter_by(id=id).first()
        product = {'Product':product.name,'Price':product.price}
        return jsonify(product)
    except AttributeError:
        return jsonify("Product does not exist.")


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
    return 'Category created'

@catalog.route('/product-create', methods=['POST'])
def create_product():
    name = request.form.get('name')
    price = request.form.get('price')
    category_name = request.form.get('category')
    category = Category.query.filter_by(name=category_name).first()
    product = Product(name, price,category)
    db.session.add(product)
    db.session.commit()
    return 'Product created.'

@catalog.route('/product-update/<int:id>',methods=['GET','PUT'])
def update_product(id):
    if request.method == "PUT":
        product = Product.query.filter_by(id=id).first()
        product.name = request.form.get('name')
        product.price = request.form.get('price')
        category_name = request.form.get('category')
        product.category = Category.query.filter_by(name=category_name).first()
        db.session.commit() 
        

    return jsonify('Method Not Allowed')

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
    return jsonify(response)
    





































