from datetime import timedelta
from json import dumps

from redis import Redis

r = Redis(port=7777, charset="utf-8", decode_responses=True)


def put_config(key, conf, expiration=None):
  r.hmset(key, conf)
  if not expiration is None: 
    expiration = timedelta(**expiration)
    r.expire(key, expiration)


def show_config(key):
  print(dumps(r.hgetall(key), indent=2))
