# -*- coding: utf-8 -*-
import logging

# from services.ftd import backend3_oms_service
from services.ftd import core2_oms_service

logging.basicConfig(level=logging.DEBUG)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

tracing = []

# consultar las ordenes que se deben reimpulsar a SIM
rows = [[505774]]
# rows = delivery_db_service.get_orders_to_send_to_sim()

for count, row in enumerate(rows):
    try:
        request = {
            "orderId": row[0],
            "skipAttemptsValidation":  True
        }
        response = core2_oms_service.send_order_to_sim(request)
        record = {
            "orderId": row[0],
            "code":  response['code'],
            "message": response['message']
        }
        tracing.append(record)
    except Exception as ex:
        logging.exception(ex)

logging.info(tracing)
