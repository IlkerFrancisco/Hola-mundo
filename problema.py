import pymongo
from pymongo import MongoClient
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception                

client = MongoClient("mongodb+srv://ilker:12345@cluster0.qkysx.mongodb.net/Prueba?retryWrites=true&w=majority")

db = client["Prueba"]
collection = db["Prueba"]

mydoc = collection.find().sort("_id", 1)

for x in mydoc:
  print(x["_id"],x["name"])


