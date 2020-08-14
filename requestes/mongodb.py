import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['test']
collection = db.students
"""student = {
    'id' : '20170101',
    'name' : 'Jordan',
    'gender' : 'male'
}
result = collection.insert(student)
print(result)
"""
result1 = collection.find({'name': 'Jordan'})
print(type(result1))
print(result1)
