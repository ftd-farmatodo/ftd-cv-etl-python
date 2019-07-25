# -*- coding: utf-8 -*-
import logging

from services.deliverydb import delivery_db_service
from services.backend3 import oms_service

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

tracing = []

# consultar las ordenes que se deben reimpulsar a RMS
rows = delivery_db_service.executeQuery(delivery_db_service.SQL_GET_ORDERS_TO_SEND_TO_RMS)

for count, row in enumerate(rows):
    request = {
        "orderId": row[0],
        "skipAttemptsValidation":  True
    }
    try:
        response = oms_service.send_order_to_rms(request).json()
        record = {
            "orderId": row[0],
            "code":  response['code'],
            "message": response['message']
        }
        tracing.append(record)
    except Exception as ex:
        logging.exception(ex)

logging.info(tracing)
