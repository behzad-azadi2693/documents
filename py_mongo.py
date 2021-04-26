import pymongo

#---connect---
my_client = pymongo.MongoClient("mongodb://localhost:27017/") #create connect with mongodb


#----create db and collection----
my_db = my_client['product'] #create new (DB)
db_list = my_client.list_database_names() #list of (DBs) exists in mongo
if 'product' in db_list: #checking (DB) is exists
    print('The database exists')

my_col = my_db['customers'] #create collection(tabel)
col_list = my_db.list_collection_names() #get all list of collections(table)
if 'customers' in col_list: #check for collection is exists
    print('The collection exists')


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
