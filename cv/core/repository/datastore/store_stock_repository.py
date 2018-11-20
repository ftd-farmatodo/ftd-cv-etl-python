# -*- coding: utf-8 -*-
import json
import logging
import requests
from cv.core.common import constants

# logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='example.log')
# create logger
logger = logging.getLogger('store_stock_repository')
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

def update(request):
    # logging.debug("method: update: " + json.dumps(request))
    try:
        response = requests.post(constants.URL_API_SAVE_STORE_STOCK, data=json.dumps(request))
        logging.info("method: update() -> Request: " + json.dumps(request) + " | Response: " + json.dumps(response.json()))
    except Exception as e:
        logging.exception("method: update() -> Request: " + json.dumps(request) + " Error. No es posible persistir la información: " + e)
