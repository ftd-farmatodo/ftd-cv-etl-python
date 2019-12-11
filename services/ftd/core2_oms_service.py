import json
import logging

import requests

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# CORE2_DELIVERY_BASE_URL = 'http://localhost:7001/DeliveryWS'
# CORE2_DELIVERY_BASE_URL = 'http://10.193.0.9:11103/DeliveryWS'
# CORE2_DELIVERY_BASE_URL = 'http://10.232.8.2:11103/DeliveryWS'
CORE2_DELIVERY_BASE_URL = 'http://10.193.0.6:11103/DeliveryWS'
# CORE2_DELIVERY_BASE_URL = 'http://10.193.0.2:11103/DeliveryWS'


def send_order_to_rms(request):
    logging.debug("method: send_order_to_rms() -> Request: " + str(request))
    try:
        url = CORE2_DELIVERY_BASE_URL + '/v1/order/sendOrderToRMS'
        logging.debug("method: send_order_to_rms() -> URL Service: " + url)
        response = requests.post(url, data=json.dumps(request), headers={'content-type': 'application/json'})
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
        url = CORE2_DELIVERY_BASE_URL + '/v1/order/sendOrderToSIM'
        logging.debug("method: send_order_to_sim() -> URL Service: " + url)
        response = requests.post(url, data=json.dumps(request), headers={'content-type': 'application/json'})
        logging.debug("method: sen_order_to_sim() -> Response: " + json.dumps(response.json()))
        return response.json()
    except Exception as ex:
        logging.exception(ex)
        return json.dumps({
            "code": "Exception",
            "message": ex.message
        })
