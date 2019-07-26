# -*- coding: utf-8 -*-
import json
import logging

# from services.ftd import backend3_oms_service
from services.ftd import core2_oms_service

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

tracing = []

# consultar las ordenes que se deben reimpulsar a SIM
# rows = [[6608825]]
rows = [[6608825], [6552674], [6628250], [6558629], [6673837], [6538171], [6591795], [6603300], [6625779], [6656303],
        [6623239], [6572228], [6570760], [6538171], [6561210], [6520081], [6609608], [6522244], [6604912], [6601962],
        [6656821], [6562113], [6494695], [6565727], [6613387], [6618333], [6453862], [6560374], [6608672], [6542380],
        [6624867], [6556086], [6632317], [6526741], [6567923], [6643233], [6570582], [6627992], [6607526], [6613438],
        [6597145], [6634232], [6427972], [6478587], [6608225], [6419248], [6556086], [6602445], [6498300], [6427901],
        [6624091], [6561210], [6458898]]
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
        logging.info(json.dumps(record))
        tracing.append(record)
    except Exception as ex:
        logging.exception(ex)

# logging.info(tracing)
