#myapp/catlogue/models.py
#coding:"utf-8"


from myapp import db

class Product(db.Model):

   
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255))
   price = db.Column(db.Float)
   category_id = db.Column(db.ForeignKey('category.id'))
   category = db.relationship('Category', backref=db.backref('products',lazy='dynamic'))
   

   def __init__(self, name, price,category):
       self.name = name
       self.price = price
       self.category = category

   def __repr__(self):
       return '<Product %d>' % self.id

class Category(db.Model):

   
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "<Category{}>".format(self.id)
   
