# -*- coding: utf-8 -*-
import json
import logging

import requests

from services.datastore import constants

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def save(request):
    logging.debug("method: save() -> Request: " + str(request))
    try:
        res = requests.post(constants.URL_API_CREATE_CONFIGURATION_PROPERTY, data=request)
        logging.info("method: save() -> Response: " + json.dumps(res.json()))
    except Exception as e:
        logging.exception("method: save() -> Error. No es posible persistir la información.")


def delete(request):
    logging.debug("method: delete() " + str(request))
