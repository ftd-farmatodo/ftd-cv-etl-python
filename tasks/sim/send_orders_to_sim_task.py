# -*- coding: utf-8 -*-
import json
import logging
import re
from logging.handlers import TimedRotatingFileHandler

from services.delivery import backend3_oms_service
from services.sim import sim_db_service

# create logger with 'xxx'
log = logging.getLogger('send_orders_to_sim_task')
log.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# create file handler which logs even debug messages
fh = TimedRotatingFileHandler('C:/tmp/logs/task.log', when="midnight", interval=1)
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)
fh.suffix = "%Y%m%d"
fh.extMatch = re.compile(r"^\d{8}$")

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)

# add the handlers to the logger
log.addHandler(fh)
log.addHandler(ch)

log.info("Start: send_orders_to_sim_task")

# consultar las ordenes que se deben reimpulsar a SIM
rows = sim_db_service.get_orders_to_send_to_sim()
log.info("#" + str(len(rows)) + " SIM open customer orders.")

for count, row in enumerate(rows):
    try:
        orderID = int(row[0])
        response = backend3_oms_service.send_order_to_sim(orderID)
        record = {
            "orderId": orderID,
            "code": response["code"],
            "message": response["message"]
        }
        log.info("#" + str(count) + ": " + str(json.dumps(record)))
    except Exception as ex:
        log.exception(ex)

log.info("Finish: send_orders_to_sim_task")
