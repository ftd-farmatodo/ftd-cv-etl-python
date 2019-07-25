# -*- coding: utf-8 -*-
import json
import logging

from services.deliverydb import delivery_db_service
from services.backend3 import oms_service

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

rows = delivery_db_service.executeQuery(delivery_db_service.SQL_GET_ORDERS_TO_SEND_TO_SIM)

records = []

for count, row in enumerate(rows):
    record = {
        "orderId": row[0],
        "skipAttemptsValidation":  True
    }
    logging.debug(record)
    records.append(record)
    try:
        response = oms_service.send_order_to_sim(record)
        logging.debug("order #" + str(row[0]) + " -> Response: " + json.dumps(response.json()))
    except Exception as ex:
        logging.exception(ex)
