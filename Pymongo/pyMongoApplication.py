from pymongo import MongoClient

import datetime
import pprint

client = MongoClient(
    "mongodb+srv://snamuelfilho2011:X4r4Ahv69Ue5wi39@cluster0.igugwrj.mongodb.net/?retryWrites=true&w=majority"
)

db = client.test
collection = db.test_collection
print(db.test_collection)  # Retorna as propriedades do cluster

# Definição de informações para compor o documento
post = {
    "author": "Mike",
    "text": "My First MongoDB Application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# Preparando para submeter as Infos
posts = db.posts
posts_id = posts.insert_one(post).inserted_id  # Inserindo um Documento
print(posts_id)

print(db.list_collection_names())  # Retorna os Nomes Da Coleções Do Banco De Dados
print(db.posts.find_one())  # Recupera um Documento do Mongo Db

pprint.pprint(db.posts.find_one())  # Mostra de Forma Identada o Documento

# bulk inserts
new_posts = [
    {
        "author": "Mike",
        "text": "Another Post",
        "tags": ["bulk", "post", "insert"],
        "date": datetime.datetime.utcnow()
    },
    {
        "author": "João",
        "text": "Post from Joao, new Post available",
        "title": "Mongo is Fun",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    }
]

result = posts.insert_many(new_posts)  # Inserindo Varios Documento
print(result.inserted_ids)

print("\n Recuperação Final")
pprint.pprint(db.posts.find_one({"author": "João"}))

print("\n Documentos Presentes na Coleção Post")
for post in posts.find():  # Recuperando os Documentos Da Coleção Post
    pprint.pprint(post)
