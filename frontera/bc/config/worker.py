# -*- coding: utf-8 -*-
from __future__ import absolute_import
from .common import *

BACKEND = 'frontera.contrib.backends.hbase.HBaseBackend'
HBASE_DROP_ALL_TABLES = True

MAX_NEXT_REQUESTS = 512
NEW_BATCH_DELAY = 3.0

HBASE_DROP_ALL_TABLES = False
HBASE_THRIFT_PORT = 9090
HBASE_THRIFT_HOST = 'hbase-docker'
#HBASE_QUEUE_TABLE = 'queue3'
#STORE_CONTENT = 'content3'
LOG_LEVEL='INFO'
LOGGING_ENABLED = True
LOGGING_EVENTS_ENABLED = True
LOGGING_MANAGER_ENABLED = True
LOGGING_BACKEND_ENABLED = True
LOGGING_DEBUGGING_ENABLED = True
CRAWLING_STRATEGY = 'bc.broadcrawl.BCPerHostLimit'
