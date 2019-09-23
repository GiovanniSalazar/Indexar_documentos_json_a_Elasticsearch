import elastic
import os
import fnmatch
import json

path='json/'

def LoopFiles():
    for f in os.listdir(path):
        if fnmatch.fnmatch(f,'*.json'):
            fullpath=path+f
            with open(fullpath, 'r') as myfile:
                data=myfile.read()
                obj = json.loads(data)
                elas=elastic.es(obj,'empleados','documentos')
                x=elas.InsertDoc()

LoopFiles()
