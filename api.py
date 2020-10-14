import os
import logging
from json import loads, dumps
from argparse import ArgumentParser

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
args = vars(parser.parse_args())

api_address = args["address"]
api_port = args["port"]
api_cert = args["cert"]
api_key = args["key"]


@app.route("/rota", methods=['POST'])
def receive_sensor_data():
    data = loads(request.data)
    log.warning("Received a POST request")
    response_body = {"success": True, "data": data }
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

