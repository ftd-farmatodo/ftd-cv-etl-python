# -*- coding: utf-8 -*-
import json
import logging

from services.ftd import delivery_db_service
from services.ftd import core2_oms_service

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

tracing = []

# consultar las ordenes que se deben reimpulsar a RMS
rows = delivery_db_service.get_orders_to_send_to_rms()
logging.info("# de ordenes: " + str(len(rows)))

for count, row in enumerate(rows):
    try:
        request = {
            "orderId": row[0],
            "skipAttemptsValidation":  True
        }
        response = core2_oms_service.send_order_to_rms(request)
        record = {
            "orderId": row[0],
            "code":  response['code'],
            "message": response['message']
        }
        logging.info(json.dumps(record))
        tracing.append(record)
    except Exception as ex:
        logging.exception(ex)

# logging.info(tracing)
