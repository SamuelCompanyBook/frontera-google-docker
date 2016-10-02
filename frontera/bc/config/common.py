# -*- coding: utf-8 -*-
from frontera.settings.default_settings import MIDDLEWARES

MAX_NEXT_REQUESTS = 256
SPIDER_FEED_PARTITIONS = 1
SPIDER_LOG_PARTITIONS = 1
DELAY_ON_EMPTY = 5.0

MIDDLEWARES.extend([
    'frontera.contrib.middlewares.domain.DomainMiddleware',
    'frontera.contrib.middlewares.fingerprint.DomainFingerprintMiddleware'
])

#--------------------------------------------------------
# Crawl frontier backend
#--------------------------------------------------------
QUEUE_HOSTNAME_PARTITIONING = True

MESSAGE_BUS='frontera.contrib.messagebus.kafkabus.MessageBus'
KAFKA_LOCATION = 'kafka:9092'
SCORING_GROUP = 'scrapy-scoring'
SCORING_TOPIC = 'frontier-score'

SPIDER_LOG_CONSUMER_BATCH_SIZE=1
SCORING_LOG_CONSUMER_BATCH_SIZE=1

#ZMQ_ADDRESS = 'spider'
#ZMQ_BASE_PORT = 5550
