from sqlalchemy import create_engine
import falcon
from falcon_autocrud.middleware import Middleware
import psycopg2
from resources import *
db_engine = create_engine('postgresql+psycopg2://postgres:steriowolf@localhost/moonproduct')
app = application = falcon.API(middleware=[Middleware()])
app.add_route('/moonproduct',RetailerCollectionResource(db_engine))
app.add_route('/moonproduct/{id}',RetailerResource(db_engine))
