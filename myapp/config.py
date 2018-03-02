#myapp/config.py
import os

class Baseconfig():

     ''' common as the class is inherited'''
     DEBUG = False
     SECRET = os.getenv("SECRET")
     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

 
class Development_config(Baseconfig):

     ''' development configaration'''

     DEBUG = True
     SQLALCHEMY_ECHO = True
     


class Production_config(Baseconfig):

      ''' production class'''

      DEBUG = False
      SQLALCHEMY_ECHO = False

class Testing_config(Baseconfig):
      TESTING = True



app_config = {'development':Development_config,
              'production' :Production_config,
              'testing'    :Testing_config

}

