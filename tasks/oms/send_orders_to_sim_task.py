# -*- coding: utf-8 -*-
import logging

from services.deliverydb import delivery_db_service
from services.backend3 import oms_service

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

tracing = []

# consultar las ordenes que se deben reimpulsar a SIM
rows = delivery_db_service.get_orders_to_send_to_sim()

for count, row in enumerate(rows):
    request = {
        "orderId": row[0],
        "skipAttemptsValidation":  True
    }
    try:
        response = oms_service.send_order_to_sim(request).json()
        record = {
            "orderId": row[0],
            "code":  response['code'],
            "message": response['message']
        }
        tracing.append(record)
    except Exception as ex:
        logging.exception(ex)

logging.info(tracing)
