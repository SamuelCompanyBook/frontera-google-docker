
### clean your containers (warning this will clean all containers)

For this to work you have to start with brand new containers
otherwise you will get the error: Hbase_thrift.AlreadyExists: AlreadyExists(message=b'table name already in use')
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

### start the 3 containers (hbase, kafka, containerWithPython(to run spider + dbw + sw))

```
docker-compose up --force-recreate
```
After 1 minute of seeing the docker logs you will see: ERROR: An HTTP request took too long to complete.
This is not a problem, keep going.

### run command to create the hbase crawler db

```
docker exec -it fronteragooglemaster_hbase-docker_1 bash -c "echo -e \"create_namespace 'crawler'\nexit\" > commands.hbase && /opt/hbase/bin/hbase shell ./commands.hbase"
```


### start the dbw

connect to the python container and run dbw
```
docker exec -it fronteragooglemaster_spider_1 bash
python -m frontera.worker.db --config bc.config.dbw
```

### start the sw

connect to the python container again and run sw
```
docker exec -it fronteragooglemaster_spider_1 bash
python -m frontera.worker.strategy --config bc.config.sw --partition-id 0
```

### start the spider 

connect to the python container again and run the spide
```
docker exec -it fronteragooglemaster_spider_1 bash
scrapy crawl bc -L DEBUG -s SEEDS_SOURCE='./seeds.txt' -s SPIDER_PARTITION_ID=0 -s FRONTERA_SETTINGS=bc.config.spider
```

but no page get crawled:
```
[scrapy] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
```
