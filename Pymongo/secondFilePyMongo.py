from pymongo import MongoClient

import pprint
import pymongo

client = MongoClient(

)

db = client.test  # Instancia o Banco De Dados
posts = db.posts  # Instancia a Coleção 'post'

for post in posts.find():
    pprint.pprint(post)

print(posts.count_documents({}))  # Contar Todos os Documentos
print(posts.count_documents({"author": "Mike"}))  # Contar Apenas com o Author Mike
print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))

print("\n Recuperando Info Da Coleção Post De Maneira Ordenada")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([("author", pymongo.ASCENDING)], unique=True)
print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'name': "luke"},
    {'user_id': 212, 'name': 'Joao'}
]

result = db.profile_user.insert_many(user_profile_user)

print("\nPrint Coleções Armazenda no Mongo DB")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

pprint.pprint(db.profiles.find_one())

print(posts.delete_one({"author": "Mike"}))  # Apagar um Campo Do Documento
print(db.profile_user.drop())  # Apagar Toda Coleção

client.drop_database('test')  # Apagar o Banco De Dados

print(db.list_collection_names())
