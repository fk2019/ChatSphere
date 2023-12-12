#!/usr/bin/env python3
"""Cache info using redis"""
import redis
from os import getenv
from dotenv import load_dotenv

load_dotenv()

port = getenv('REDIS_PORT')
host = getenv('REDIS_HOST')
db = getenv('REDIS_DB')
pool = redis.ConnectionPool(host=host, port=port, db=db)

redis_client = redis.Redis(connection_pool=pool)
