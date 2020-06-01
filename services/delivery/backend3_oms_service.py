import json
import logging

import requests

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# BACKEND3_OMS_BASE_URL = 'http://localhost:8080/oms'
BACKEND3_OMS_BASE_URL = 'https://3-1-0-dot-soap-dot-stunning-base-164402.appspot.com'
payload = {'skipAttemptsValidation': 'true'}
headers = {'content-type': 'application/json'}


def send_order_to_rms(request):
    logging.debug("method: send_order_to_rms() -> Request: " + str(request))
    try:
        url = BACKEND3_OMS_BASE_URL + '/oms/v3/order/' + str(request) + '/rms'
        logging.info("method: send_order_to_rms() -> URL Service: " + url)
        response = requests.post(url, params=payload, headers=headers)
        logging.debug("method: send_order_to_rms() -> Response: " + json.dumps(response.json()))
        return response.json()
    except Exception as ex:
        logging.exception(ex)
        return json.dumps({
            "code": "Exception",
            "message": ex.message
        })


def send_order_to_sim(request):
    logging.debug("method: send_order_to_sim() -> Request: " + str(request))
    try:
        url = BACKEND3_OMS_BASE_URL + '/oms/v3/order/' + str(request) + '/sim'
        logging.info("method: send_order_to_sim() -> URL Service: " + url)
        response = requests.post(url, params=payload, headers=headers)
        logging.debug("method: send_order_to_sim() -> Response: " + json.dumps(response.json()))
        return response.json()
    except Exception as ex:
        logging.exception(ex)
        return json.dumps({
            "code": "Exception",
            "message": ex.message
        })
