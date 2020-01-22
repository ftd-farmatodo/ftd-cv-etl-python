# -*- coding: utf-8 -*-
import json
import logging

from services.ftd import core2_oms_service, delivery_db_service

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

tracing = []

rows = delivery_db_service.get_customers_20_to_send_to_atom()
logging.info("# of customers: " + str(len(rows)))

for count, row in enumerate(rows):
    try:
        request = {
            "customerId": row[0],
            "sourceCode":  "2.0"
        }
        response = core2_oms_service.send_customer_to_atom(request)
        record = {
            "customerId": row[0],
            "atomId":  response['atomId'],
            "source": response['source']
        }
        logging.info(json.dumps(record))
        tracing.append(record)
    except Exception as ex:
        logging.exception(ex)

# logging.info(tracing)
