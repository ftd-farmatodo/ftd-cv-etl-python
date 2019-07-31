import json
import logging

import requests

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

OMS_BASE_URL = 'http://localhost:8080/oms'


def send_order_to_sim(request):
    logging.debug("method: send_order_to_sim() -> Request: " + str(request))
    url = OMS_BASE_URL + '/v3/order/sim'
    response = requests.post(url, data=json.dumps(request), headers={'content-type': 'application/json'})
    logging.debug("method: sen_order_to_sim() -> Response: " + json.dumps(response.json()))
    if response.status_code == 200:
        return response.json()
    else:
        return json.dumps({
            "code": "Exception",
            "message": ""
        })


def send_order_to_rms(request):
    logging.debug("method: send_order_to_rms() -> Request: " + str(request))
    url = OMS_BASE_URL + '/v3/order/rms'
    response = requests.post(url, data=json.dumps(request), headers={'content-type': 'application/json'})
    logging.debug("method: send_order_to_rms() -> Response: " + json.dumps(response.json()))
    if response.status_code == 200:
        return response.json()
    else:
        return json.dumps({
            "code": "Exception",
            "message": ""
        })
