# -*- coding: utf-8 -*-
import logging

from services.delivery import delivery_db_service

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

delivery_db_connection = delivery_db_service.get_connection()

tracing = []

# consultar las ordenes que se deben reimpulsar a SIM
items = [206600052]
stores = [2, 3, 4, 6, 7, 9, 11, 14, 15, 16, 19, 20, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 37, 39, 40, 41, 42, 43, 44,
          45, 46, 47, 50, 51, 52, 53, 54, 60, 61, 62, 63, 64, 65, 67, 68, 69, 71, 72, 73, 74, 76, 79, 80, 81, 83, 85,
          86, 87, 88, 89, 995, 996, 997, 1000, 1001]

logging.info("# items: " + str(len(items)))
logging.info("# stores: " + str(len(stores)))

for item in items:
    for store in stores:
        try:
            record = (store, item, 100)
            logging.info(record)
            delivery_db_service.update_store_stock_stock(delivery_db_connection, store, item, 100)
            tracing.append(record)
            delivery_db_connection.commit()
        except Exception as ex:
            logging.exception(ex)
            delivery_db_connection.rollback()

delivery_db_connection.close()
# logging.info(tracing)
