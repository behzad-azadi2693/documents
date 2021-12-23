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



----database(DB)----

#create new document(DB)
create_db = connection['shop']
>>>use shop

#list document(DB)
list_db = connection.list_database_names()
>>>show dbs
>>>db.getMongo().getDBNames()

#number database(DB)
print(len(list_db))
>>>db.getMongo().getDBNames().length

#check exist database(DB)
if 'product' in list_db:
    print('The database exists')
>>>db.getMongo().getDBNames().indexof("shop")

#remove database(DB)
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
create_collection = create_db['products'] 
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

#insertOne data
my_dict = {'name':'samsung', 'price':10000}
one_data = collection.insert_one(my_dict) 
print(f'one_data output={one_data.inserted_id}') #get id document(record)
>>>db.products.insertOne({'name':'samsung', 'price':10000})

#insertMany data
list_data = [
    {'name': 'joey', 'address': 'germany'},
    {'name': 'jack', 'address': 'canada'},
    {'name': 'john', 'address': 'france'}    
]
many_data = collection.insert_many(list_data) #inpurt data in collection or create document(record)
print(f'many_data output={many_data.inserted_ids}')#get id documents(records)
>>>db.products.insertMany([{...},{....},{....}])

#searching(find) , query
sample_query = {'nmae':'samsung'}
advance_query = {'price':{'$gt':10000}}
regular_query = {'name':{'$regex':'^S'}}

findone = my_col.find_one() #get one data in collection
print(f'findone output={findone}')
>>>db.products.findOne()

for data in my_col.find(): #get many data in collection
    print(f'manydata={data}')
>>>db.products.find()

for data in my_col.find({}, {'_id':0,'name':1,'address':1}): #control output for show wich information 0=False 1=True
    print(data)
>>>db.products.find({},{'_id':0, 'name':1,'address':1})

my_doc = my_col.find(advance_equery).sort('_id', -1).limit(5) #-1=descending and 1=ascending
for data in my_doc:
    print(f'my_doc={data}')
>>>db.products.find({'price':{'$gt:9000'}).limit(5).sort({'_id':-1})

#delete
my_col.delete_one(sample_query)
>>>db.products.deleteOne(query)

delete = my_col.delete_many(regular_query)
print(f'number of delete={delete.deleted_count}')
>>>db.products.deleteMany(query)
                     
delete_all_col = my_col.delete_many({})
print(f'delete all collection={delete_all_col.deleted_count}')
>>>db.collection.remove({})

#updating
one_query = {'ame':'apple'}
new_value = {'$set':{'price':12000}}
my_col.update_one(one_query, new_value)
>>>db.products.updateOne(query, value)
                     
many_query = {'name':{'$regex':'^S'}}
new_values = {'$set':{'name':'LG'}}
output = my_col.update_many(many_query, new_values)
print(f'number data changed(updating)={output.modified_count}')
>>>db.products.updateMany(query, value)

                     
                     
---index---
         
#index
index = collection.create_index([("first_field-index", 1),("second_field_index", -1)]) 
print ("index response:", resp)
>>>db.product.createIndex({"first-fieeld-index":1, "second-field-index":-1})

#get all index
collection.index_information()     
>>>db.products.getIndexes()
                     
#remove index one
connection.collection.reindex("first-field-index")
>>>db.products.dropIndex("first-field-index")

#remove index many
connection.collection.drop_indexes({"first-fieeld-index":1, "second-field-index":1})
>>>db.products.dropIndexes({"first-fieeld-index":1, "second-field-index":1})
                     
                     
                     
---search---
#full text search                     
collection.create_index([('field_i_want_to_index', pymongo.TEXT)], name='column_name', default_language='english')
>>>db.products.createIndex({column_name:"text"})            

#key word search
collection.inseart_one({'name':'new','price':3000, 'key_search':["one-key","two-key"]}
collection.create_index(["key_search":1])
                     

                       
---relation---
collection = create_db['user']
collection_address = create_db['address']
    
#one to one
collection.insert_one({'name':'joe','address':{'city':'sanandaj','streeate':'one','phone':09120000000}})
                       
#one to many
collection_address.insert_many({'user_id':'joe', 'address':{'city':'sanandaj','streeate':'one','phone':09120000000},
                               'user_id':'joe', {'address':{'city':'sanandaj','streeate':'one','phone':09120000000}
                              })
 collection.insert_one({'name':'joe','address':[
                                                {'city':'sanandaj','streeate':'one','phone':09120000000},
                                                {'city':'sanandaj','streeate':'one','phone':09120000000}
                                               ]
                      })
                                
#many to many
collection.insert_one({'name':'joe', 'address':['address_id_1','address_id_2']})
                     
                     
