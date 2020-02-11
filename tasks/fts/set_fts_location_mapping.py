# -*- coding: utf-8 -*-
import logging

from services.delivery import delivery_db_service
from services.fts import fts_utility_service_db, fts_ftretail_service_db

logging.basicConfig(level=logging.INFO)
logging.Formatter('%(asctime)s %(levelname)s %(message)s')

fts_db_connection = fts_utility_service_db.get_connection()

# consultar las tiendas de Domicilios
locations = delivery_db_service.get_stores()
logging.info("# of stores: " + str(len(locations)))

for count, row in enumerate(locations):
    try:
        logging.info(row)
        fts_utility_service_db.insert_location_mapping(fts_db_connection, 1995, row[1])
        fts_db_connection.commit()
    except Exception as ex:
        logging.exception(ex)
        fts_db_connection.rollback()

fts_db_connection.close()
