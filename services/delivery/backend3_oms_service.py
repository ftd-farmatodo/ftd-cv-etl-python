import json
import logging

import requests

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# BACKEND3_OMS_BASE_URL = 'http://localhost:8080/oms'
BACKEND3_OMS_BASE_URL_COL = 'https://soap-dot-stunning-base-164402.appspot.com'
BACKEND3_OMS_BASE_URL_Vzl = 'https://soap-dot-oracle-services-vzla.uc.r.appspot.com'
payload = {'skipAttemptsValidation': 'true'}
headers = {'content-type': 'application/json'}


def send_order_to_rms_col(request):
    logging.debug("method: send_order_to_rms() -> Request: " + str(request))
    try:
        url = BACKEND3_OMS_BASE_URL_COL + '/oms/v3/order/' + str(request) + '/rms'
        logging.info("method: send_order_to_rms() -> URL Service: " + url)
        response = requests.post(url, params=payload, headers=headers)
        logging.debug("method: send_order_to_rms() -> Response: " + json.dumps(response.json()))
        return response.json()
    except Exception as ex:
        logging.exception(ex)
        return json.dumps({
            "code": "Exception",
            "message": str(ex)
        })


def send_order_to_sim_col(request):
    logging.debug("method: send_order_to_sim() -> Request: " + str(request))
    try:
        if str(request).find('-') != -1:

            aux = str(request).find('-')
            order_id = str(request)[0:aux]
            post = str(request)[aux+1:len(str(request))]

            url = BACKEND3_OMS_BASE_URL_COL + '/oms/v3/order/' + order_id + '/sim?postfix=' + post
            logging.info("method: send_order_to_sim() -> URL Service: " + url)
            response = requests.post(url, params=payload, headers=headers)
            print('Orden con CMP: ' + request)
        else:

            url = BACKEND3_OMS_BASE_URL_COL + '/oms/v3/order/' + str(request) + '/sim'
            logging.info("method: send_order_to_sim() -> URL Service: " + url)
            response = requests.post(url, params=payload, headers=headers)


        logging.debug("method: send_order_to_sim() -> Response: " + json.dumps(response.json()))
        return response.json()
    except Exception as ex:
        logging.exception(ex)
        return json.dumps({
            "code": "Exception",
            "message": str(ex)
        })


def send_order_to_sim_vzl(request):
    logging.debug("method: send_order_to_sim() -> Request: " + str(request))
    try:
        if str(request).find('-') != -1:

            aux = str(request).find('-')
            order_id = str(request)[0:aux]
            post = str(request)[aux+1:len(str(request))]

            url = BACKEND3_OMS_BASE_URL_Vzl + '/oms/v3/order/' + order_id + '/sim?postfix=' + post
            #print(url)
            logging.info("method: send_order_to_sim() -> URL Service: " + url)
            response = requests.post(url, params=payload, headers=headers)
            print('Orden con CMP: ' + request)
        else:

            url = BACKEND3_OMS_BASE_URL_Vzl + '/oms/v3/order/' + str(request) + '/sim'
            logging.info("method: send_order_to_sim() -> URL Service: " + url)
            response = requests.post(url, params=payload, headers=headers)


        logging.debug("method: send_order_to_sim() -> Response: " + json.dumps(response.json()))
        return response.json()
    except Exception as ex:
        logging.exception(ex)
        return json.dumps({
            "code": "Exception",
            "message": str(ex)
        })
