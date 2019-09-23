from elasticsearch import Elasticsearch
from elasticsearch import helpers
import uuid

# helpers nos permitirá a realizar el volado de los json
class es():

    def __init__(self,doc,index,type):
        
        self.doc = doc
        self.index = index
        self.type = type
        # Cambiar por la IP configurada en ES
        self.es = Elasticsearch(['192.168.0.12'],port=9200)
        # Usamos uuid para generar un random id
        self.id = uuid.uuid1()

    def InsertDoc(self):

        actions = [{"_index": self.index ,"_type":self.type,"_id": self.id ,"_source": self.doc}]
        helpers.bulk(self.es, actions)
