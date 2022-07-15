==================================================intall========================================
pip install elasticsearch
pip install elasticsearch[async]


==================================================in python========================================
from elasticsearch import Elasticsearch

#connect
es = Elasticsearch('http://localhost:9200')

#create index in elastic this need insdex and id, this lie db in sql, not concept index in sql, if run again update date
resp = es.index(index='<name>', id=<id>, document=<dictionary python>)  #if dont use id elastic define automate objectid
print(resp)                #show information
print(resp['result'])


#get data information of elastic
resp = es.get(index='<name>', id=1)   #get information of index with id in elastic
print(resp['_source'])


#search in elastic
resp = es.search(index='<name>', query={'match_all': {})
print(resp)                       #return all information about index, data
print(resp['hits']['hits'])       #return all data and information
for hit in resp['hits'][hits']:
    print(hit)                    #return dittionary python of data


#update document in elastic
resp = es.update(index='<name>', id=<id>, document=<dictionary python>
print(resp['result'])
                 
#delete document                
es.delete(index='<name>', id=<id>)









==================================================cluster sngle node========================================
version: "3.9"
services:
  elasticsearch:
    image: elasticsearch:8.2.2
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    volumes:
      - es_data:/usr/share/elasticsearch/data
    ports:
      - target: 9200
        published: 9200
    networks:
      - elastic

  kibana:
    image: kibana:8.2.2
    ports:
      - target: 5601
        published: 5601
    depends_on:
      - elasticsearch
    networks:
      - elastic      

volumes:
  es_data:
    driver: local

networks:
  elastic:
    name: elastic
    driver: bridge

==================================================cluster multi nodes========================================
version: '2.2'
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.6.1
    container_name: es01
    environment:
      - node.name=es01
      - cluster.name=es-docker-cluster
      - discovery.seed_hosts=es02,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data01:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    networks:
      - elastic
  es02:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.6.1
    container_name: es02
    environment:
      - node.name=es02
      - cluster.name=es-docker-cluster
      - discovery.seed_hosts=es01,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data02:/usr/share/elasticsearch/data
    networks:
      - elastic
  es03:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.6.1
    container_name: es03
    environment:
      - node.name=es03
      - cluster.name=es-docker-cluster
      - discovery.seed_hosts=es01,es02
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data03:/usr/share/elasticsearch/data
    networks:
      - elastic

volumes:
  data01:
    driver: local
  data02:
    driver: local
  data03:
    driver: local

networks:
  elastic:
    driver: bridge