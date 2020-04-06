# -*- coding: utf-8 -*-
import logging

from services.delivery import delivery_db_service

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

delivery_db_connection = delivery_db_service.get_connection()

tracing = []

# listado de items a los que se les va a crear un registro en la tabla
items = [1002941, 1004009, 1004092, 1015423, 1021448, 1024706, 1026200, 1026814, 1027967, 1029027, 1029222, 1039132,
         1047859, 1048009, 1051956, 1053395, 1055120, 1055549, 1056194, 1061240, 206600044, 206600052, 206600061,
         206650041, 207050072, 207100050, 207100068, 207150065, 207150081, 207150090, 207150102, 207150129, 207450076,
         207500096, 207500109, 207600071, 207700063, 207750061, 207800064, 207800072, 207800081, 207800099, 207800110,
         207800136, 207800152, 207850061, 207900073, 207900090, 207900102, 207900111, 207950062, 207950071, 208000069,
         208000077, 208100086, 208100107, 208150139, 208300070, 208300096, 208300109, 208300117, 208300125, 208300133,
         208300141, 208300150, 208300176, 208300184, 208300192, 208300205, 208400062, 208400071, 208400097, 208400126,
         208400151, 208400169, 208400185]
logging.info("# items: " + str(len(items)))
uploaded = 0
logging.info("uploaded: " + str(uploaded))

size = len(items)
counter = 1
for item in items:
    try:
        record = (counter, item, uploaded)
        logging.info(record)
        delivery_db_service.create_log_updated_item(delivery_db_connection, item, uploaded)
        tracing.append(record)
        delivery_db_connection.commit()
    except Exception as ex:
        logging.exception(ex)
        delivery_db_connection.rollback()
    counter = counter + 1

delivery_db_connection.close()
logging.info(tracing)
