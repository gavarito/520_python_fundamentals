#!/usr/bin/python3

from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

try:
    con = MongoClient()
    db = con['client']
    # db.pessoas.insert({"nome":"joao", "idade":49})
    # db.pessoas.insert({"nome":"jefter", "idade":24})
    # db.pessoas.insert({"nome":"eurides", "idade":89})
    # db.pessoas.update({"nome":"jessica"},{'$set':{'sobrenome':'santos'}})
    db.pessoas.remove({'_id':ObjectId('5b534974e3d0b510b417385e')})
    documento =  [doc for doc in db.pessoas.find()]
    pprint(documento)
except Exception as e:
    print('Erro: {}'.format(e))