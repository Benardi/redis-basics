import os
import logging
from json import loads, dumps
from datetime import timedelta
from argparse import ArgumentParser

from redis import Redis
from flask import Response, Flask, request

app = Flask(__name__)
log = logging.getLogger(__name__)

parser = ArgumentParser()
parser.add_argument("-a", "--address",
                    action="store", dest="address",
                    type=str, required=True,
                    help="Address for api")
parser.add_argument("-p", "--port",
                    action="store", dest="port",
                    type=str, required=True,
                    help="Port for api")
parser.add_argument("-c", "--crt",
                    action="store", dest="cert",
                    type=str, required=False,
                    help="Path to certificate for this API")
parser.add_argument("-k", "--key",
                    action="store", dest="key",
                    type=str, required=False,
                    help="Path to key of certificate used by this API")

parser.add_argument("-rp", "--redis-port",
                    action="store", dest="redis-port",
                    type=str, required=True,
                    help="Port for Redis client")

args = vars(parser.parse_args())

api_address = args["address"]
api_port = args["port"]
api_cert = args["cert"]
api_key = args["key"]

redis_port = args["redis-port"]
r = Redis(port=redis_port, charset="utf-8", decode_responses=True)


@app.route("/hash", methods=['POST'])
def create_redis_hash():
    data = loads(request.data)
    success = r.hmset(data["key"], data["pairs"])
    if data.get("expire") is not None:
      expiration = timedelta(**data.get("expire"))
      r.expire(data["key"], expiration)
    
    response_body = {"success": success}
    response_body[data["key"]] = r.hgetall(data["key"])
  
    return Response(dumps(response_body), status=200, mimetype="application/json")


@app.route("/hash", methods=['PUT'])
def update_redis_hash():
    data = loads(request.data)
    success = r.hmset(data["key"], data["pairs"])
    if data.get("expire") is not None:
      expiration = timedelta(**data.get("expire"))
      r.expire(data["key"], expiration)
    
    if data.get("newkey") is not None:
      r.rename(data["key"], data["newkey"])

    response_body = {"success": success}
    if data.get("newkey") is not None:
      response_body[data["newkey"]] = r.hgetall(data["newkey"])
    else:
      response_body[data["key"]] = r.hgetall(data["key"])
  
    return Response(dumps(response_body), status=200, mimetype="application/json")


@app.route("/hash", methods=['GET'])
def get_redis_hash():
    response_body = {"success": True}
    key = request.headers.get("key")
    response_body[key] = r.hgetall(key)

    return Response(dumps(response_body), status=200, mimetype="application/json")


@app.route("/key", methods=['DELETE'])
def delete_redis_key():
    status = 200
    key = request.headers.get("key")
    success = r.delete(key)

    if not success:
        status = 404
    response_body = {"success": bool(success)}

    return Response(dumps(response_body), status=status, mimetype="application/json")


@app.route("/list", methods=['POST'])
def create_redis_list():
    data = loads(request.data)
    strat = data.get("strategy")
    if strat is not None and strat == "left":
      length = r.lpush(data["key"], *data["values"])
    else:
      length = r.rpush(data["key"], *data["values"])
   
    response_body = {"length": length}
    response_body[data["key"]] = r.lrange(data["key"], 0, -1)
  
    return Response(dumps(response_body), status=200, mimetype="application/json")


@app.route("/list", methods=['GET'])
def get_entire_list():
    response_body = {"success": True}
    key = request.headers.get("key")
    response_body[key] = r.lrange(key, 0, -1) 

    return Response(dumps(response_body), status=200, mimetype="application/json")


@app.route("/list/<idx>", methods=['GET'])
def get_list_at_idx(idx):
    response_body = {"success": True}
    key = request.headers.get("key")
    response_body[key] = {}
    response_body[key][str(idx)] = r.lindex(key, idx) 

    return Response(dumps(response_body), status=200, mimetype="application/json")


@app.route("/set", methods=['POST'])
def create_add_set():
    data = loads(request.data)
    length = r.sadd(data["key"], *data["values"])
   
    response_body = {"length": length}
    response_body[data["key"]] = list(r.smembers(data["key"]))
  
    return Response(dumps(response_body), status=200, mimetype="application/json")


@app.route("/set/<n_items>", methods=['GET'])
def get_n_items_set(n_items):
    response_body = {"success": True}
    key = request.headers.get("key")
   
    response_body = {key: list(r.srandmember(key, n_items))}
  
    return Response(dumps(response_body), status=200, mimetype="application/json")


@app.route("/set", methods=['GET'])
def get_set():
    response_body = {"success": True}
    key = request.headers.get("key")
   
    response_body = {key: list(r.smembers(key))}
  
    return Response(dumps(response_body), status=200, mimetype="application/json")


def start_api(address, port, clnt_cert=None, clnt_key=None):
    if clnt_cert is None or clnt_key is None:
      app.run(host=address, port=port, debug=False)
    else:
      app.run(host=address, port=port, 
              ssl_context=(clnt_cert, clnt_key), debug=False)


if api_cert is None or api_key is None: 
  start_api(api_address, api_port)
else:
  start_api(api_address, api_port, api_cert, api_key)

