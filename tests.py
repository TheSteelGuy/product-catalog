#tests.py
#coding:"utf-8"
import os

import unittest
from flask_testing import TestCase
from flask import url_for
from myapp.models import Product, Category


from myapp import create_app,db
from myapp.models import Product, Category

class TestBase(TestCase):

  def create_app(self):
    
    config_name = 'testing'
    app = create_app(config_name)
    app.config.update(SQLALCHEMY_DATABASE_URI= 'postgresql://cata:cata1@localhost/test_catalog'
    )
    return app

  def setUp(self):
    """called before  any test"""
    #create tables
    db.create_all()
    #create category for tests


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
     

if __name__ == ('__main__'):
   unittest.main()











   
    

