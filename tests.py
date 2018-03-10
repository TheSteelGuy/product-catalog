#tests.py
#coding:"utf-8"
import os

import unittest
from flask_testing import TestCase
from flask import url_for
from myapp.models import Product, Category
import json

from myapp import create_app,db
from myapp.models import Product, Category

class TestBase(TestCase):

  def create_app(self):
    
    config_name = 'testing'
    self.app = create_app(config_name)
    self.app.config.update(SQLALCHEMY_DATABASE_URI= "postgresql://postgres:postgres@localhost/test_catalog"
    #self.app.config.update(SQLALCHEMY_DATABASE_URI= "mysql://root:collo0@localhost/test_catalog"
    )
    return self.app

  def setUp(self):
    """called before  any test"""
    #create tables
    self.client = self.app.test_client()
    self.product = {
       'name':'testproduct',
       'price': 56.0,
       'category':'ipods'
     } 
    db.create_all()
  

  def tearDown(self):
    """gets run after every test"""
    db.session.remove()
    db.drop_all()
    
    

class TestModels(TestBase):
    """test the number of records in product tables"""

    def test_category_model(self):
        category = Category(name="smartphone")
        db.session.add(category)
        db.session.commit()
        self.assertEqual(Category.query.count(),1)
         

    def test_product_model(self):
        product = Product(name="Nokia",price=45.0,category=Category(name="smartphone"))
        db.session.add(product)
        db.session.commit()
        self.assertEqual(Product.query.count(),1)

  
    
class Testviews(TestBase):
    """ tests for views"""
   
    def test_homepage(self):
       """tests if homepage is accessible with no login"""
       response = self.client.get(url_for('catalog.home'))
       self.assertEqual(response.status_code,200)

    def test_product(self):
      """tests if products are accesible without login"""
      response = self.client.get(url_for('catalog.products')) 
      self.assertEqual(response.status_code,200)

      """def test_single_product(self): 
       response = self.client.get(url_for('catalog.product'),values=[id]) 
       self.assertEqual(response.status_code,200) """

    def test_product_update(self):
      """test if update possible"""
      self.client.post(
        '/product-create',
        data=json.dumps(self.product),
        content_type ='application/json'
      )
      new_product = {
          'name':'new name',
          'price':45.0,
          'category':'new category'
      }
      update = self.client.put(
        '/product-update/1',
        data=json.dumps(new_product),
        content_type='application/json'
      )
      self.assertIn('Product updated',update.data)

    def test_product_create(self):
      """test if update possible"""
      result = self.client.post(
        '/product-create',
        data=json.dumps(self.product),
        content_type ='application/json'
      )
      self.assertEqual(result.status_code,201)
    def test_create_category(self):
      """ tests creation of category"""
      result = self.client.post(
        '/create-category',
        data=json.dumps({'name':'Tablets'}),
        content_type='application/json'
      )
      self.assertIn('Category created',result.data)
    def test_categories(self):
      '''tests get requests to categeories'''
      result = self.client.get(url_for('catalog.get_categories'))
      self.assertEqual(result.status_code,200)



if __name__ == ('__main__'):
   unittest.main()











   
    

