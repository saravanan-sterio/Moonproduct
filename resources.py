from falcon_autocrud.resource import CollectionResource, SingleResource
from models import *
# /moonproduct
class RetailerCollectionResource(CollectionResource):
 model=moonproduct
# /moonproduct/{id}
class RetailerResource(SingleResource):
 model=moonproduct
