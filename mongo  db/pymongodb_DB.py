import pymongo
import dns
import os
import sys
import pprint

def main():
    #url = 'mongodb://MaddieComp:<password>@cluster0-v2sep.mongodb.net/test?retryWrites=true'
    
    url = 'mongodb+srv://{}:{}@{}/{}'.format (
        os.environ["MONGO_USERNAME"],
        os.environ["MONGO_PASSWORD"],
        os.environ["MONGO_HOST"],
        os.environ["MONGO_DBNAME"]
    )

    client = pymongo.MongoClient(url)
    db = client[os.environ["MONGO_DBNAME"]]
    collection = db['start'] #put the name of your collection in the quotes
    
    #1. print the number of documents in collection
    print(collection.count_documents({}))
    #2. print the first document in the collection
    print(collection.find_one({}))
    #3. print all documents in the collection
    for p in collection.find({}):
        print(p)
    #4. print all documents with a particular value for some attribute
    #ex. print all documents with the birth date 12/1/1990
    for n in collection.find(None,{'city'}):
        print(n)
if __name__=="__main__":
    main()