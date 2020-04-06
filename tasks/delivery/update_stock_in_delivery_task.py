# -*- coding: utf-8 -*-
import logging

from services.delivery import delivery_db_service

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

delivery_db_connection = delivery_db_service.get_connection()

tracing = []

# consultar las ordenes que se deben reimpulsar a SIM
items = [101002941,
101004009,
101004092,
101015423,
101021448,
101024706,
101026200,
101026814,
101027967,
101029027,
101029222,
101039132,
101047859,
101048009,
101051956,
101053395,
101055120,
101055549,
101056194,
101061240,
206600044,
206600052,
206600061,
206650041,
207050072,
207100050,
207100068,
207150065,
207150081,
207150090,
207150102,
207150129,
207450076,
207500096,
207500109,
207600071,
207700063,
207750061,
207800064,
207800072,
207800081,
207800099,
207800110,
207800136,
207800152,
207850061,
207900073,
207900090,
207900102,
207900111,
207950062,
207950071,
208000069,
208000077,
208100086,
208100107,
208150139,
208300070,
208300096,
208300109,
208300117,
208300125,
208300133,
208300141,
208300150,
208300176,
208300184,
208300192,
208300205,
208400062,
208400071,
208400097,
208400126,
208400151,
208400169,
208400185]
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
