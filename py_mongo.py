---install mongo on ubuntu---

sudo apt update
sudo apt install -y mongodb

sudo systemctl status mongodb
or service mongodb status

sudo systemctl start mongod
or service mongodb start

sudo systemctl stop mongod  or
service mongodb stop



---docker---

#pull of dockerhost
docker pull mongo

#run container mongo
docker run --name mongo -p 27017:27017 -d mongo

#mongoshel
docker exec -it mongo mongo
>>>mongo


---install driver pymongo---
python -m pip install pymongo
python -m pip install --upgrade pymongo
sudo apt-get install build-essential python-dev



-------------------------------START-------------------------------

#include driver
import pymongo



#---connection---

#create connect with mongodb
connection = pymongo.MongoClient("mongodb://localhost:27017/")
connection = pymongo.MongoClient('localhost', 27017)
>>>mongo



----document(DB)----

#create new document(DB)
create_document = connection['shop']
>>>use shop

#list document(DB)
list_document = connection.list_database_names()
>>>show dbs
>>>db.getMongo().getDBNames()

#number document(DB)
print(len(list_document))
>>>db.getMongo().getDBNames().length

#check exist document(DB)
if 'product' in list_db:
    print('The database exists')
>>>db.getMongo().getDBNames().indexof("shop")

#remove document(DB)
connection.drop_database('shop')
>>>db.dropDatabase()



---role and user---
#list user
>>>show users
>>>get.getUsers()

#create user
>>>db.createUser({user:"admin",pwd:"admin",roles:[{role:"userAdminAnyDatabase", db:"admin"}]})

#delete user
>>>db.removeUsers("admin")
>>>db.dropUser("admin")



---collection(table)---

#create collections(table)
create_collection = create_document['products'] 
>>>db.CreateCollection('products')

#list collections(table)
collection_list = create_collection.list_collection_names()
>>>show collections
>>>db.getCollectionNames()

#check for collection is exists
if 'products' in collection_list: 
    print('The collection exists')
    
#remove collection(table)
>>>create_collection.drop()
>>>db.products.drop()



#----insert-----
my_dict = {'name':'joe', 'address':'USA'} #we information
one_data = my_col.insert_one(my_dict) #inpurt data in collection or create document(record)
print(f'one_data output={one_data.inserted_id}') #get id document(record)


my_list = [
    {'name': 'joey', 'address': 'germany'},
    {'name': 'jack', 'address': 'canada'},
    {'name': 'john', 'address': 'france'}    
]#we information for many
many_data = my_col.insert_many(my_list) #inpurt data in collection or create document(record)
print(f'many_data output={many_data.inserted_ids}')#get id documents(records)


#----searching , queery----
sample_query = {'address':'USA'}
advance_query = {'address':{'$gt':'s'}}
regular_query = {'address':{'$regex':'^S'}}

findone = my_col.find_one() #get one data in collection
print(f'findone output={findone}')

for data in my_col.find(): #get many data in collection
    print(f'manydat={data}')
for data in my_col.find({}, {'_id':0,'name':1,'address':1}): #control output fro show wich information 0=False 1=True
    print(data)

my_doc = my_col.find(advance_equery).sort('name', -1).limit(5) #-1=descending and 1=ascending
for data in my_doc:
    print(f'my_doc={data}')


#----delete----
my_col.delete_one(sample_query)

delete = my_col.delete_many(regular_query)
print(f'number of delete={delete.deleted_count}')

delete_all_col = my_col.delete_many({})
print(f'delete all collection={delete_all_col.deleted_count}')

my_col.drop() #delete collection(table)


#----updating----
one_query = {'address':'canada'}
new_value = {'$set':{'address':'UKA'}}
my_col.update_one(one_query, new_value)

many_query = {'address':{'$regex':'^S'}}
new_values = {'$set':{'name':'minne'}}
output = my_col.update_many(many_query, new_values)
print(f'number data changed(updating)={output.modified_count}')
